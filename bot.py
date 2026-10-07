import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    user_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⚽ ቡድን ምረጥ (Fantasy Team)",
                    callback_data="play_fantasy",
                )
            ],
            [
                InlineKeyboardButton(
                    text="💳 ሂሳብ አስገባ (Chapa Payment)", callback_data="deposit"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🏆 የደረጃ ሰንጠረዥ (Leaderboard)",
                    callback_data="leaderboard",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📢 ቻናላችንን ይቀላቀሉ (Link)",
                    url="https://t.me/MedaFantasyBot",
                )
            ],
        ]
    )

    welcome_text = (
        f"ሰላም {user_name}! 👋\n\n"
        f"እንኳን ወደ **ሜዳ ፋንታሲ (Meda Fantasy)** በደህና መጡ! ⚽🔥\n\n"
        f"የራስዎን ቡድን ይገንቡ፣ ይወዳደሩ፣ ነጥብ ይሰብስቡ እና ታላላቅ ሽልማቶችን ያሸንፉ!\n\n"
        f"ከታች ካሉት አማራጮች አንዱን ይምረጡ፦"
    )

    await message.answer(welcome_text, reply_markup=keyboard, parse_mode="Markdown")


@dp.callback_query(lambda c: c.data == "play_fantasy")
async def play_fantasy_callback(callback: types.CallbackQuery):
    await callback.message.answer(
        "⚽ የፋንታሲ ውድድሩ በቅርቡ ይጀምራል! ዝግጅት ላይ ነን..."
    )
    await callback.answer()


@dp.callback_query(lambda c: c.data == "deposit")
async def deposit_callback(callback: types.CallbackQuery):
    await callback.message.answer(
        "💳 የቻፓ (Chapa) ክፍያ ስርዓት በመገናኘት ላይ ነው..."
    )
    await callback.answer()


@dp.callback_query(lambda c: c.data == "leaderboard")
async def leaderboard_callback(callback: types.CallbackQuery):
    await callback.message.answer(
        "🏆 የደረጃ ሰንጠረዥ፦ ውድድሩ ሲጀምር ነጥቦች እዚህ ይታያሉ።"
    )
    await callback.answer()


async def main():
    print("Meda Fantasy Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
