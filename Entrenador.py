import yaml

def obtener_clasificacion_manual(correos):                             # Función para que el usuario clasifique manualmente los correos
    clasificacion_usuario = []
    
    for correo in correos['messages']:
        print("----------------------------------------------------")
        print(f"Correo: {correo}")
        while True:
            try:
                etiqueta = input("¿Es SPAM? (Escribe 'sí' para spam o 'no' para no spam): ").lower()
                if etiqueta not in ['si', 'no']:
                    raise ValueError("Entrada inválida. Debes escribir 'sí' o 'no'.")
                break
            except ValueError as e:
                print(f"Error: {e}")
        
        clasificacion_usuario.append({
            'label': 'Spam' if etiqueta == 'si' else 'NO spam',
            'message': correo
        })
    
    return clasificacion_usuario

def clasificar_manual(archivo_correos, archivo_salida):                # Función para clasificar y guardar la salida
    with open(archivo_correos, 'r', encoding='utf-8') as archivo:
        correos = yaml.safe_load(archivo)

    clasificacion_usuario = obtener_clasificacion_manual(correos)      # Obtener la clasificación manual del usuario
    
    with open(archivo_salida, 'w', encoding='utf-8') as archivo_salida:
        yaml.dump(clasificacion_usuario, archivo_salida, allow_unicode=True, default_flow_style=False)

    print(f"Clasificación manual guardada en '{archivo_salida}'.")

# Ejecutar el proceso de clasificación manual
clasificar_manual('Correos_ParaEntrenar.yaml', 'CorreosClasificados_Usuario.yaml')
