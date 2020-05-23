from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


button_yes = InlineKeyboardButton('Участвую!', callback_data='button_yes')

hello_kb = InlineKeyboardMarkup().add(button_yes)

button_tomorrow = InlineKeyboardButton('Участвую!', callback_data='button_tomorrow')

tomorrow_kb = InlineKeyboardMarkup().add(button_yes)
