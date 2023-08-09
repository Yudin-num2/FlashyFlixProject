
from moviepy.editor import *
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.rotate import rotate
from moviepy.audio.fx.volumex import volumex
from cv2 import VideoCapture
import cv2

address_video = '07_08_2023  11_20_01.mp4'


def size(address):
    print(os.getcwd())
    # os.chdir('video')
    vid = VideoCapture(address)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    return [height, width]


def watermark(address, height, width):

    os.chdir('video/')
    video_address = address
    video_without_watermark = VideoFileClip(video_address)
    video_without_watermark = video_without_watermark.fx(volumex, 2)\
                                                     # .fx(rotate(angle=angle(5))
    logo = ImageClip(r'C:\Users\i.sysoev\PycharmProjects\FlashyFlixProject\Logo.png') \
        .set_duration(video_without_watermark.duration) \
        .resize(height=100) \
        .set_pos('top', 'center')
    video_with_watermark = CompositeVideoClip([video_without_watermark, logo])
    video_with_watermark.write_videofile(f'out_video_{video_address}')


watermark(address_video, size(address_video)[0], size(address_video)[1])
