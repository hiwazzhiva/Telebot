import os
import random
import uuid
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from aiogram.utils import executor

API_TOKEN = os.getenv("BOT_TOKEN")  # Telegram bot token from environment

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

predictions = [
    "You will be dismissed",
    "It was a tough day, you deserve a coffee!",
    "Go chal you lazy bish",
    "A surprise awaits you (probation)",
    "It's never late to change your major...or uni",
    "Shower today. SHOWER TODAY!",
    "You are gay",
    "Food might be poisoned",
    "You may receive a love letter from someone",
    "I hope this email finds you depressed...",
    "50/50 chance of meeting Shigeo",
"You will get F from one of the courses",
"You will get A on your next assignment",
"Don't miss tomorrow's 9 am lecture!",
"That coffee from Daily was not worth it",
"Corner cashier will smile to you today",
"Magnum cash register will break on your turn",
"Be ready for pop up quiz" 


]

@dp.inline_handler()
async def send_prediction(inline_query: types.InlineQuery):
    result_text = random.choice(predictions)
    input_content = InputTextMessageContent(result_text)
    item = InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        title="Get your prediction ✨",
        input_message_content=input_content
    )
    await inline_query.answer([item], cache_time=1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
