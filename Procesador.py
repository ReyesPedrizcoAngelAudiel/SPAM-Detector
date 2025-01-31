import yaml
import re

# Lista de artículos, preposiciones y conjunciones a eliminar
STOPWORDS = [
    "a", "al", "ante", "bajo", "cabe", "con", "contra", "de", "del", "desde", "durante", 
    "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "so", 
    "sobre", "tras", "versus", "vía", "y", "o", "u", "ni", "que", "como", "el", "la", 
    "los", "las", "un", "una", "unos", "unas", "lo", "le", "les", "me", "te", "se", 
    "nos", "os", "mi", "tu", "su", "yo", "tú", "él", "ella", "ellos", "ellas", 
    "nosotros", "vosotros", "usted", "ustedes", "esto", "eso", "aquello", "aquí", 
    "ahí", "allí", "allá", "más", "menos", "muy", "tan", "donde", "cuando", "si", 
    "no", "sí", "pero", "porque", "aunque", "además", "sin embargo", "sino", "mientras"
]

# Lista de palabras relevantes para detectar spam
PALABRAS_RELEVANTES = [
    "dinero", "oferta", "regalo", "promocion", "gana", "concurso", "premio",
    "nuevo", "mejor", "gratis", "ahorra", "comprar", "click", "haz", "tu",
    "seguro", "exito", "urgente", "ahora", "limite", "especial", "beneficio",
    "adicional", "ofrecido", "acceso", "invitado", "prueba", "sorpresa", 
    "exclusivo", "descuento", "envío", "cupon", "desbloquea", "desbloquear", 
    "contraseña", "alerta", "actualiza", "actualización", "responde", 
    "devolución", "reembolso", "solicitud", "garantía", "reserva", "limpiador", 
    "factura", "aprobado", "bajo", "increíble", "urgencia", "fácil", "rápido", 
    "confidencial", "protege", "ahorro", "aprovecha", "finaliza", "solo hoy",
    "costo", "precio", "soporte", "cliente", "seleccionado", "lotería", 
    "transferencia", "confirmar", "contacto", "seguimiento"
]

def limpiar_mensaje(mensaje):                                           # Función para limpiar y filtrar los mensajes
    mensaje_limpio = re.sub(r'[^\w\s]', '', mensaje.lower())            # Convertir el mensaje a minúsculas
    tokens = mensaje_limpio.split()                                     # Filtrar stopwords y mantener palabras relevantes por tokens
    tokens_filtrados = [token for token in tokens if token not in STOPWORDS and token in PALABRAS_RELEVANTES]
    return tokens_filtrados

def contar_palabras(tokens, contador):                                  # Función para contar la frecuencia de palabras
    for token in tokens:
        if token in contador:
            contador[token] += 1
        else:
            contador[token] = 1

def procesar_correos(archivo_yaml):                                     # Función para procesar los correos y obtener la tabla de probabilidad
    with open(archivo_yaml, 'r', encoding='utf-8') as archivo:
        correos = yaml.safe_load(archivo)
    
    contador_spam = {}                                                  # Diccionario para contar las palabras en mensajes de spam

    for correo in correos:                                              # Procesar los correos
        if correo['label'].lower() == 'spam':                           # Solo procesar correos clasificados como spam
            tokens = limpiar_mensaje(correo['message'])                 # Limpiar el mensaje y filtrar palabras
            contar_palabras(tokens, contador_spam)                      # Contar las palabras filtradas

    total_palabras_spam = sum(contador_spam.values())                   # Calcular la tabla de probabilidad (frecuencia relativa)
    tabla_probabilidad = {palabra: frecuencia / total_palabras_spam for palabra, frecuencia in contador_spam.items()}

    with open('TablaProbabilidad.yaml', 'w', encoding='utf-8') as archivo_salida:
        yaml.dump(tabla_probabilidad, archivo_salida, allow_unicode=True, default_flow_style=False)

    print("Tabla de probabilidad guardada en 'TablaProbabilidad.yaml'.")

# Ejecutar el proceso de generación de la tabla de probabilidad
procesar_correos('CorreosClasificados_Usuario.yaml')
