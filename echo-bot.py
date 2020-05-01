from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1258774903:AAF4hMnM3bYYEQ0bgeodVw7Lf75FIiUUFIA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Hi!')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
