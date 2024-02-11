# Tarea 6 - IE0217 - Estructuras abstractas de datos y algoritmos  

**Temática:** Análisis de datos en Python.

**Nombre:** Danny Solórzano Mayorga  

**Carné:** C27667  

**Docente:** Rafael Esteban Badilla Alvarado  

**Ciclo lectivo:** III-2023

### Resumen 

El objetivo de esta tarea es adquirir experiencia en el análisis de datos utilizando Python al analizar un conjunto de datos sobre vehículos. Para esto se utilizarán regresiones, clustering y servicios web.

### Requisitos de compilación

- python
- sklearn
- matplotlib
- pandas
- numpy
- make

### Compilación

1. Abra una terminal.
2. Ingrese al directorio del proyecto.

```
cd /ruta/TAREA_SEIS
```

3. Ejecute el comando `make` para ejecutar la primera parte.

```
make
```

## Respuestas de la parte teórica

**Regresión:**

1. La regresión lineal es un método estadístico utilizado para modelar la relación entre una variable dependiente y una o más variables independientes. Se diferencia de la regresión no lineal en que la relación entre las variables en la regresión lineal se modela como una línea recta, mientras que en la regresión no lineal, la relación puede seguir cualquier forma de curva.

2. Los coeficientes de regresión son los valores que se utilizan para estimar la relación entre las variables en un modelo de regresión. Proporcionan información sobre la magnitud y dirección de la relación entre las variables predictoras y la variable de respuesta.

3. El error cuadrático medio (MSE) es una medida de la calidad de un modelo de regresión que mide la diferencia cuadrada promedio entre los valores observados y los valores predichos por el modelo. Se utiliza para evaluar la precisión del modelo, donde un MSE más bajo indica un mejor ajuste del modelo a los datos observados.

4. La regresión simple involucra una variable independiente y una variable dependiente, mientras que la regresión múltiple implica más de una variable independiente y una variable dependiente. La regresión simple se utiliza cuando se estudia la relación entre dos variables, mientras que la regresión múltiple se utiliza cuando se consideran múltiples variables independientes que pueden afectar a la variable dependiente.

**Clustering:**

1. El clustering es un método de análisis de datos no supervisado que agrupa un conjunto de objetos en grupos, o "clusters", de manera que los objetos dentro de un mismo grupo sean más similares entre sí que con los objetos en otros grupos. Su objetivo principal es encontrar estructuras o patrones inherentemente presentes en los datos.

2. 
   - K-Means es un algoritmo de clustering que divide un conjunto de datos en k grupos basados en las características de los datos. Comienza eligiendo k centroides aleatorios y luego asigna cada punto de datos al centroide más cercano, recalcula los centroides y repite el proceso hasta que los centroides convergen.
   - DBSCAN (Density-Based Spatial Clustering of Applications with Noise) es un algoritmo de clustering basado en densidad que agrupa puntos en áreas de alta densidad. Utiliza dos parámetros: epsilon, que define la distancia máxima entre dos puntos para que uno sea considerado vecino del otro, y minPts, que es el número mínimo de puntos necesarios para formar un grupo.

3. La inercia en el contexto del clustering es una medida de cómo los puntos en un grupo están cerca de los centroides de ese grupo. Se utiliza para evaluar la calidad de un agrupamiento, donde una inercia más baja indica que los puntos están más cerca de sus centroides y, por lo tanto, los grupos son más compactos.

4. Los centroides son puntos representativos de cada grupo en el algoritmo K-Means. Se utilizan para calcular la distancia entre los puntos de datos y asignarlos al grupo más cercano durante la fase de asignación de clusters.

5. Los datos estructurados se refieren a datos organizados en una forma predefinida y fácilmente accesible, como tablas de bases de datos o hojas de cálculo, mientras que los datos no estructurados son datos que no siguen un formato específico y pueden incluir texto, imágenes o audio. Organizar los datos en paquetes y módulos en Python ayuda a estructurar y modularizar el código, lo que facilita su mantenimiento, reutilización y colaboración.

**Paquetes en Python (init.py):**

1. Un paquete en Python es una carpeta que contiene varios módulos relacionados entre sí. Se diferencia de un módulo en que un módulo es un solo archivo de Python que puede contener variables, funciones y clases, mientras que un paquete es una colección de módulos organizados en una estructura de directorios.

2. El archivo __init__.py dentro de un paquete de Python sirve para indicar que la carpeta es un paquete de Python y puede contener código Python que se ejecuta cuando se importa el paquete.

3. Se puede importar un módulo o función desde un paquete en Python utilizando la declaración de importación seguida del nombre del paquete y el nombre del módulo o función, separados por puntos. Por ejemplo: `import paquete.modulo` o `from paquete import funcion`.

4. La variable __all__ en el archivo __init__.py se utiliza para especificar qué módulos o funciones deben importarse cuando se importa el paquete utilizando la instrucción `from paquete import *`. Esto permite controlar qué partes del paquete están disponibles para ser importadas.

5. La ventaja de organizar el código en paquetes y módulos en Python es que facilita la estructuración y modularización del código, lo que mejora su mantenibilidad, reutilización y colaboración. Además, ayuda a evitar conflictos de nombres y a mantener un código más organizado y legible.

**Python HTTP y Servicios Web (API):**

1. Una API (Interfaz de Programación de Aplicaciones) es un conjunto de reglas y definiciones que permiten que diferentes aplicaciones se comuniquen entre sí. En el contexto de los servicios web, una API define cómo las aplicaciones pueden interactuar entre sí a través de la web.

2. Una API RESTful es un estilo de arquitectura para servicios web que utiliza HTTP y los principios REST (Transferencia de Estado Representacional) para proporcionar interoperabilidad entre sistemas informáticos en la web. Por otro lado, una API SOAP (Simple Object Access Protocol) es un protocolo de intercambio de mensajes basado en XML que define un conjunto de reglas para la comunicación entre aplicaciones distribuidas a través de la red.

3. Los pasos básicos para consumir una API utilizando Python incluyen:
   - Importar la biblioteca necesaria para hacer solicitudes HTTP, como `requests`.
   - Enviar una solicitud HTTP al servidor utilizando los métodos HTTP apropiados (GET, POST, PUT, DELETE).
   - Manejar la respuesta del servidor, que generalmente está en formato JSON o XML, dependiendo de la API.
   - Procesar los datos de la respuesta según sea necesario.

4. La autenticación de API es el proceso de verificar la identidad del usuario que intenta acceder a una API y asegurarse de que tenga los permisos adecuados para realizar las acciones solicitadas. Es importante para proteger los datos y los recursos de la API contra accesos no autorizados.

5. Los verbos HTTP (GET, POST, PUT, DELETE) se utilizan en las solicitudes a una API para indicar la acción que se debe realizar en un recurso específico. GET se utiliza para recuperar datos, POST para enviar datos, PUT para actualizar datos y DELETE para eliminar datos. Estos verbos

 proporcionan una forma estándar de interactuar con los recursos a través de la web utilizando HTTP.