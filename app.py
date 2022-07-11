from random import random
from typing import Text
from flask import Flask, request, abort
import yaml
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, QuickReplyButton, QuickReply
from bs4 import BeautifulSoup
import requests
from HC_Lib.create_bubble import create_bubble
from HC_Lib.crawler import get_film_name_and_link
from HC_Lib.create_quick_reply import create_quick_reply

app = Flask(__name__)

with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)

token = config["line-bot"]["channel_access_token"]
secret = config["line-bot"]["channel_secret"]
line_bot_api = LineBotApi(token)
handler = WebhookHandler(secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]

    body = request.get_data(as_text=True)
    app.logger.info("Requet body: " + body)

    try:
        print(body, signature)
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):

    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":

        result_message = ''
        print(event.message.text)
        print(event.__dict__["source"].__dict__["user_id"])
        ####

        url = "https://movies.yahoo.com.tw/movie_intheaters.html?page=1"
        film_dict = get_film_name_and_link(url)
        ####

        ####
        result_message = "沒有這部電影資訊或已下檔，請輸入別的電影名稱"
        print(f"\n\nreply token is {event.reply_token}\n\n")
        if event.message.text == "找影城":
            result_message = "此功能開發中，目前無法使用"
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=result_message)
            )
        if event.message.text == "電影名稱":
            result_message = ''
            film_name = []
            for key in film_dict.keys():
                film_name.append(key)
                result_message += f"{key}\n"
            #
            quick_reply_items = create_quick_reply(film_name)
            message = TextSendMessage(text="以下是目前上映中的電影：",
                                      quick_reply=quick_reply_items
                                      )
            #
            line_bot_api.reply_message(
                event.reply_token,
                message
            )
            # line_bot_api.reply_message(
            #     event.reply_token,
            #     TextSendMessage(text=result_message)
            # )
        if event.message.text not in film_dict.keys():
            result_message = "查無此電影或該電影已下檔，請輸入其他電影名稱。"
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=result_message)
            )
        if event.message.text in film_dict.keys():
            film_info = film_dict[event.message.text]["url"]
            movie_time = film_dict[event.message.text]["movie_time"]
            img_url = film_dict[event.message.text]["img_url"]
            result_message = f"該影片的資訊為：{film_info},\n時刻表為{movie_time}"
            bubble_content = create_bubble(
                event.message.text, film_info, img_url, movie_time)

        result_message = result_message.strip()
        result_message = film_dict[event.message.text]["img_url"]
        # line_bot_api.reply_message(
        #     event.reply_token,
        #     TextSendMessage(text=result_message)
        # )
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage('img url', bubble_content)
        )


if __name__ == "__main__":
    app.run(debug=True, port=33507)
