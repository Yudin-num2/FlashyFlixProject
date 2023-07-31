import telebot
from config import *

bot = telebot.TeleBot(TG_API_KEY, parse_mode='html')


@bot.message_handler(commands=['admin'])
def admin(message):
    bot.send_message(message.from_user.id, '<i>Hi, admin!</i>')


bot.infinity_polling()
