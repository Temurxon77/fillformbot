import telebot
from config import Token
from telebot import types
from telebot import types
from telebot.types import ReplyKeyboardRemove
from components.LanguagePanel import Language
from components.FormButtons import Buttons
import re

from telebot.types import KeyboardButton,InlineKeyboardButton,ReplyKeyboardMarkup

bot = telebot.TeleBot(Token.TOKEN)

form_dict = {"name":"","surname":"","phone":0,"email":"","tg_name":"","zipCode":0,"bank_accountNum":0}
language_type = {"UZ":False,"RU":False,"EN":False,"isSend":False,"Counter":0,"Error_catch":False}


@bot.message_handler(commands=['start'])
def Starter(message):
    bot.disable_save_next_step_handlers()
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id,"Tilni tanlang | Выберите язык | Choose language",reply_markup=Language())
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id,"ooops")

@bot.message_handler(func=lambda mess: mess.text == "🇺🇿 UZ" or mess.text == "🇷🇺 RU" or mess.text == "🏴󠁧󠁢󠁥󠁮󠁧󠁿 EN")
def Register(message):
    bot.disable_save_next_step_handlers()
    try:
        form_dict["tg_name"] = message.chat.username
        #print(form_dict["tg_name"])
        if message.text == "🇺🇿 UZ":
            language_type["UZ"] = True
            msg = bot.reply_to(message,"Ismingizni kiriting")
            bot.register_next_step_handler(msg,AskName)
        elif message.text == "🇷🇺 RU":
            language_type["RU"] = True
            msg = bot.reply_to(message,"Введите ваше имя")
            bot.register_next_step_handler(msg,AskName)
        elif message.text == "🏴󠁧󠁢󠁥󠁮󠁧󠁿 EN":
            language_type["EN"] = True 
            msg = bot.reply_to(message,"Enter your name")
            bot.register_next_step_handler(msg,AskName)
        else:
            bot.send_message(message.chat.id,"Please choose language...")
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id,"ooops")

# @bot.message_handler(commands=['/fillform'])
# def Refill(message):
#     try:
#         chat_id = message.chat.id
#         if language_type["UZ"]:
#             msg = bot.send_message(chat_id,"Ismingizni kiriting")
#             bot.register_next_step_handler(msg,AskName)
#         elif language_type["RU"]:
#             msg = bot.send_message(chat_id,"Введите ваше имя")
#             bot.register_next_step_handler(msg,AskName)
#         elif language_type["EN"]:
#             msg = bot.send_message(chat_id,"Enter your name")
#             bot.register_next_step_handler(msg,AskName)
#     except Exception as e:
#         print(e)
#         bot.send_message(message.chat.id,"ooops")

def AskName(message):
    bot.disable_save_next_step_handlers()
    chat_id = message.chat.id
    try:
        regex_name = re.search("[a-zа-яёғҳзўқ]{3,}",message.text)
        if not regex_name:
            if language_type["UZ"]:
                bot.send_message(chat_id,"Isminigz noto\'g\'ri kiritildi... boshqattan kiring")
            elif language_type["RU"]:
                bot.send_message(chat_id,"Имя введено некорректно... введите заново")
            elif language_type["EN"]:
                bot.send_message(chat_id,"Invalid name entered... Try again")
            bot.register_next_step_handler(message,AskName)
        else:
            form_dict["name"] = message.text
            if language_type["UZ"]:
                bot.send_message(chat_id,"Familiyangizni kiriting:")
            elif language_type["RU"]:
                bot.send_message(chat_id,"Введите вашу фамилию")
            elif language_type["EN"]:
                bot.send_message(chat_id,"Enter your surname")
            bot.register_next_step_handler(message, AskPhone)
    except Exception as e:
        print(e)
        bot.send_message(chat_id,"ooops")
        
