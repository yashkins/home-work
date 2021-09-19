
from datetime import date, datetime
import ephem
from glob import glob
import logging
from random import randint, choice
import settings 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, messagehandler


logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print("Вызван: /start")
    update.message.reply_text("Привет")

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)
    

def definition_planet(update,context):
    planet_def = update.message.text.split()[-1].capitalize()
    corrent_date = date.today()
    planet = getattr(ephem, planet_def)(corrent_date.strftime('%Y/%m/%d'))
    constellation = ephem.constellation(planet)
    update.message.reply_text(constellation)


def logic_play(user_digit):
    bot_digit = randint(user_digit-10, user_digit+10)
    result = "Вы выиграли" * (user_digit > bot_digit) + "Вы проиграли" * (user_digit < bot_digit)+ "Ничья" * (user_digit == bot_digit)
    return f"Ваше число {user_digit} Мое число {bot_digit} \n" + result


def play_digit(update, context):
    if context.args:
        try:
            user_digit = int(context.args[0])
            messages = logic_play(user_digit)
        except (TypeError, ValueError):
            messages = "Введите целое число"
    else:
        messages = "Введите число"
    update.message.reply_text(messages)



def main():
    mybot = Updater(settings.API_KEY, use_context = True, request_kwargs = PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("digit", play_digit))
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", definition_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__=="__main__":
    main()
