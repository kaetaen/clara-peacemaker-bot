import telebot
import env

bot = telebot.TeleBot(env.TOKEN)
bot.remove_webhook()

@bot.message_handler(commands=['start'])
def welcome(msg):
    bot.send_message(msg.chat.id, 'Olá, sou a Clara, posso te ajudar nos momentos de ansiedade')


@bot.message_handler(commands=['respire'])
def breathe(msg):
    img = open('./assets/breath.gif', 'rb')
    bot.send_document(msg.chat.id, img)


if __name__ == '__main__':
    bot.polling()