def AskPhone(message):
    bot.disable_save_next_step_handlers()
    chat_id = message.chat.id
    try:
        regex_surname = re.search("[a-zа-яёғҳзўқ]{3,}",message.text)
        if not regex_surname:
            if language_type["UZ"]:
                bot.send_message(chat_id,"Familiyangizni noto\'g\'ri kiritildi... boshqattan kiring")
            elif language_type["RU"]:
                bot.send_message(chat_id,"Фамилия введена некорректно... введите заново")
            elif language_type["EN"]:
                bot.send_message(chat_id,"Invalid surname entered... Try again")
            bot.register_next_step_handler(message,AskPhone)
        else:
            form_dict["surname"] = message.text
            #print(form_dict["surname"])
            if language_type["UZ"]:
                bot.send_message(chat_id,"Raqamingizni kiriting:")

            elif language_type["RU"]:
                bot.send_message(chat_id,"Введите ваш номер")
            elif language_type["EN"]:
                bot.send_message(chat_id,"Enter your phone number")
            bot.register_next_step_handler(message, AskEmail)
    except Exception as e:
        print(e)
        bot.send_message(chat_id,"ooops")

def AskEmail(message):
    bot.disable_save_next_step_handlers()
    chat_id = message.chat.id
    try:
        regex_phone = re.search("((998)9([3-5]|[7-9]){1}[0-9]{7})",message.text)
        if not regex_phone:
            if language_type["UZ"]:
                bot.send_message(chat_id,"Raqamingiz noto\'g\'ri kiritildi... boshqattan kiring")
            elif language_type["RU"]:
                bot.send_message(chat_id,"Номер введён некорректно... введите заново")
            elif language_type["EN"]:
                bot.send_message(chat_id,"Invalid phone number entered... Try again")
            bot.register_next_step_handler(message, AskEmail)
        else:
            form_dict["phone"] = message.text
            #print(form_dict["phone"])
            if language_type["UZ"]:
                bot.send_message(chat_id,"elektron pochtangizni kiriting:")
            elif language_type["RU"]:
                bot.send_message(chat_id,"Введите вашу электронную почту")
            elif language_type["EN"]:
                bot.send_message(chat_id,"Enter your email address")
            bot.register_next_step_handler(message, AskZip)
    except Exception as e:
        print(e)
        bot.send_message(chat_id,"ooops")

def AskZip(message):
    bot.disable_save_next_step_handlers()
    chat_id = message.chat.id
    try:
        regex_email = re.search(r"\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b",message.text)
        if not regex_email:
            if language_type["UZ"]:
                bot.send_message(chat_id,"elektron pochtangiz noto\'g\'ri kiritildi... boshqattan kiring")
            elif language_type["RU"]:
                bot.send_message(chat_id,"электронная почта введена некорректно... введите заново")
            elif language_type["EN"]:
                bot.send_message(chat_id,"Invalid email address entered... Try again")
            bot.register_next_step_handler(message, AskZip)
        else:
            form_dict["email"] = message.text
            #print(form_dict["email"])
            if language_type["UZ"]:
                bot.send_message(chat_id,"ZIP kodingizni kiriting:")
            elif language_type["RU"]:
                bot.send_message(chat_id,"Введите ваш ZIP код")
            elif language_type["EN"]:
                bot.send_message(chat_id,"Enter your ZIP code")
            bot.register_next_step_handler(message, AskAccount)
    except Exception as e:
        print(e)
        bot.send_message(chat_id,"ooops")


