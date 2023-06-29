import openai

# Configuración de OpenAI API
openai.api_key = 'tu_api_key_de_OpenAI'  # Reemplaza con tu propia clave de API

# Función para obtener la respuesta del modelo de lenguaje
def obtener_respuesta(texto_entrada):
    respuesta = openai.Completion.create(
        engine='text-davinci-003',  # Reemplaza con el motor de lenguaje adecuado
        prompt=texto_entrada,
        max_tokens=50,  # Reemplaza con la longitud de respuesta deseada
        temperature=0.7,  # Reemplaza con el nivel de creatividad/determinismo deseado
        n = 1,  # Reemplaza con el número de respuestas deseadas
        stop=None,  # Reemplaza con una lista de palabras para detener la respuesta si es necesario
    )
    return respuesta.choices[0].text.strip()

# Función principal para la interacción del chatbot
def chatbot_bad_bunny():
    print("¡Hola! Soy Bad Bunny. Pregúntame lo que quieras o escribe 'salir' para terminar.")

    while True:
        entrada_usuario = input("Tú: ")

        if entrada_usuario.lower() == "salir":
            print("Bad Bunny: ¡Hasta luego! Nos vemos pronto.")
            break

        # Generar respuesta utilizando el modelo de lenguaje
        respuesta_modelo = obtener_respuesta(entrada_usuario)

        print("Bad Bunny:", respuesta_modelo)

# Ejecutar el chatbot
chatbot_bad_bunny()