import telebot
import env
from media import LINKS
from utils.randomize import get_random_file

bot = telebot.TeleBot(env.TOKEN)
bot.remove_webhook()

@bot.message_handler(commands=['start'])
def welcome(msg):
    bot.send_message(msg.chat.id, 'Olá, sou a Clara, posso te ajudar nos momentos de ansiedade')


@bot.message_handler(commands=['respire'])
def breathe(msg):
    bot.send_document(msg.chat.id, LINKS["gifs"][0])

@bot.message_handler(commands=['escute'])
def listen(msg):
    bot.send_audio(msg.chat.id, get_random_file('audios', LINKS))
    

if __name__ == '__main__':
    bot.polling()

