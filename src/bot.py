import telebot
import env

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
    pass

@bot.message_handler(commands=['escute'])
def listen(msg):
    pass


@bot.message_handler(commands=['contemple'])
def enjoy(msg):
    pass

if __name__ == '__main__':
    bot.polling()

