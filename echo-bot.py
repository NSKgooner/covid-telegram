import os

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.environ['API_TOKEN']

predicts = {'Новосибирская область': '800'}

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Hi!')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(predicts.get(message.text))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
