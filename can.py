import requests
from bs4 import BeautifulSoup
r = requests.get('https://kafeterya.metu.edu.tr/')
soup = BeautifulSoup(r.content, "html.parser")
urunler = soup.find_all("div", attrs={"class":"yemek"})
spisok = []

for elem in urunler:
    spisok.append(elem('img')[0]['alt'])

ogle = ('Öğle Yemeğiniz : ', spisok[0:4])
aksam = ('Akşam Yemeğiniz : ', spisok[4:8])

"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'API TOKEN YAPIŞTIRIN'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['yemek'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(ogle)
    await message.reply(aksam)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