def AskAccount(message):
    bot.disable_save_next_step_handlers()
    chat_id = message.chat.id
    try:
        regex_zip = re.search(r"[0-9]{6}",message.text)
        if not regex_zip:
            if language_type["UZ"]:
                bot.send_message(chat_id,"ZIP kodingiz noto\'g\'ri kiritildi... boshqattan kiring")
            elif language_type["RU"]:
                bot.send_message(chat_id,"ваш ZIP код введён некорректно... введите заново")
            elif language_type["EN"]:
                bot.send_message(chat_id,"Invalid ZIP code entered... Try again")
            bot.register_next_step_handler(message, AskAccount)
        else:
            form_dict["zipCode"] = message.text
            #print(form_dict["zipCode"])
            #print(form_dict)
            data = "Name: "+form_dict["name"]+"\nSurname: "+form_dict["surname"]+"\nPhone: +"+str(form_dict["phone"])+"\ne-mail: "+form_dict["email"]+"\nTG_Name: @"+form_dict["tg_name"]+"\nZipCode: "+str(form_dict["zipCode"])+"\nbank_accountNum: "+str(form_dict["bank_accountNum"])
            if language_type["UZ"]:
                bot.send_message(chat_id,"Sizning ma\'lumotlaringiz:")
                bot.send_message(chat_id,data)
                bot.send_message(chat_id,"Arizangiz muvaffaqiyatli to\'ldirildi\njonatish uchun tugmani bosing",reply_markup=Buttons(language_type))
            elif language_type["RU"]:
                bot.send_message(chat_id,"Ваши данные:")
                bot.send_message(chat_id,data)
                bot.send_message(chat_id,"Ваша заявка была успешно принята \nчтобы отправить нажмите кнопку ниже",reply_markup=Buttons(language_type))
            elif language_type["EN"]:
                bot.send_message(chat_id,"Here is your data:")
                bot.send_message(chat_id,data)
                bot.send_message(chat_id,"your form filled successfully\npress button to send it",reply_markup=Buttons(language_type))   
    except Exception as e:
        print(e)
        bot.send_message(chat_id,"ooops")

@bot.message_handler(func=lambda mess: mess.text == "изменть язык" or mess.text == "tilni o'zgartirish" or mess.text == "change language")
def HandleLanguage(message):
    bot.disable_save_next_step_handlers()
    chat_id = message.chat.id
    bot.send_message(chat_id,"Tilni tanlang | Выберите язык | Choose language",reply_markup=Language())
    if message.text == "🇺🇿 UZ":
        language_type["UZ"] = True 
        language_type["RU"] = False 
        language_type["EN"] = False
        msg = bot.reply_to(message,"Ismingizni kiriting")
        bot.register_next_step_handler(msg,AskName)
    elif message.text == "🇷🇺 RU":
        language_type["RU"] = True 
        language_type["UZ"] = False 
        language_type["EN"] = False
        msg = bot.reply_to(message,"Введите ваше имя")
        bot.register_next_step_handler(msg,AskName)
    elif message.text == "🏴󠁧󠁢󠁥󠁮󠁧󠁿 EN":
        language_type["EN"] = True 
        language_type["UZ"] = False  
        language_type["RU"] = False
        msg = bot.reply_to(message,"Enter your name")
        bot.register_next_step_handler(msg,AskName)
    else:
        bot.send_message(message.chat.id,"Please choose language...")

@bot.message_handler(func=lambda mess: mess.text == "отправить" or mess.text == "yuborish" or mess.text == "send")
def MainPage(message):
    try:
        bot.disable_save_next_step_handlers()
        language_type["isSend"] = True
        language_type["Counter"] +=1
        chat_id = message.chat.id
        Mydata = "Name: "+form_dict["name"]+"\nSurname: "+form_dict["surname"]+"\nPhone: +"+str(form_dict["phone"])+"\ne-mail: "+form_dict["email"]+"\nTG_Name: @"+form_dict["tg_name"]+"\nZipCode: "+str(form_dict["zipCode"])+"\nbank_accountNum: "+str(form_dict["bank_accountNum"])
        bot.send_message(chat_id,"Your data here:\n"+Mydata,reply_markup=Buttons(language_type))
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id,"ooops")

@bot.message_handler(func=lambda mess: mess.text == "заполнить заново" or mess.text == "yangidan to\'ldirish" or mess.text == "re-fill form")
def RefillForm(message):
    bot.disable_save_next_step_handlers()
    try:
        bot.send_message(message.chat.id,"Tilni tanlang | Выберите язык | Choose language",reply_markup=Language())
    except Exception as e:
        print(e)


@bot.message_handler(func=lambda mess: mess.text == "Restart!")
def Restart(message):
    try:
        bot.send_message(message.chat.id,"/start")
        bot.register_next_step_handler(message,Starter)
    except Exception as e:
        print(e)
        

def main():
    bot.polling(none_stop=True,interval=1)

if __name__ == "__main__":
    main()