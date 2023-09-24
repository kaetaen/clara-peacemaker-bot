import telebot
from positive_vibes_api import PositiveVibesAPI as Media
import messages
import os
from flask import Flask, request

#SECRET = 'dkejwejao28888udsadya'
url = 'https://clarapeacemakerbot.onrender.com'

bot = telebot.TeleBot("6446946135:AAFUNqmJGto0OXcKyHbPWJP-x4ygJciBs9w", threaded=False)
bot.remove_webhook()
bot.set_webhook(url=url)

app = Flask(__name__)

@app.route('/foo', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200


@bot.message_handler(commands=['start', 'sobre'])
def welcome(msg):
    bot.send_message(msg.chat.id, messages.ABOUT)


@bot.message_handler(commands=['respire'])
def breathe(msg):
    bot.send_document(msg.chat.id, 'https://media.giphy.com/media/1xVc4s9oZrDhO9BOYt/source.gif')


@bot.message_handler(commands=['reflita'])
def think(msg):
    episode = Media().get_podcast()
    bot.send_document(msg.chat.id, episode["url"], caption=episode["title"])
    

@bot.message_handler(commands=['escute'])
def listen(msg):
    music = Media().get_music()
    bot.send_audio(msg.chat.id, music["file"], caption=messages.SONG_TAG(music))


@bot.message_handler(commands=['contemple'])
def enjoy(msg):
    image = Media().get_image()
    quote = Media().get_quote()
    bot.send_photo(msg.chat.id, image, caption=quote)


@bot.message_handler(commands=['converse'])
def talk(msg):
   bot.send_message(
       msg.chat.id,
       messages.EXTERNAL_REFS,
       disable_web_page_preview=True
   )


app = Flask(__name__)

@app.route('/', methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


if __name__ == '__main__':
    bot.polling()

