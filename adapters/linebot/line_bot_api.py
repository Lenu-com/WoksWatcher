import json
from linebot import LineBotApi

TOKEN_FILE = 'config/token.json'
CHANNEL_ACCESS_TOKEN = json.load(open(TOKEN_FILE, 'r'))['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
