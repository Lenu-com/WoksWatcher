from fastapi import FastAPI, Request
from core.application.command_handlers import handle_message_command
from adapters.linebot.webhook_handler import handler

app = FastAPI()

@app.post("/callback")
async def callback(request: Request):
    signature = request.headers.get('X-Line-Signature')
    body = await request.body()
    return await handler(body, signature)
