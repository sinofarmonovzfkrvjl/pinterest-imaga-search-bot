from telebot import TeleBot, types
import logging
from tools import get_random_pinterest_image_url, Pinterest
import os
import shutil
from keyboards import keyboard_for_admin
from time import sleep

API_TOKEN = "7596605488:AAFTbpv3_67TleOw8bm5JzSLqZCC0r9F4bY"

bot = TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.send_message(message.chat.id, f"Salom {message.from_user.full_name}")

@bot.message_handler(commands=['photos'])
def send_text(message: types.Message):
    bot.send_message(message.chat.id, "rasmlar yuklanmoqda...")
    images = [get_random_pinterest_image_url() for _ in range(9)]
    media = [types.InputMediaPhoto(photo) for photo in images]
    bot.send_media_group(message.chat.id, media)

@bot.message_handler(func=lambda message: True)
def message_true(message: types.Message):
    global opened_data
    p = Pinterest()
    data = message.text.split(" ")
    opened_data = " ".join(data)
    bot.send_message(message.chat.id, "rasmlar yuklamoqda...")
    try:
        images_url = p.search(data[0], int(data[-1] if data[-1].isdigit() else 10))
        p.download(url_list=images_url, number_of_workers=1, output_folder=opened_data)
    except Exception as e:
        print(e)
    images = os.listdir(opened_data)
    if message.from_user.id == 7077167971:
        for image in images:
            with open(f"{opened_data}/{image}", "rb") as photo:
                bot.send_photo(7077167971, photo.read())
                sleep(0.5)
        bot.send_message(7077167971, "bu rasmlar kanalgan tashlansinmi", reply_markup=keyboard_for_admin())
    else:
        for image in images:
            with open(f"{opened_data}/{image}", "rb") as photo:
                bot.send_photo(message.chat.id, photo.read())

@bot.callback_query_handler(func=lambda call: True)
def callback(call: types.CallbackQuery):
    if call.data == "ha":
        images = os.listdir(opened_data)
        for image in images:
            with open(f"{opened_data}/{image}", "rb") as photo:
                bot.send_photo(-1002181889394, photo.read())
                sleep(1)
    elif call.data == "yoq":
        bot.send_message(call.message.chat.id, "bekor qilindi")
    shutil.rmtree(opened_data)

print(f"[@{bot.get_me().username}] is started")
bot.infinity_polling(skip_pending=True, logger_level=logging.INFO)