from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def keyboard_for_admin():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.row(InlineKeyboardButton(text="ha", callback_data="ha"), InlineKeyboardButton(text="yo'q", callback_data="yoq"))
    return keyboard

def ask_for_images_to_send_to_channel():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.row(InlineKeyboardButton(text="ha", callback_data="haa"), InlineKeyboardButton(text="yo'q", callback_data="yoqq"))
    return keyboard