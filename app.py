from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('2UdbmwTaqMYWDCEn9IdNxW5RS8XEOy5yPe/Cw6VjmvE5e4lpOvOcqZW8AUU3AZHtuulTErsrV4Vs0LtKciBrQkf10kUtvrS1gMnQ59xj9qzs2QfbPu66n5WeskxEQndo2MAtZ0wtd1hcgi/nVMW4KAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('21eb5304abf241b815dc6c81130b98d0')


@app.route("/callback", methods=['POST'])
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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    sticker_message = StickerSendMessage(
        package_id='1',
        sticker_id='1'
    )

    line_bot_api.reply_message(
        event.reply_token,
        # TextSendMessage(text=event.message.text))
        sticker_message)

if __name__ == "__main__":
    app.run()