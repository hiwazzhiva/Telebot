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
    "Чопрайс",
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
"Be ready for pop up quiz",
"Your clothes will get dirty in the laundry",
"You will be dismissed for missing that one session in orientation week.",
"Your extra place from will be rejected",
"Bursars will forget your stipend",
"You'll end up in a group project with a bunch of vip kazakhs",
"You will lose your pen in auditory",
"Someone will share their lecture notes with you to help",
"When you will leave the campus next time, it will rain awfully",
"It’s turned out that your ID was once exposed in Lost&Found chat and now everyone laughs at your GPA",
"You will take the same course section with your ex",
"You will accidentally step on poop of the horse that is in our campus",
"Prof will curve your grade down",
"Block manager is right behind you",
"You just won a prize! lifetime ban from eating in corner",
"Registrar will send you an email that starting from today you will pay 100000 tenge for every retake",
"This bot claims you an eligible member of NU Femboy club",
"Professor will curve 5%",
"Your grade for the assignment will be out today",
"You will forget NU ID card today at your room",
"90% chance of meeting Waqar Ahmad",
"No darling, you’re doing everything just fine. Quit the overthinking, step outside, touch some grass, and give yourself a little break",
"You will end up reading all unread tumba posts",
"Your roommate secretly hates you",
"Military is looking after you today. Hide",
"3 people are going to annoy you",
"Text your crush. No seriously GO TEXT YOUR CRUSH",
"This semester will be the best",
"There is a cockroach in your room",
"Go play boardgames! It will be fun",
"It's time to pull an allnighter",
"Today's attendance was mandatory",
"You are the best teammate ever",
"Professor is proud of you",
"Today the water will be cut off",
"Go make some friends",
"Time to get bitches",
"No one will go eating in canteens with you this week",
"You will need service desk soon",
"Do you really need this club?",
"It's never late to steal a founder",
"Here’s a lucky Corner doner 🌯, you will have a nice week",
"Hey, dungeon master, your gym bro misses you",
"Visit psychologis ASAP",
"Your calculator will break during the quiz",
"Professor will ask you a question. Be prepared",
"Dear student! The bot is currently out of service. Try again later",
"Eat some fruits and go for a walk. Your health is more important than your grades",
"Dorm prices will rise next year, start saving now",
"You will be relocated to D6 block next semester",
"No one will answer your next VA question",
"Time to shine! Wear your best outfit today",
"Elevator will close in front of you",
"There’s no free places in block’s atriums today, find another place",
"Oh no, misconduct is approaching",
"You will pass everything",
"How is your capstone? Finish it before it's too late",
"Maybe it’s enough doomscrolling for today",
"Someone is going to invite you to Astana Ball",
"Try searching for a j*b",
"Overprice coffee and macbook will not get you an A",
"You are also someone's crush",
"Dance all night long and party hard",
"Read your courses’ syllabi already",
"You won't need this degree in your life",
"Lots of couples kissing in the Atrium. But not you, haha",
"Make a call, talk to your parents",
"You better pay attention to your wisdom teeth",
"10 hour screen time is bad for your health",
"You will not find that one article neither in SciHub nor in library website",
"Don’t forget flushing after yourself in public toilets",
"Avoid going to the 3rd block, 2nd floor extension, men’s toilet today",
"Block manager will check your room for illegal roommates",
"You will miss your bus and catch a taxi and it's going to be extremely expensive"
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
