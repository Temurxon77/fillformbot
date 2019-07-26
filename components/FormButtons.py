import telebot
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton,KeyboardButton
from telebot import types

send_str = ["отправить","yuborish","send"]
lang_switch = ["изменть язык","tilni o'zgartirish","change language"]
refill_form = ["заполнить заново","yangidan to\'ldirish","re-fill form"]

def Buttons(lang):
    try:
        reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
        if lang["RU"]:
            reply_markup.row(types.KeyboardButton(send_str[0]))
            reply_markup.row(types.KeyboardButton(refill_form[0]))
            reply_markup.row(types.KeyboardButton(lang_switch[0]))
        elif lang["UZ"]:
            reply_markup.row(types.KeyboardButton(send_str[1]))
            reply_markup.row(types.KeyboardButton(refill_form[1]))
            reply_markup.row(types.KeyboardButton(lang_switch[1]))
        elif lang["EN"]:
            reply_markup.row(types.KeyboardButton(send_str[2]))
            reply_markup.row(types.KeyboardButton(refill_form[2]))
            reply_markup.row(types.KeyboardButton(lang_switch[2]))
    except Exception as e:
        print(e)
        reply_markup.row(types.KeyboardButton("Restart!"))
        lang["Error_catch"] = True
    finally:
        return reply_markup