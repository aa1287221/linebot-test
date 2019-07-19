from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction
)
import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


def flower():
    r = requests.get('https://www.2ustyle.com/tutorial')
    soup = BeautifulSoup(r.text, 'html.parser')
    stories = soup.select('ul.sub-menu a')
    content=""
    for s in stories:
        title = s.text
        link = s.get('href')
        content+='{}\n{}\n'.format(title,link)
    return content
