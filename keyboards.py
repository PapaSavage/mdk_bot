from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
)

from aiogram import types


def keyboard_builder(data):
    keyboard = types.InlineKeyboardMarkup()

    for item in data:
        keyboard.add(
            types.InlineKeyboardButton(
                text=item[0],
                # callback_data=item[item[1]],
                web_app=WebAppInfo(url=item[2]),
            )
        )

    return keyboard
