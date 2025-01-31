import yaml
import re
from Procesador import limpiar_mensaje  # Asumo que esta función ya limpia el mensaje

# Función para calcular la media de las probabilidades
def calcular_media(probabilidades):
    total = sum(probabilidades.values())
    return total / len(probabilidades) if probabilidades else 0

# Función para clasificar los correos utilizando media y umbral
def clasificar_correos(archivo_correos_prueba, archivo_tabla_probabilidad):
    with open(archivo_tabla_probabilidad, 'r', encoding='utf-8') as archivo:
        tabla_probabilidad = yaml.safe_load(archivo)

    with open(archivo_correos_prueba, 'r', encoding='utf-8') as archivo:
        correos_prueba = yaml.safe_load(archivo)

    umbral = 0.25  # Umbral fijo
    media_probabilidad = calcular_media(tabla_probabilidad)  # Calcular la media de las probabilidades

    clasificaciones_ia = []
    spam_count = 0
    no_spam_count = 0

    for correo in correos_prueba['messages']:
        tokens = limpiar_mensaje(correo)  # Limpiar y tokenizar el mensaje
        puntaje = sum(tabla_probabilidad.get(token, 0) for token in tokens)

        # Normalizar el puntaje utilizando la media de probabilidades
        puntaje_normalizado = puntaje / media_probabilidad if media_probabilidad != 0 else 0

        if puntaje_normalizado >= umbral:  # Comparar el puntaje normalizado con el umbral
            etiqueta = "spam"
            spam_count += 1
        else:
            etiqueta = "no spam"
            no_spam_count += 1

        clasificaciones_ia.append({
            'label': etiqueta,
            'message': correo
        })

    # Guardar las clasificaciones en el archivo "CorreosClasificados_IA.yaml"
    with open('CorreosClasificados_IA.yaml', 'w', encoding='utf-8') as archivo_salida:
        yaml.dump(clasificaciones_ia, archivo_salida, allow_unicode=True, default_flow_style=False)

    print("Clasificaciones guardadas en 'CorreosClasificados_IA.yaml'.")
    print(f"Spam clasificados: {spam_count}, No Spam clasificados: {no_spam_count}")

# Ejecutar la clasificación
clasificar_correos('Correos_Prueba.yaml', 'TablaProbabilidad.yaml')
