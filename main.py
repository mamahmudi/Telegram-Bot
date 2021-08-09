import os
import telebot

my_secret = os.environ['bot_token']
bot = telebot.TeleBot(my_secret)

@bot.message_handler(commands = ["Hi"])
def first_command(message):
    bot.reply_to(message, "Hi back!")


@bot.message_handler(commands = ["Asdfg"])
def second_command(message):
    bot.send_message(message.chat.id, "FU")


bot.polling()