import os

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.environ['API_TOKEN']

predicts = {'Новосибирская область': '800'}

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Привет! Введи название страны или региона РФ')


@dp.message_handler(commands=['switch'])
def switch(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text='Try', switch_inline_query='Telegram')
    markup.add(switch_button)
    await message.answer(message.chat.id, 'Выбрать чат', reply_markup=markup)


@dp.message_handler()
async def handler(message: types.Message):
    try:
        await message.answer(predicts[message.text])
    except KeyError:
        await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
