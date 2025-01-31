# ✉️ Clasificador de Correos SPAM
#### 🐍 Proyecto sencillo de machine learning con PYTHON.
> Este proyecto permite clasificar correos electrónicos como SPAM o NO SPAM utilizando un sistema basado en la comparación entre las clasificaciones manuales del usuario y un modelo de clasificación de IA. El sistema utiliza un conjunto de herramientas en Python para cargar, procesar y comparar los correos, además de generar estadísticas sobre la precisión de la clasificación.

#### 🤖 Visualización de codigo funcionando
---
![](/Cuestionario.jpg)

#### 🚀 Habilidades de programación adquiridas.
> + **Procesamiento de Datos y Manejo de Archivos:** 
>   + Lectura y escritura de archivos **YAML (pyyaml)** para almacenar y recuperar datos estructurados.
>   + Manipulación de **estructuras de datos** como listas, diccionarios y conjuntos para organizar información.
>+ **Programación Orientada a Objetos (POO):**
>   + Definición de **clases y métodos** para encapsular la lógica del clasificador, el procesador y el comparador.
>   + Uso de **herencia y polimorfismo**.
>+ **Procesamiento de Texto y NLP (Natural Language Processing):** 
>   + **Tokenización** de correos electrónicos para analizar palabras clave.
>   + **Preprocesamiento de texto** (stopword removal, stemming, lematización).
>   + Construcción de **modelos de clasificación** basados en frecuencias de palabras.
>+ **Probabilidad y Estadística:** 
>   + Cálculo de probabilidades condicionales para clasificar correos mediante **modelos probabilísticos**.
>   + Aplicación del **teorema de Bayes** en la clasificación de textos (clasificador Naïve Bayes).
>   + Construcción de **tablas de frecuencia** de palabras en distintos tipos de correos.
> + **Desarrollo de Modelos de Clasificación:**
>   + Implementación de un clasificador probabilístico basado en estadísticas de **palabras en correos previos**.
>   + Comparación de **predicciones de la IA** con clasificaciones humanas para medir **precisión, recall y F1-score**.
> + **Comparación y Evaluación de Modelos:**
>   + **Cálculo de métricas** como precisión, recall y F1-score para **evaluar el rendimiento de la IA** frente a las clasificaciones del usuario.
>   + Visualización de datos para entender cómo se distribuyen las palabras en correos clasificados.

#### 📂 Estructura del Proyecto
    ClasificadorCorreos/
    │── Correos_ParaEntrenar.yaml   # Correos a clasificar manualmente por el usuario
    │── CorreosClasificados_Usuario.yaml  # Correos clasificados manualmente por el usuario
    │── CorreosClasificados_IA.yaml     # Clasificación generada por la IA
    │── TablaProbabilidad.yaml           # Tabla de probabilidad para clasificación
    │── Entrenador.py                    # Código para clasificación manual por parte del usuario
    │── Procesador.py                    # Código para procesar los correos y generar la tabla de probabilidad
    │── Clasificador.py                  # Código para clasificar correos según la tabla de probabilidad
    │── Comparador.py                    # Código para comparar las clasificaciones de la IA y el usuario


#### 🎮 ¿Cómo funciona?
>- El sistema permite clasificar los correos manualmente como SPAM o NO SPAM, y luego entrenar un modelo de IA con las respuestas.
>- Utiliza técnicas de procesamiento de texto para calcular la probabilidad de que un correo sea SPAM, basándose en la frecuencia de palabras relevantes.
>- Por último, se compara la clasificación generada por la IA con las respuestas del usuario y se calcula la precisión del modelo.

#### ✨  Características Destacadas
>##### Este proyecto destaca por:
>- **Clasificación Manual y Automática:** 
>Los usuarios pueden clasificar los correos manualmente y generar una clasificación automatizada basada en un modelo de probabilidad.
>- **Comparación Precisa:** 
>El sistema permite medir la precisión de la clasificación de la IA en comparación con las respuestas del usuario.
>- **Flexibilidad:** 
>La tabla de probabilidad puede ajustarse fácilmente con nuevas palabras relevantes.

#### 📌 Mejoras Futuras
>- **Interfaz Gráfica:** 
>Implementación de una interfaz gráfica para facilitar la interacción con el usuario.
>- **Algoritmos Avanzados de Clasificación:** 
>Incorporar algoritmos de clasificación más avanzados, como máquinas de soporte vectorial (SVM) o redes neuronales, para mejorar la precisión.
>- **Optimización de la Precisión:** 
>Mejorar el sistema de clasificación utilizando técnicas de aprendizaje automático para ajustar el modelo a partir de nuevas clasificaciones.
---
###### ¡Gracias por revisar este proyecto! 
###### Si tienes sugerencias o mejoras, no dudes en contribuir. 🦊
