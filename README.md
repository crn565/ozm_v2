# ozm_v2
Desagregación del consumo energético mediante NILMTK usando datos 6 medidores OZMmeter

# DSUALM: NILM Dataset
Este repositorio es parte del Trabajo Final de Máster en Tecnologias y Aplicaciones en Ingenieria Informatica  de  Carlos Rodriguez Navarro (https://www.soloelectronicos.com/). El proyecto esta coordinado  por el docente e investigador  Dr. Alfredo Alcayde  cuyo  actividad  se desarrolla en la Universidad de Almeria.

El objetivo de este trabajo es,  usando los datos arrojados por dispositivos OZM, mostrar el uso y potenciales aplicaciones de la herramienta de desagregación de la demanda Non-Intrusive Load Monitoring Toolkit ([NILMTK](http://nilmtk.github.io/)) a través de la implementación de un caso real que involucra la creación de un dataset de uso público proveniente  de los datos  arrrojados por varios OZM dispuestos en la Escuela Politécnica Superior de la Universidad de Almeria.

HDF5 es un formato de datos jerárquico que se usa en el NILMTK como fuente datos basado en HDF4 y NetCDF (otros dos formatos de datos jerárquicos).El formato de datos jerárquico, versión 5 (HDF5), es un formato de archivo de código abierto que admite datos grandes, complejos y heterogéneos. HDF5 utiliza una estructura similar a un “directorio de archivos” que le permite organizar los datos dentro del archivo de muchas formas estructuradas diferentes, como lo haría con los archivos en su computadora. El formato HDF5 también permite la incrustación de metadatos, lo que lo hace autodescriptivo .Esto significa que cada archivo, grupo y conjunto de datos puede tener metadatos asociados que describen exactamente cuáles son los datos.

Un beneficio clave de tener metadatos adjuntos a cada archivo, grupo y conjunto de datos es que esto facilita la automatización sin la necesidad de un documento de metadatos separado (y adicional). Usando un lenguaje de programación, como R o Python, podemos obtener información de los metadatos que ya están asociados con el conjunto de datos y que podríamos necesitar para procesar el conjunto de datos.

El formato HDF5 es un formato comprimido. El tamaño de todos los datos contenidos en HDF5 está optimizado, lo que reduce el tamaño general del archivo. Sin embargo, incluso cuando están comprimidos, los archivos HDF5 a menudo contienen grandes volúmenes de datos y, por lo tanto, pueden ser bastante grandes. Un atributo poderoso de HDF5 es data slicingmediante el cual se puede extraer un subconjunto particular de un conjunto de datos para su procesamiento. Esto significa que no es necesario leer el conjunto de datos completo en la memoria (RAM); muy útil para permitirnos trabajar de manera más eficiente con conjuntos de datos muy grandes (gigabytes o más).


Con los datos arrojados por el OZM se ha creado un nuevo dataset denominado **DSUALM (Dataset de la Universidad de Almeria )** almacenandose  en formato HDFS5 y  puede ser descargado directamente desde este repositorio. Adicionalmente,para capturar los datos y los correspondientes metadatos del OZM,  se proporciona un nuevo convertidor (convert_ualm) basado en IAWE , con el fin de ser utilizado en NILMTK (este  software igualmente tambien se encuentra en este repositorio).

EL NILM o Non-Intrusive Load Monitoring, es decir la desagregación no intrusiva de la demanda  es una técnica computacional para la estimación del consumo individual de diversos dispositivos utilizando para ello la lectura agregada de un único medidor de energía (Smart Meter, SM). (https://ieeexplore.ieee.org/document/192069?section=abstract) (https://spiral.imperial.ac.uk/handle/10044/1/49452).  Gracias a las ventajas en cuanto instalación , coste e implementación, éste concepto ha tomado relevancia en los últimos años en el ámbito de las Smart Grids, al aportar una estimación de los hábitos de consumo de los clientes sin la necesidad de un despliegue masivo de contadores inteligentes en cada punto de consumo.

En este contexto vamos a ver una herramienta o toolkit open software llamado NILMTK que nos va a ayudar a comparar algoritmos para implementar la desagregación ( además particularmente no contempla un uso diferente a este). Es de destacar que aunque en 2021 no ha tenido tanta relevacia, el NILMTK es un software plenamente vigente como lo demuestran las numerosas publicaciones referidas a este tema (https://github.com/crn565/dsualm/blob/main/Publicaciones.ipynb ).

Para el análisis de la desagregación , necesitamos recolectar datos del consumo centralizado , lo cual nos va permitir a creación de un nuevo dataset el cual puede ser analizado usando las funciones de NILMTK lo que permite, por ejemplo, visualizar los datos de potencia en un determinado periodo u obtener estadísticas de energía del dataset.

Posteriormente, en la etapa de preprocesamiento se toman decisiones en línea con los análisis realizados, con el objetivo de preparar correctamente los datos para del entrenamiento de los modelos de desagregación. Básicamente, el entrenamiento de un modelo consiste en enseñarle a reconocer por separado las características de los dispositivos para luego identificarlos dentro de una señal agregada. El entrenamiento contempla el uso de los algoritmos Combinatorial Optimization (CO) y Factorial Hidden Markov Model (FHMM).


Dentro de loss posibles beneficios de esta técnica  destacan los siguientes:

- Información detallada  desagregada en la factura eléctrica al consumidor 

- Identificacion de la actividad de los convivientes que usen esa instalacion electrica ( por ejemplo personas dependientes o ancianos) 

- Aplicaciones en programas de respuesta a la demanda o *demand response* (DR) 

- Identificación de averías 

- Investigaciones relacionadas con el  consumo ilegal  o fraudulento de energía

- Interoperabilidad de dispositivos de almacenamiento

- Reducción de las pérdidas de transmisión y distribución

- Control del flujo de energía bidireccional

- Aplicación de los sistemas de gestión de la demanda (DSM)

- Control de calidad de la energía

- Medición del consumo en tiempo real

- Eficiencia energética/uso racional de la energía

- Tarifas dinámicas

- Integración de plantas de potencia virtuales (VPP)

- Trazabilidad del origen de la energía.

- etc


## NILMTK

NILMTK ,que como comentabamos es ampliamente usado por investigadores (https://github.com/crn565/dsualm/blob/main/Publicaciones.ipynb) es un kit de herramientas de código abierto y gratuito diseñado específicamente para permitir un acceso fácil y brindar un análisis comparativo de algoritmos de desagregación de demanda en diversos datasets. NILMTK proporciona un *pipeline* completo, intérpretes de diversos datasets y métricas de precisión, lo que reduce la barrera de entrada para investigadores y desarrolladores. 

Se recomienda instalar NILMTK bajo un *enviroment* de paquetes de Python, específicamente [Anaconda](https://www.anaconda.com/distribution/). Una guía de instalación de NILMTK en Windows se encuentra en los [siguientes enlacse](https://soloelectronicos.com/2021/07/02/instalacion-del-nilmtk/) y en https://soloelectronicos.com/2021/10/18/instalacion-nilmtk-con-anaconda-2021/ 

Adicionalmente, toda la información sobre NILMTK se encuentra en [nilmtk.github.io](http://nilmtk.github.io/).



## Nuevo Dataset DSUALM

Dentro de las instalaciones de la Escuela Politécnica Superior de la Universidad de Almeria  está equipada con un cuadro eléctrico con diversos medidores.

Estos medidores registran el consumo agregado y consumos individuales de determinados dispositivos .

Gracias a esto, se han registrado datos de consumo y se han almacenado junto con sus metadatos en un dataset:

-Medidor principal

-Medidor 2 (boiler) 

-Medidor 3 (fan)  

-Medidor 4 (freezer)  

-Medidor 5 (monitor) 

-Medidor 6 (vacuum cleaner) 






### Adquisición de datos

DSUAL  contiene datos agregados y metadatos de un sistema  de seis dispositivos de consumo. La siguiente tabla resume las medidas registradas en el dataset.

| Medidor                              | Medidas Registradas | Periodo de Muestreo |
| ------------------------------------ | ------------------- | ------------------- |
| 1x Medidor principal               ) | P, Q ,V,I,PHI,VA,F  | 1 segundo           |
| 5 x Medidores de Dispositivos        | P, Q, V,I,PHI,VA,F  | 1 segundo           |

El medidor principal  mide la potencia P y Q agregada,  permitiendo registrar P, Q, V e I para cada una de ellas. En cuanto a los dispositivos, se cuenta con mediciones diferenciadas para estos . 



### Convertidor NILMTK

Para la creación de un dataset compatible con NILMTK es necesario contar con un convertidor que estructure los datos y sus metadatos en el formato HDF5. En el presente trabajo se utiliza como referencia el convertidor IAWE previamente desarrollado, incorporándole modificaciones para que los datos extraídos sean compatibles.

- El convertidor y los metadatos se pueden [descargar desde este enlace].
- Para su mejor comprensión, se ha elaborado una [guía de implementación y uso del convertidor]

### Análisis y modelos de desagregación 

Con la ayuda de las diversas funciones de NILMTK se analizan datos y metadatos del dataset DEPS. 

En los siguientes notebooks se presentan diversos análisis y preprocesamiento necesario para posteriormente generar y comparar diversos modelos de desagregación usando varios periodos y métodos de muestreo basados en los algoritmos CO (*Combinatorial Optimisation*) y FHMM (*Factorial Hidden Markov Model*):

- [1 -PREPROCESADO DE LOS DATOS DEL OZM] 

- [2- CARGA Y ANALISIS DE LOS DATOS DEL OZM] 

- [3.- ANALISIS Y ESTADISTICAS] 

- [4. - PREPROCESAMIENTO] 

- [5.- ENTRENAMIENTO]

- [6.- VALIDACION] 

- [7.- DESAGREGACION] 

- [8.- METRICAS ]
