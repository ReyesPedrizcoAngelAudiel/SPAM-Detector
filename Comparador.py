import yaml
#Importar los programas
#import Entrenador, Procesador, Clasificador

def cargar_clasificaciones(archivo_ia):                               
    with open(archivo_ia, 'r', encoding='utf-8') as archivo:
        clasificacion_ia = yaml.safe_load(archivo)
    return clasificacion_ia

def preguntar_al_usuario(correo, clasificacion_ia):                   
    print(f"Detecté que el siguiente correo es '{clasificacion_ia}': {correo}")
    respuesta = input("¿Es verdad? (si/no): ").strip().lower()
    return respuesta == 'si'

def comparar_clasificaciones_ia_usuario(clasificacion_ia):              
    aciertos = 0
    total = 0

    for correo_ia in clasificacion_ia:
        es_correcto = preguntar_al_usuario(correo_ia['message'], correo_ia['label'])
        total += 1                                                    
        if es_correcto:
            aciertos += 1

    return aciertos, total

def calcular_porcentaje(aciertos, total):                              
    if total == 0:
        return 0.0
    return (aciertos / total) * 100

def comparar(archivo_ia):                                              
    clasificacion_ia = cargar_clasificaciones(archivo_ia)

    aciertos, total = comparar_clasificaciones_ia_usuario(clasificacion_ia)
    porcentaje_acierto = calcular_porcentaje(aciertos, total)

    print(f"\nTotal de correos evaluados: {total}")
    print(f"Aciertos: {aciertos}")
    print(f"Precisión: {porcentaje_acierto:.2f}%")
    
#Ejecutar primero Entrenador
#Entrenador.clasificar_manual('Correos_ParaEntrenar.yaml', 'CorreosClasificados_Usuario.yaml')
#Ejecutar despues Procesador
#Procesador.procesar_correos('CorreosClasificados_Usuario.yaml')
#Ejecutar clasificador
#Clasificador.clasificar_correos('Correos_Prueba.yaml', 'TablaProbabilidad.yaml')
#Finalmente el comparador
comparar('CorreosClasificados_IA.yaml')