from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


button_yes = InlineKeyboardButton('Участвую!', callback_data='button1_yes')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
greet_kb.add(button_yes)

hello_kb = InlineKeyboardMarkup().add(button_yes)
