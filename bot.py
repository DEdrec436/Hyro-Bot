
from config import token
from random import choice
#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

bot = telebot.TeleBot(token)
bot.delete_webhook()

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет! Я Hyro Bot!.
Я способен абсолютно на всё, ну же протестируй меня!!\
""")
@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice([
        
        "ОРЕЛ-источник: https://platform.kodland.org/ru/task_96343/", 
        "РЕШКА-источник: https://platform.kodland.org/ru/task_96343/" ])
    bot.reply_to(message, coin)
@bot.message_handler(commands=['fact'])
def fact_handler(message):
        fact = choice(["Интересный факт - Batman: Arkham Asylum чуть не стала ритм-игрой.На ранних уровнях разработки боевая система в прототипе Batman: Arkham Asylum выглядела как ритм-игра. Второй прототип проводил встречи с врагами в виде двумерного файтинга. Обе эти попытки были отбракованы, но их наработки воплотились в итоговом варианте игры.- https://medium.com/cybervalhalla/",
                        "Интересный факт - Первая видеоигра в космосе.Тетрис. В 1993 году Game Boy с игрой оказался на борту ракеты “Союз ТМ-17”, а затем — на космической станции “Мир”, где в него играл космонавт Александр Серебров. Позже игру продали на аукционе за $1220. - https://medium.com/cybervalhalla/ "])
        bot.reply_to(message, fact)
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text) 


    



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
