import telebot
from setting import TOKEN
from wfload import wf_load

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help']) # комманды 
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, напиши мне ник персонажа Warface, и я пришлю тебе его статистику.')


@bot.message_handler(content_types=['text']) # новое сообщение
@bot.edited_message_handler(content_types=['text']) # если пользователь изменяет сообщение
def send_text(message):
    bot.send_message(message.from_user.id, wf_load(message.text))

bot.polling()