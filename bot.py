import config
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=config.BOT_TOKEN)
bot_dispatcher = Dispatcher(bot)


@bot_dispatcher.message_handler(commands=['start', 'help'])
async def welcome_handler(message: types.Message):
    '''Sends welcome message on /start command'''
    await message.reply(config.WELCOME_MESSAGE)


if __name__ == "__main__":
    executor.start_polling(bot_dispatcher)
