from telegram.ext import Updater, CommandHandler

PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(update, context):
    print("Вызван: /start")
    update.message.reply_text("Привет")

def main():
    mybot = Updater("1978137503:AAFi3gKfGucEZdQcM79SeNz3O0YTgYaivpA", use_context = True, request_kwargs = PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    mybot.start_polling()
    mybot.idle()


main()
