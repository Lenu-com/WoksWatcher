from linebot.models import MessageEvent, TextMessage, TextSendMessage
from adapters.linebot.line_bot_api import line_bot_api
from adapters.linebot.webhook_handler import handler

@handler.add(MessageEvent, message=TextMessage)
def handle_message_command(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )
