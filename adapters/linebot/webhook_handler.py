import json
from linebot import WebhookHandler

TOKEN_FILE = 'config/token.json'
CHANNEL_SECRET = json.load(open(TOKEN_FILE, 'r'))['CHANNEL_SECRET']
handler = WebhookHandler(CHANNEL_SECRET)