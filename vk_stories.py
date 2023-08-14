from config import VK_API_KEY

import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

authorize = vk_api.VkApi(token=VK_API_KEY)
longpoll = VkLongPoll(authorize)

image = r'C:\Users\i.sysoev\PycharmProjects\FlashyFlixProject\Logo.png'

upload = VkUpload(authorize)
upload_image = upload.photo_group_widget(photo=image, image_type='510x128')
print(upload_image)
attachments = 'photo{}_{}'.format(upload_image['owner_id'], upload_image['id'])

href = attachments


# Функция отправки на стену
# def send_content(href):
#     first_post = authorize.method('photos.getWallUploadServer', {'group_id': 'flashyflix'})
#     # second_post = authorize.method('')
#
#     # authorize.method('wall.post', {'group_id': 'flashyflix',
#     #                                'message': 'Hello, World!',
#     #                                'attachments': href
#     #                                }
#     #                  )
#     print(first_post)
#
# if __name__ == '__main__':
#     send_content(href)
