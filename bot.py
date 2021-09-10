import logging
from re import X
import settings 
import ephem
from datetime import date
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
    print(planet_def)
    corrent_date = date.today()
    planet = ephem.planet_def(f'{corrent_date.year}/{corrent_date.month}/{corrent_date.day}')
    constellation = ephem.constellation(planet)
    update.message.reply_text(constellation)

def main():
    mybot = Updater(settings.API_KEY, use_context = True, request_kwargs = PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", definition_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__=="__main__":
    main()
