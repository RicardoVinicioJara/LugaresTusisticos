import json
import requests
from ibm_watson import AssistantV2, LanguageTranslatorV3, TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator('U4IKxuhQ4XBIrskFYSLLqrB29b_A2fch9uL4gWQUZ-f4')
assistant = AssistantV2(
    version='2018-09-20',
    authenticator=authenticator)
assistant.set_service_url(
    'https://api.us-south.assistant.watson.cloud.ibm.com/instances/20d0e70b-3f11-4c02-9137-205d38b948a9')
assistant.set_disable_ssl_verification(False)
session = assistant.create_session("633359aa-4a7e-4cfa-8ebe-78113a86ad21").get_result()

authenticatorT = IAMAuthenticator('0Iobj63HD2qz6ChKXOCkc1kARMJ8E9-Gkq1045FQIGf7')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticatorT)
language_translator.set_service_url('https://gateway.watsonplatform.net/language-translator/api')

def mensaje(text, session):
    message = assistant.message("633359aa-4a7e-4cfa-8ebe-78113a86ad21",
                                session["session_id"],
                                input={'message_type': 'text', 'text': text}).get_result()
    return (message['output']['generic'][0]['text'])


def traducir(text, language_translator):
    translation = language_translator.translate(
        text=text, model_id='en-es').get_result()
    return translation['translations'][0]['translation']





# Variables para el Token y la URL del chatbot
TOKEN = "1152444193:AAFPVyFp353Lc_3g7LJfwt35Y_-YcfJ8Cvk"  # Cambialo por tu token
URL = "https://api.telegram.org/bot" + TOKEN + "/"


def update(offset):
    # Llamar al metodo getUpdates del bot, utilizando un offset
    respuesta = requests.get(URL + "getUpdates" + "?offset=" + str(offset) + "&timeout=" + str(100))

    # Decodificar la respuesta recibida a formato UTF8
    mensajes_js = respuesta.content.decode("utf8")

    # Convertir el string de JSON a un diccionario de Python
    mensajes_diccionario = json.loads(mensajes_js)

    # Devolver este diccionario
    return mensajes_diccionario


def info_mensaje(mensaje):
    # Comprobar el tipo de mensaje
    if "text" in mensaje["message"]:
        tipo = "texto"
    elif "sticker" in mensaje["message"]:
        tipo = "sticker"
    elif "animation" in mensaje["message"]:
        tipo = "animacion"  # Nota: los GIF cuentan como animaciones
    elif "photo" in mensaje["message"]:
        tipo = "foto"
    elif "voice" in mensaje["message"]:
        tipo = "audio"
    else:
        # Para no hacer mas largo este ejemplo, el resto de tipos entran
        # en la categoria "otro"
        tipo = "otro"

    # Recoger la info del mensaje (remitente, id del chat e id del mensaje)
    persona = mensaje["message"]["from"]["first_name"]
    id_chat = mensaje["message"]["chat"]["id"]
    id_update = mensaje["update_id"]

    # Devolver toda la informacion
    return tipo, id_chat, persona, id_update


def leer_mensaje(mensaje):
    # Extraer el texto, nombre de la persona e id del último mensaje recibido
    texto = mensaje["message"]["text"]

    # Devolver las dos id, el nombre y el texto del mensaje
    return texto

def leer_audio(mensaje):
    print(mensaje)
    print(mensaje['message']['voice'])


def enviar_mensaje(idchat, texto):
    # Llamar el metodo sendMessage del bot, passando el texto y la id del chat
    requests.get(URL + "sendMessage?text=" + texto + "&chat_id=" + str(idchat))

def enviar_vox(idchat, texto):
    # Llamar el metodo sendMessage del bot, passando el texto y la id del chat
    data = {'idchat': '72600457', 'voice': 'AwADBAADPAYAAvFWCVFZFfPyZdGLfhYE'}
    requests.get(URL + "/sendVoice",  params=data)
    print(requests.json())

# Variable para almacenar la ID del ultimo mensaje procesado
ultima_id = 0

while (True):
    mensajes_diccionario = update(ultima_id)
    for i in mensajes_diccionario["result"]:
        tipo, idchat, nombre, id_update = info_mensaje(i)
        if tipo == "texto":
            texto = leer_mensaje(i)
            tradiccion = traducir(texto, language_translator)
            print(tradiccion)
            texto_respuesta = mensaje(tradiccion,session)
        elif tipo == "sticker":
            texto_respuesta = "Bonito sticker!"
        elif tipo == "animacion":
            texto_respuesta = "Me gusta este GIF!"
        elif tipo == "foto":
            texto_respuesta = "Bonita foto!"
        elif tipo == "audio":
            texto_respuesta = "Vamos a ve si podemos sacar el audio"
            leer_audio(i)
        elif tipo == "otro":
            texto_respuesta = "Es otro tipo de mensaje"

        if id_update > (ultima_id - 1):
            ultima_id = id_update + 1
        print(texto_respuesta)
        enviar_mensaje(idchat, texto_respuesta)

    # Vaciar el diccionario
    mensajes_diccionario = []
#half of the world