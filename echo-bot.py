import os

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ContentType, Message, ParseMode
from aiogram.utils.markdown import bold, text

from keyboards import greet_kb

API_TOKEN = os.environ['API_TOKEN']

predicts = {'Новосибирская область': '800'}

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    await message.reply('Привет! Введи название страны или региона РФ', reply_markup=greet_kb)


@dp.message_handler()
async def handler(message: Message):
    try:
        await message.answer(predicts[message.text])
    except KeyError:
        await message.answer('Привет!\nИспользуй /help, чтобы узнать список доступных команд!')


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(message: Message):
    message_text = text(bold('Я могу ответить на команды /start, /help, sep="\n"'))
    await message.answer(message_text, parse_mode=ParseMode.MARKDOWN)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
