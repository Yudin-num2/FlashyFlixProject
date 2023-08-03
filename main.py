import datetime
import time
from pprint import pprint

import telebot
from config import *


bot = telebot.TeleBot(TG_API_KEY, parse_mode='html')


@bot.message_handler(commands=['admin'])
def admin(message):
    bot.send_message(message.from_user.id, '<i>Hi, admin!</i>')


@bot.message_handler(content_types=['video', 'gif'])
def get_video(message):
    file_name = time.strftime("%d_%m_%Y  %H_%M_%S")
    file_info = bot.get_file(message.video.file_id)
    with open(file_name, 'wb') as short:
        file = bot.download_file(file_info.file_path)
        short.write(file)
    pprint(message.json)


bot.infinity_polling()
