
from moviepy.editor import *
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.audio.fx.volumex import volumex

address_video = '07-08-2023-11-20-01_kWeEsLA7.mp4'


def watermark(address):

    os.chdir('video/')
    video_address = address
    video_without_watermark = VideoFileClip(video_address)
    video_without_watermark = colorx(video_without_watermark, 1.3)
    video_without_watermark = crop(video_without_watermark, y2=-40)
    logo = ImageClip(r'C:\Users\i.sysoev\PycharmProjects\FlashyFlixProject\Logo.png') \
        .set_duration(video_without_watermark.duration) \
        .resize(height=100) \
        .set_pos('top', 'center')
    video_with_watermark = CompositeVideoClip([video_without_watermark, logo])
    video_with_watermark.write_videofile(f'out_video_{video_address}')


watermark(address_video)
