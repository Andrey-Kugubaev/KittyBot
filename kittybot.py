import logging
import os

import requests

from telegram.ext import CommandHandler, Updater, Filters, MessageHandler
from telegram import ReplyKeyboardMarkup
from telegram import bot

from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')
channel_id = os.getenv('CHANNEL')
updater = Updater(token=secret_token, use_context=True)

logging.basicConfig(
    level=logging.INFO,
    filename='main.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)


URL = 'https://api.thecatapi.com/v1/images/search'
OTHER_URL = 'https://api.thedogapi.com/v1/images/search'


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name

    button = ReplyKeyboardMarkup(
        [['help', 'show cat', 'send cat']],
        resize_keyboard=True,
    )

    context.bot.send_message(
        chat_id=chat.id,
        text='Hello, {}! How are you? Make a choice, please!'.format(name),
        reply_markup=button
    )


def info_help(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    urlchannel = 'https://t.me/theworldofcats'

    text = '{}! You can ask me to send a random photo with a cat. ' \
           'Or you can send me your photo for publishing it in a channel {}!\n' \
           '\n' \
           '"show cat"  -  this command will send you a random cat photo\n' \
           '\n' \
           '"send cat"  - after this command you can send me a photo will ' \
           'publish later in my channel. Please add an info in the ' \
           'description about a place the photo was taken at' \
           ''.format(name, urlchannel)
    context.bot.send_message(
        chat_id=chat.id,
        text=text,
    )


def get_new_image():
    try:
        response = requests.get(URL)
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        response = requests.get(OTHER_URL)

    response = response.json()
    random_photo = response[0].get('url')
    return random_photo


def new_cat(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    text = '{}! Look whom I found for you'.format(name)
    context.bot.send_photo(chat.id, get_new_image(), caption=text)


def send_cat(update, context):
    chat = update.effective_chat
    text = "Great! Send me a photo with one or several cats " \
           "and write me where you took it. Thanks!"
    context.bot.send_message(
        chat_id=chat.id,
        text=text
    )
    try:
        updater.dispatcher.add_handler(MessageHandler(Filters.photo, photo_cat))
    except:
        context.bot.send_message(
            chat_id=chat.id,
            text='Something went wrong, please upload the photo again',
        )


def photo_cat(update, context):
    text = update.message.caption
    image_cat = update.message.photo[-1]
    context.bot.send_photo(
        chat_id=channel_id,
        photo=image_cat,
        caption=text
    )


def unknown(update, context):
    chat = update.effective_chat
    text = "Sorry, I didn't understand that command"
    context.bot.send_message(
        chat_id=chat.id,
        text=text
    )


def main():
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(MessageHandler(Filters.text('help'), info_help))
    updater.dispatcher.add_handler(MessageHandler(Filters.text('send cat'), send_cat))
    updater.dispatcher.add_handler(MessageHandler(Filters.text('show cat'), new_cat))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
