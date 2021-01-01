import telebot
import env
from positive_vibes_api import PositiveVibesAPI as Media

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
    quote = Media().get_quote()
    bot.send_message(msg.chat.id, quote)
    

@bot.message_handler(commands=['escute'])
def listen(msg):
    music = Media().get_music()
    msg_title = f'🎵 Canção: {music["song_name"]} \n👨 Artista: {music["artist_name"]}'
    bot.send_document(msg.chat.id, music["file"], caption=msg_title)


@bot.message_handler(commands=['contemple'])
def enjoy(msg):
    image = Media().get_image()
    quote = Media().get_quote()
    bot.send_photo(msg.chat.id, image, caption=quote)


if __name__ == '__main__':
    bot.polling()

