from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


button_yes = InlineKeyboardButton('Участвую!', callback_data='button1_yes')

hello_kb = InlineKeyboardMarkup().add(button_yes)
