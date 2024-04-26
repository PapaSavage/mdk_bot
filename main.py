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
        text="Добро пожаловать в наш магазин! 🛍️\n\n"
        "Здесь вы можете просмотреть наш ассортимент товаров, сделать заказ и отследить его статус.\n\n"
        "Используйте кнопки меню ниже, чтобы начать покупки или проверить ваши заказы. Приятных покупок! 😊",
        reply_markup=kb.keyboard_builder(
            [
                [
                    "🛒 Меню",
                    "",
                    "https://mdk-botstore.vercel.app/" + str(message.from_user.id),
                ],
                [
                    "📦 Мои заказы",
                    "",
                    "https://mdk-botstore.vercel.app/order/"
                    + str(message.from_user.id),
                ],
            ]
        ),
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
