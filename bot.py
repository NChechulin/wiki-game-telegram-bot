"""
Main bot file
"""


from aiogram import Bot, Dispatcher, executor, types
from core import search
from json import loads as load_json
from urllib.parse import urlparse
from re import compile as compile_regex

config = None
bot = None
bot_dispatcher = None
URL_REGEX = compile_regex(
    "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
)


def load_config():
    global config
    try:
        with open("config.json", "r") as fh:
            raw_data = fh.read()
        config = load_json(raw_data)
    except Exception as e:
        print("Could not open config. Error: " + str(e))


if __name__ == "__main__":
    """
    Main is located on top because decorators need a dispatcher object, which is created here
    """
    load_config()

    if config:
        bot = Bot(token=config["BOT_TOKEN"])
        bot_dispatcher = Dispatcher(bot)


@bot_dispatcher.message_handler(commands=["start", "help"])
async def welcome_handler(message: types.Message) -> None:
    """Sends welcome message on /start command"""
    await message.reply(config["WELCOME_MESSAGE"])


@bot_dispatcher.message_handler()
async def search_handler(message: types.Message) -> None:
    """
    Checks if sent message is a EN Wiki article and sends the result back.
    """
    try:
        url = urlparse(message.text)
        if URL_REGEX.match(message.text) and url.path != "":

            if url.netloc == "en.wikipedia.org":
                await message.reply(search.search(message.text))
            elif url.netloc == "en.m.wikipedia.org":
                await message.reply(
                    search.search(message.text.replace("en.m.wiki", "en.wiki"))
                )
            else:
                await message.reply(config["WRONG_URL_MESSAGE"])
        else:
            await message.reply(config["WRONG_URL_MESSAGE"])
    except Exception:
        await message.reply(config["ERROR_MESSAGE"])

executor.start_polling(bot_dispatcher)
