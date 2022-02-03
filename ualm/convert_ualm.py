import pandas as pd
import numpy as np
from os.path import join
from nilmtk.datastore import Key
from nilmtk.measurement import LEVEL_NAMES
from nilmtk.utils import check_directory_exists, get_datastore, get_module_directory
from nilm_metadata import convert_yaml_to_hdf5
from copy import deepcopy

def reindex_fill_na(df, idx):
    df_copy = deepcopy(df)
    df_copy = df_copy.reindex(idx)

    power_columns = [
        x for x in df.columns if x[0] in ['power']]
    non_power_columns = [x for x in df.columns if x not in power_columns]

    for power in power_columns:
        df_copy[power].fillna(0, inplace=True)
    for measurement in non_power_columns:
        df_copy[measurement].fillna(df[measurement].median(), inplace=True)

    return df_copy


column_mapping = {
    'W': ('power', 'active'),
    'A': ('current', ''),
    'PF': ('pf', ''),
    'VA': ('power', 'apparent'),
    'VAR': ('power', 'reactive'),
    'VLN': ('voltage', ""),
    'f': ('frequency', "")
}

TIMESTAMP_COLUMN_NAME = "timestamp"
TIMEZONE = "Europe/Berlin" 
#START_DATETIME, END_DATETIME = '2013-07-13', '2013-08-04'
START_DATETIME, END_DATETIME = '2021-11-10', '2021-11-12'
FREQ = "1T"
#old= 1T  nueva 1S

def convert_ualm(iawe_path, output_filename, format="HDF"):
    """
    Parameters
    ----------
    iawe_path : str
        The root path of the iawe dataset.
    output_filename : str
        The destination filename (including path and suffix).
    """

    check_directory_exists(iawe_path)
    idx = pd.date_range(start=START_DATETIME, end=END_DATETIME, freq=FREQ)
    idx = idx.tz_localize('GMT').tz_convert(TIMEZONE)

    # Open data store
    store = get_datastore(output_filename, format, mode='w')
    electricity_path = join(iawe_path, "electricity")

    print("Path ualm:",iawe_path,"/electricity") 
    # Mains data
   
    # VamoS a tener 7 appliances
    
    for chan in range(1, 8):
        key = Key(building=1, meter=chan)
        filename = join(electricity_path, "%d.csv" % chan)
        print('..Cargando el fichero  ', chan,'.csv')
        df = pd.read_csv(filename, dtype=np.float64, na_values='\\N')
        print('Leyendo fichero csv')
        print(df)
        
        df.drop_duplicates(subset=["timestamp"], inplace=True)
        df.index = pd.to_datetime(df.timestamp.values, unit='ms', utc=True) #unit='ms'
        df = df.tz_convert(TIMEZONE)
        df = df.drop(TIMESTAMP_COLUMN_NAME, 1)
        print('Conversion timestamp')
        print (df)
        
        #hasta aqui ok
        df.columns = pd.MultiIndex.from_tuples(
            [column_mapping[x] for x in df.columns],
            names=LEVEL_NAMES
        )
        print('Carga columnas')
        print(df)

        
        
        
        df = df.apply(pd.to_numeric, errors='ignore')
        df = df.dropna()
        df = df.astype(np.float32)
        df = df.sort_index()
        print('Sort_index')
        print(df)
        #hasta aqui ok
        
        
        df = df.resample("1S").mean()      #resample("1S")
        print('Resample')
        print(df)
        #aqui falla  con la potencia
        
        #df = reindex_fill_na(df, idx)
        print ('Reindexando fichero')
        print (df)
        
        assert df.isnull().sum().sum() == 0
        store.put(str(key), df)
        print ('Fichero ',chan,'cargado ok') 
        
    store.close()
    print ('Uniendo  Medadata')
    metadata_dir = join(get_module_directory(), 'dataset_converters', 'ualm', 'metadata')
    convert_yaml_to_hdf5(metadata_dir, output_filename)

    print("Realizada con exito la conversion de ualM al formato  HDF5!")

