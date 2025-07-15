import telebot
from telebot import types

TOKEN = "7231257838:AAFFtuNDECCnxbFFPnrHatFMgNSVXVnjX9M"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    item1 = types.InlineKeyboardButton("vs code установка боюнча", url="https://youtu.be/30AuuZtdZUM")
    item2 = types.InlineKeyboardButton("папка ачуу боюнча", url="https://youtu.be/30AuuZtdZUM")
    item3 = types.InlineKeyboardButton("сурот коюу боюнча", url="https://youtu.be/30AuuZtdZUM")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Саламатсызбы, кандай жардам керек? Сизге керектүү бөлүмдү тандаңыз:",
                     reply_markup=markup)

bot.remove_webhook()

bot.polling()