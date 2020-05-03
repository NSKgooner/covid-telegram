from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove
)

button_hi = KeyboardButton('Привет!')
button_help = KeyboardButton('Помочь?')

inline_button = InlineKeyboardButton('Первая кнопка!', callback_data='button1')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
greet_kb.add(button_hi)
greet_kb.add(button_help)

inline_kb = InlineKeyboardMarkup().add(inline_button)
