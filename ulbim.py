# -*- coding: utf-8 -*-
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from selenium import webdriver
from classification import *
import serial    #import serial module
import time
import datetime
import schedule
import numpy as np
import pandas as pd
import multiprocessing as mp
import re
import tempfile, os
import subprocess,sys

app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi('wyRN3rOak52yoFnGdgZUbmO8PEUCyTSHYccmn778+Wpxw8VjunniWdM+waq/1BxoASSZs5KzvBg5XuMsdjVWWQwEvg+PdMoIIuomc+CisAOwrbZ6y0tfoQ5u0GSUgHpSbNfnltTaBZYITpaJ6Kt2DwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('839b4f535143451a6adeccd885ac515b')
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')

def flex(Title,title,label1,text1,data1,label2):
    bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://i.imgur.com/aKCu3NS.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text=title, weight='bold', size='xl',align='center')

                        ]
            ),
            footer=BoxComponent(
                layout='horizontal',
                spacing='sm',
                contents=[
                    # callAction, separator, websiteAction
                    SpacerComponent(size='sm'),
                    # callAction
                    ButtonComponent(
                        style='primary',
                        height='sm',
                        color = '#0B74A5',
                        action=PostbackAction(label=label1, text=text1,data=data1),
                    ),
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='primary',
                        height='sm',
                        color = '#C23232',
                        action=URIAction(label=label2,uri='http://training.tabc.org.tw/bin/acctinfo.php'),
                    )
                ]
            ),
        )
    message = FlexSendMessage(alt_text= Title , contents=bubble)
    return message

def news(Title,title,label1,text1,data1,label2,text2,data2):
    bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://i.imgur.com/aKCu3NS.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text=title, weight='bold', size='xl',align='center')
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # callAction, separator, websiteAction
                    SpacerComponent(size='sm'),
                    # callAction
                    ButtonComponent(
                        style='primary',
                        height='sm',
                        color = '#624490',
                        action=PostbackAction(label=label1,text=text1,data=data1)
                    ),
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='primary',
                        height='sm',
                        color = '#624490',
                        action=PostbackAction(label=label2,text=text2,data=data2)
                    )
                ]
            ),
        )
    message = FlexSendMessage(alt_text=Title, contents=bubble)
    return message

def upload(Title,title,text,label1,data1,text1,label2,data2,text2,label3,data3,text3,label4,data4,text4,label5,data5,text5):
    bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://i.imgur.com/aKCu3NS.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text=title, weight='bold', size='xl',align='center')
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # callAction, separator, websiteAction
                    SpacerComponent(size='sm'),
                    # callAction
                    ButtonComponent(
                        style='primary',
                        height='sm',
                        color = '#624490',
                        action=PostbackAction(label=label1,text=text1,data=data1),
                    ),
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='primary',
                        height='sm',
                        color = '#624490',
                        action=PostbackAction(label=label2,text=text2,data=data2),
                    ),
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='primary',
                        height='sm',
                        color = '#624490',
                        action=PostbackAction(label=label3,text=text3,data=data3),
                    ),
                    SeparatorComponent(),
                    ButtonComponent(
                        style='primary',
                        height='sm',
                        color = '#624490',
                        action=PostbackAction(label=label4,text=text4,data=data4),
                    ),
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='primary',
                        height='sm',
                        color = '#624490',
                        action=PostbackAction(label=label5,text=text5,data=data5),
                    )
                ]
            ),
        )
    message = FlexSendMessage(alt_text=Title, contents=bubble)
    return message

@handler.add(PostbackEvent)
def handle_postback(event):
    postback = event.postback.data
    profile = line_bot_api.get_profile(event.source.user_id)
    if postback == '會員':
        line_bot_api.reply_message(event.reply_token, flex("會員專區",'會員專區','課程報到','報到','註冊會員',''))
    elif postback == '功能':
        line_bot_api.reply_message(event.reply_token, TextSendMessage('很抱歉，功能尚未開通'))
    elif postback == 'BIM':
        line_bot_api.reply_message(event.reply_token, upload('平台上架選單','平台上架選單','page1','送件須知','送件','送件須知','下載專區','下載','下載專區','電子合約','合約','電子合約','檔案上傳','上傳','檔案上傳','審核進度','審核','審核進度'))

@handler.add(MessageEvent, message=(ImageMessage, TextMessage))
def handle_message(event):
    msg = event.message.text
    if re.match(r"(D)", msg, re.DOTALL):#設計
        line_bot_api.reply_message(event.reply_token, sql(msg.replace('D', '')))
    elif re.match(r"(BD)", msg, re.DOTALL):#建商
        line_bot_api.reply_message(event.reply_token, sql(msg.replace('BD', '')))
    elif re.match(r"(C)", msg, re.DOTALL):#營造
        line_bot_api.reply_message(event.reply_token, sql(msg.replace('C', '')))
    elif re.match(r"(BM)", msg, re.DOTALL):#建材
        line_bot_api.reply_message(event.reply_token, sql(msg.replace('BM', '')))

@handler.add(MessageEvent, message=(ImageMessage, TextMessage,VideoMessage,AudioMessage,LocationMessage,StickerMessage))
def handle_message(event):
    df = pd.read_excel('label描述.xlsx',0)
#    df = df.to_json()
    l1 = df['種類']
    l2 = df['英文']
    l3 = df['名稱']
    if isinstance(event.message, ImageMessage):
        ext = 'jpg'
        # 讀取使用者上傳的圖片
        message_content = line_bot_api.get_message_content(event.message.id)
        with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix=ext + '-', delete=False) as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)
            tempfile_path = fd.name
        # 進行辨識
        result = main(tempfile_path)
        print(result)
        # 將result轉成中文
        for i in range(len(l2)):
            if result == l2[i]:
                name = str(l3[i])
                kind = str(l1[i])
                message1 = '這是家具類別' + kind + '中的' + name
                message2 = '以下是商品相關網頁：'
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message1+'\n'+message2))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='這張圖片不在我的辨識範圍中，請換一張試試！'))

@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

if __name__ == "__main__":
    app.run()
