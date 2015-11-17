import telebot
 
TOKEN = '128261054:AAF8D_ha-ySdbgepBWg-4RxU7GpsrPBltY4' #Ponemos nuestro TOKEN generado con el @BotFather
bot = telebot.TeleBot(TOKEN) #Creamos nuestra instancia "mi_bot" a partir de ese TOKEN


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
cid = message.chat.id # Guardamos el ID de la conversacion para poder responder.


bot.send_message(cid, text) # Ejemplo tb.send_message('123456789', 'Hola mundo!')
