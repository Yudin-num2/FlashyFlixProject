import os
from moviepy.editor import *
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.audio.fx.volumex import volumex

address_video = 'out_video_aaa.mp4'


def watermark(address):

    os.chdir('video/')
    video_address = address
    video_without_watermark = VideoFileClip(video_address)
    video_without_watermark = colorx(video_without_watermark, 1.3)
    # video_without_watermark = crop(video_without_watermark, y2=-40)
    logo = ImageClip(r'C:\Users\i.sysoev\PycharmProjects\FlashyFlixProject\Logo.png') \
        .set_duration(video_without_watermark.duration) \
        .resize(height=100) \
        .set_pos('top', 'center')
    video_with_watermark = CompositeVideoClip([video_without_watermark, logo])
    video_with_watermark.write_videofile(f'watermark_aaa.mp4')


watermark(address_video)


def audio(address):
    file_address = address
    video = VideoFileClip(file_address)
    new_video = video.fx(volumex, 1.5)
    name = file_address.split('/')[-1]
    new_video.write_videofile(f'{name}_volumex.mp4')


# audio(r'C:\Users\i.sysoev\PycharmProjects\FlashyFlixProject\video\Summer.mp4')


def mute(name_of_file):
    file_address = f'video/{name_of_file}'
    video = VideoFileClip(file_address)
    video.without_audio().write_videofile(f'{name_of_file}_mute.mp4')


# mute('ASMR.mp4')


def add_music():
    video = VideoFileClip(os.path.join('video', 'ASMR.mp4_mute.mp4'))
    audio = AudioFileClip('Audio/1.mp3').set_duration(video.duration)
    video.set_audio(audio).write_videofile('ASMR.mp4')


# add_music()

def sub():
    video = VideoFileClip(r'video\Summer.mp4')
    new_video = video.subclip(830, 14420)
    new_video.write_videofile(f'subclip_Summer.mp4')


# sub()


