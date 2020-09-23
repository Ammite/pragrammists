import telebot
import variables

bot = telebot.TeleBot(variables.token)
hello_messages = ['привет', 'дратвуй', 'здравствуйте', 'хай']
name_messages = ['как тебя зовут', 'твоё имя', 'как тебя звать', 'какое у тебя имя', 'как тебя зовут?', 'твоё имя?',
                 'как тебя звать?', 'какое у тебя имя?']


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Ты впервые тут? Давай работать!")


@bot.message_handler(content_types=['text'])
def messaging(message):
    if message.text.lower() in hello_messages:
        bot.send_message(message.chat.id, "Привет! Ботать?")
    elif message.text.lower() in name_messages:
        bot.send_message(message.chat.id, "Меня зовут PragrammistBot!")
    elif message.text == "Пока":
        bot.send_message(message.chat.id, "Пока, друг!")
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling()
