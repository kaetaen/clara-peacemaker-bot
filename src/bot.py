import telebot
import env

bot = telebot.TeleBot(env.TOKEN)
bot.remove_webhook()


