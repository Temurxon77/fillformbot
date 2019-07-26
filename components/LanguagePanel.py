import telebot
from telebot.types import InlineKeyboardButton,KeyboardButton,ReplyKeyboardMarkup
from telebot import types

def Language():
    try:
        reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        reply_markup.row(types.KeyboardButton("🇺🇿 UZ"),types.KeyboardButton("🇷🇺 RU"))
        reply_markup.row(types.KeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿 EN"))
    except Exception as e:
        print(e)
        reply_markup.row(types.KeyboardButton("Restart!"))
    finally:
        return reply_markup
