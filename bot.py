"""
Main bot file
"""


from aiogram import Bot, Dispatcher, executor, types
from core import search
import config
from urllib.parse import urlparse

bot = Bot(token=config.BOT_TOKEN)
bot_dispatcher = Dispatcher(bot)


@bot_dispatcher.message_handler(commands=["start", "help"])
async def welcome_handler(message: types.Message) -> None:
    """Sends welcome message on /start command"""
    await message.reply(config.WELCOME_MESSAGE)


@bot_dispatcher.message_handler()
async def search_handler(message: types.Message) -> None:
    """
    Checks if sent message is an English Wikipedia article and sends the result back.
    """
    try:
        url = urlparse(message.text)
        if url.netloc == "en.wikipedia.org" and url.path != "":
            await message.reply(search.search(message.text))
        else:
            await message.reply(config.WRONG_URL_MESSAGE)
    except:
        await message.reply(config.ERROR_MESSAGE)


if __name__ == "__main__":
    executor.start_polling(bot_dispatcher)
