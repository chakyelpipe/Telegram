# Telegram
git clone https://github.com/eternnoir/pyTelegramBotAPI.git  
cd pyTelegramBotAPI  
sudo python setup.py install
import telebot

TOKEN = '<116995232:AAH_d0bI7AZeoUZZKLa39eNEeyt7Ct_dJcs>' #Ponemos nuestro TOKEN generado con el @BotFather

mi_bot = telebot.TeleBot(TOKEN) #Creamos nuestra instancia "mi_bot" a partir de ese TOKEN  

TOKEN = '<116995232:AAH_d0bI7AZeoUZZKLa39eNEeyt7Ct_dJcs
>' #Ponemos nuestro TOKEN generado con el @BotFather  
mi_bot = ChakyElPipe(116995232:AAH_d0bI7AZeoUZZKLa39eNEeyt7Ct_dJcs
)                         #Creamos nuestra instancia "ChakyElPipebot" a partir de ese TOKEN

def listener(*mensajes):  ##Cuando llega un mensaje se ejecuta esta función  
    for m in mensajes:
        chat_id = m.chat.id
        if m.content_type == 'text':
            text = m.text
            mi_bot.send_message(chat_id,"Me copio de tu texto")
            mi_bot.send_message(chat_id, text)

mi_bot.set_update_listener(listener) #registrar la funcion listener  
mi_bot.polling()

while True: #No terminamos nuestro programa  
    pass
