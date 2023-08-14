from moviepy.editor import *
from moviepy.video.fx.colorx import colorx
from moviepy.audio.fx.volumex import volumex
import time
from pprint import pprint
import os
import telebot
from config import *

bot = telebot.TeleBot(TG_API_KEY, parse_mode='html')


# my_tg_id = 1567823651

@bot.message_handler(commands=['admin'])
def admin(message):
    try:
        bot.send_message(message.from_user.id, '<i>Hi, admin!</i>')
        text = """<b>Commands:</b>
        /admin - commands
        /stop - stop bot
        /ls - ls la
        /watermark - watermark
        /volume - volume x2
        /del - delete file
        /getfile - bot send file"""
        bot.send_message(message.from_user.id, text)
    except Exception as e:
        bot.send_message(message.from_user.id, str(e))


@bot.message_handler(commands=['stop'])
def stop(message):
    try:
        bot.send_message(message.from_user.id, 'Остановка бота выполнена ✅')
        bot.stop_bot()
    except Exception as e:
        bot.send_message(message.from_user.id, str(e))


@bot.message_handler(content_types=['video', 'gif'])
def get_video(message):
    try:
        file_name = time.strftime("%d_%m_%Y  %H_%M_%S") + '.mp4'
        file_info = bot.get_file(message.video.file_id)
        os.chdir(r"video/")
        with open(file_name, 'wb') as short:
            file = bot.download_file(file_info.file_path)
            short.write(file)
        bot.send_message(message.from_user.id, 'Сохранил видео ✅')
    except Exception as e:
        bot.send_message(message.from_user.id, str(e))


@bot.message_handler(commands=['ls'])
def ls_la(message):
    try:
        for _, _, files in os.walk(r'C:\Users\i.sysoev\PycharmProjects\FlashyFlixProject\video'):
            for file in files:
                bot.send_message(message.from_user.id, file)

    except Exception as e:
        bot.send_message(message.from_user.id, str(e))


@bot.message_handler(commands=['watermark'])
def address_video_watermark(message):
    try:
        ls_la(message)
        msg = bot.send_message(message.from_user.id, '<b>Отправь мне название файла для редактирования</b>')
        bot.register_next_step_handler(msg, watermark)
    except Exception as e:
        bot.send_message(message.from_user.id, str(e))


def watermark(message):
    try:
        video_address = os.path.join('video/', message.text)
        video_without_watermark = VideoFileClip(video_address)
        logo = ImageClip(r'C:\Users\i.sysoev\PycharmProjects\FlashyFlixProject\Logo.png') \
            .set_duration(video_without_watermark.duration) \
            .resize(height=200) \
            .set_pos('top', 'center')
        bot.send_message(message.from_user.id, 'Выполняю...')
        video_with_watermark = CompositeVideoClip([video_without_watermark, logo])
        video_with_watermark.write_videofile(f'video/watermark_{message.text}')
        bot.send_video(message.from_user.id, video=open(f'video/watermark_{message.text}', 'rb'))
        bot.send_message(message.from_user.id, 'Выполнено ✅')
    except Exception as e:
        bot.send_message(message.from_user.id, str(e))


@bot.message_handler(commands=['volume'])
def volume_choise(message):
    try:
        ls_la(message)
        bot.send_message(message.from_user.id, 'Выбери видео из списка')
        bot.register_next_step_handler(message, volume)
    except Exception as e:
        bot.send_message(message.from_user.id, str(e))


def volume(message):
    try:
        bot.send_message(message.from_user.id, 'Выполняю...')
        # print(os.getcwd())
        file_address = os.path.join('video/', f'{message.text}')
        # print(file_address)
        video = VideoFileClip(file_address)
        new_video = video.fx(volumex, 1.5)
        new_video.write_videofile(f'volumex_{message.text}')
        bot.send_video(message.from_user.id, video=open(f'volumex_{message.text}', 'rb'))
        bot.send_message(message.from_user.id, 'Выполнено ✅')
    except Exception as e:
        bot.send_message(message.from_user.id, str(e))


@bot.message_handler(commands=['del'])
def delete(message):
    try:
        ls_la(message)
        bot.send_message(message.from_user.id, 'Выбери видео из списка')
        bot.register_next_step_handler(message, delete2)
    except Exception as e:
        bot.send_message(message.from_user.id, str(e))


def delete2(message):
    try:
        bot.send_message(message.from_user.id, 'Выполняю...')
        name_file = message.text
        os.chdir('video/')
        os.remove(name_file)
        bot.send_message(message.from_user.id, 'Файл удалён ✅')
    except Exception as e:
        bot.send_message(message.from_user.id, str(e))


@bot.message_handler(commands=['getfile'])
def send_file(message):
    try:
        ls_la(message)
        bot.send_message(message.from_user.id, 'Выбери видео из списка')
        bot.register_next_step_handler(message, send_file2)
    except Exception as e:
        bot.send_message(message.from_user.id, str(e))


def send_file2(message):
    try:
        bot.send_message(message.from_user.id, 'Выполняю...')
        file_name = message.text
        bot.send_video(message.from_user.id, video=open(file_name, 'rb'))
        bot.send_message(message.from_user.id, 'Выполнено ✅')
    except Exception as e:
        bot.send_message(message.from_user.id, str(e))


@bot.message_handler(commands=['mute'])
def mute_choise(message):
    try:
        ls_la(message)
        bot.send_message(message.from_user.id, 'Выбери видео из списка')
        bot.register_next_step_handler(message, mute)
    except Exception as e:
        bot.send_message(message.from_user.id, str(e))


def mute(message):
    try:
        bot.send_message(message.from_user.id, 'Выполняю...')
        file_address = f'video/{message.text}'
        video = VideoFileClip(file_address)
        video.without_audio().write_videofile(f'video/{message.text}_mute.mp4')
        bot.send_message(message.from_user.id, 'Выполнено ✅')
    except Exception as e:
        bot.send_message(message.from_user.id, str(e))


bot.infinity_polling()
