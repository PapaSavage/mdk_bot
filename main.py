import asyncio
import logging
from aiogram import Bot, Dispatcher, types

import keyboards as kb

from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Hello!",
        reply_markup=kb.keyboard_builder(
            [
                [
                    "Меню",
                    "",
                    "https://papasavage.github.io/",
                ],
                ["Мои заказы", "", "https://ya.ru/"],
                ["Профиль", "", "https://ya.ru/"],
                ["Контакты", "", "https://ya.ru/"],
                ["Пригласить друзей", "", "https://ya.ru/"],
            ]
        ),
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
