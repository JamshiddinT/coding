from transliterate import to_cyrillic, to_latin
from telebot import *

bot = telebot.TeleBot("6531411171:AAFP-4UWgdtc0Vl_DmZWVjFn413V2ok6V-o", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
apihelper.SESSION_TIME_TO_LIVE = 2 * 60
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salom. Faqat matn kiriting: ")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    if msg.isascii():
        reply=to_cyrillic(msg)
    else:
        reply=to_latin(msg)
    bot.reply_to(message, reply)

bot.infinity_polling()

    










