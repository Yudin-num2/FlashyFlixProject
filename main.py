from moviepy.editor import *
import time
from pprint import pprint
import os
import telebot
from config import *
import yt_dlp

bot = telebot.TeleBot(TG_API_KEY, parse_mode='html')


# my_tg_id = 1567823651

@bot.message_handler(commands=['admin'])
def admin(message):
    bot.send_message(message.from_user.id, '<i>Hi, admin!</i>')


@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.from_user.id, 'Остановка бота выполнена ✅')
    bot.stop_bot()


@bot.message_handler(content_types=['video', 'gif'])
def get_video(message):
    file_name = time.strftime("%d_%m_%Y  %H_%M_%S") + '.mp4'
    file_info = bot.get_file(message.video.file_id)
    os.chdir(r"video/")
    with open(file_name, 'wb') as short:
        file = bot.download_file(file_info.file_path)
        short.write(file)


@bot.message_handler(commands=['address'])
def ls_la(message):
    files = []
    for _, _, file in os.walk(r'C:\Users\i.sysoev\PycharmProjects\FlashyFlixProject\video'):
        files.append(file)
    bot.send_message(message.from_user.id, str(files))


@bot.message_handler(commands=['watermark'])
def address_video_watermark(message):
    msg = bot.send_message(message.from_user.id, '<b>Отправь мне название файла для редактирования</b>')
    bot.register_next_step_handler(msg, watermark)


def watermark(message):
    os.chdir('video/')
    video_address = message.text
    video_without_watermark = VideoFileClip(video_address)
    logo = ImageClip(r'C:\Users\i.sysoev\PycharmProjects\FlashyFlixProject\Logo.png') \
        .set_duration(video_without_watermark.duration) \
        .resize(height=100) \
        .set_pos('top', 'center')
    bot.send_message(message.from_user.id, 'Выполняю...')
    video_with_watermark = CompositeVideoClip([video_without_watermark, logo])
    video_with_watermark.write_videofile(f'out_video_{video_address}')
    bot.send_video(message.from_user.id, video=open(f'out_video_{video_address}', 'rb'))
    bot.send_message(message.from_user.id, 'Выполнено ✅')


bot.infinity_polling()
