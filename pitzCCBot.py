import telepot
import time

from telepot.loop import MessageLoop

# le paso la id al bot
bot = telepot.Bot("427596794:AAH8zIm51YpmnYvbQx8qmfHUHXaqRuko7NI")


# funcion para manejar mensajes
def handle(msg):
    # id del chat
    chat_id = msg['chat']['id']
    usuario = msg['from']['username']

    # almacena mensaje
    mensaje = msg['text']

    # el 1 significa que solo separa una vez el string (en la primera aparicion de ' ')
    mensajeSeparado = mensaje.split(' ', 1)
    comando = mensajeSeparado[0]
    resto = ""

    # Comandos de 0 parámetros
    if len(mensajeSeparado) == 1:

        # Comando: Hola Mundo
        if comando.startswith('/hola'):
            bot.sendMessage(chat_id, "Hola Mundo!")


    elif len(mensajeSeparado) >= 2:

        # Comando: Echo <mensaje>
        if comando.startswith('/echo'):
            bot.sendMessage(chat_id, mensajeSeparado[1])


            # bot.sendMessage(chat_id, "send nudes")
            # bot.forwardMessage(chat_id, from_chat_id, message_id, disable_notification=None)
            # bot.sendPhoto(chat_id, photo, caption)


# espera mensajes
MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)




# http://telepot.readthedocs.io/en/latest/reference.html
