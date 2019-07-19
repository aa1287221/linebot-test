from flask import Flask, request, abort
from imgurpython import ImgurClient

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import tempfile, os
import time


# imgur key
client_id = 'def8f01cf7bbc84'
client_secret = 'a421c16db93b83c57a936afc64aacd87c1054bb7'
album_id = 'oVsMCXH'
access_token = 'b58ab530e9da88e2d73d0c970b5ebc5cb17ceaef'
refresh_token = 'b575094501f457393c7f0c12edb2d1344264d786'


def handle_message():
    os.popen('fswebcam -r 640x480 --jpeg 85 -D 1 plant-picture.jpg')
    time.sleep(5)
    path = "/home/pi/line_bot/plant-picture.jpg"
    try:
        client = ImgurClient(client_id, client_secret, access_token, refresh_token)
        config = {
            'album': album_id,
            'name': 'Catastrophe!',
            'title': 'Catastrophe!',
            'description': 'Cute kitten being cute on '
        }
        client.upload_from_path(path, config=config, anon=False)
        images = client.get_album_images(album_id)
        index = len(images) - 1
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
    except:
        countinue
    return url
    

