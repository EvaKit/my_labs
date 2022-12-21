import telebot
import requests
from random import randint

bot = telebot.TeleBot('token')

@bot.message_handler(content_types='text')
def send_joke(message):
    if message.text == 'Хочу анекдот':
        number = randint(2, 386)
        url1 = 'https://api.sampleapis.com/jokes/goodJokes'
        res = requests.get(url=url1)
        result1 = res.json()[number]['setup']
        result2 = res.json()[number]['punchline']
        bot.send_message(message.chat.id, result1)
        bot.send_message(message.chat.id, result2)
    else:
        bot.send_message(message.chat.id, 'Глаза разуй, я сказал писать мне "Хочу анекдот"')
        
bot.polling(non_stop=True)
