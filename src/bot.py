import telebot
import env
from positive_vibes_api import Quotes, Music

bot = telebot.TeleBot(env.TOKEN)
bot.remove_webhook()

@bot.message_handler(commands=['start'])
def welcome(msg):
    bot.send_message(msg.chat.id, 'Olá, sou a Clara, posso te ajudar nos momentos de ansiedade')


@bot.message_handler(commands=['respire'])
def breathe(msg):
    bot.send_document(msg.chat.id, 'https://media.giphy.com/media/1xVc4s9oZrDhO9BOYt/source.gif')


@bot.message_handler(commands=['reflita'])
def think(msg):
    quote = Quotes().randomQuote()
    bot.send_message(msg.chat.id, quote)
    

@bot.message_handler(commands=['escute'])
def listen(msg):
    music = Music().randomMusic()
    bot.send_audio(msg.chat.id, music)


@bot.message_handler(commands=['contemple'])
def enjoy(msg):
    ...
    

if __name__ == '__main__':
    bot.polling()

