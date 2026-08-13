import json
import os
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

BOT_TOKEN = os.getenv("8225223905:AAEc_OzKG2ecjHjnAXgVJZSOme5ss3hbZLM", "")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Echo: {message.text}")

async def handler(event, context):
    if event.get("httpMethod") != "POST":
        return {"statusCode": 405, "body": "Method Not Allowed"}
    
    try:
        body = json.loads(event.get("body", "{}"))
        update = types.Update(**body)
        await dp.feed_update(bot=bot, update=update)
    except Exception as e:
        print(f"Error handling update: {e}")
        return {"statusCode": 500, "body": str(e)}

    return {"statusCode": 200, "body": "OK"}
