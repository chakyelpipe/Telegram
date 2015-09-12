# Telegram
git clone https://github.com/eternnoir/pyTelegramBotAPI.git  
cd pyTelegramBotAPI  
sudo python setup.py install
import telebot

TOKEN = '<116995232:AAH_d0bI7AZeoUZZKLa39eNEeyt7Ct_dJcs>' #Ponemos nuestro TOKEN generado con el @BotFather

mi_bot = telebot.TeleBot(TOKEN) #Creamos nuestra instancia "mi_bot" a partir de ese TOKEN  
