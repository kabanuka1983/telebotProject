import telebot
from config import TOKEN


bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message=message, text='Hi')


@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, text=message.text)


bot.infinity_polling()
