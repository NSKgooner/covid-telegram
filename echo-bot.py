import os

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import CallbackQuery, ContentType, Message, ParseMode
from aiogram.utils.markdown import bold, text

from keyboards import hello_kb
from texts import HELLO_TEXT

API_TOKEN = os.environ['API_TOKEN']

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    await message.reply(HELLO_TEXT, reply_markup=hello_kb)


@dp.message_handler(commands=['button_yes'])
async def send_button(message: Message):
    await message.reply('Введи свои имя и фамилию')


@dp.callback_query_handler(lambda c: c.data == 'button_yes')
async def process_callback_button1(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введи свои имя и фамилию')


@dp.message_handler()
async def handler(message: Message):
    try:
        await message.answer('Отлично, жди когда бот пришлет собеседника!')
    except KeyError:
        await message.answer('Привет!\nИспользуй /help, чтобы узнать список доступных команд!')


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(message: Message):
    message_text = text(bold('Я могу ответить на команды /start, /help, sep="\n"'))
    await message.answer(message_text, parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
