import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    exit("Error: BOT_TOKEN is missing in .env file!")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



def get_main_keyboard() -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    # Додаємо кнопки у сітку
    builder.button(text="➕ Add Income")
    builder.button(text="➖ Add Expense")
    builder.button(text="📊 View")
    builder.button(text="📈 Statistics")
    builder.button(text="💰 Balance")
    builder.button(text="⚙️ Settings")

    # Формуємо сітку: 2 кнопки в рядку
    builder.adjust(2)

    # resize_keyboard=True робить кнопки компактними
    return builder.as_markup(resize_keyboard=True)


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привіт, {message.from_user.first_name}! 👋\n"
        f"Ласкаво просимо до **Finance Tracker Bot**!\n\n"
        f"Обери дію на клавіатурі нижче:",
        reply_markup=get_main_keyboard(),
        parse_mode="Markdown",
    )


# 2. Реагуємо на кнопку "💰 Balance"
@dp.message(F.text == "💰 Balance")
async def show_balance(message: types.Message):
    from storage import load_data

    incomes, expenses = load_data()

    total_inc = sum(item["amount"] for item in incomes)
    total_exp = sum(item["amount"] for item in expenses)
    balance = total_inc - total_exp

    response_text = (
        "💰 **ПОТОЧНИЙ БАЛАНС**\n\n"
        f"📥 Загальний доход: `{total_inc:.2f}`\n"
        f"📤 Загальні витрати: `{total_exp:.2f}`\n"
        f"-------------------\n"
        f"💳 Баланс: `{balance:.2f}`"
    )

    await message.answer(response_text, parse_mode="Markdown")



async def main():
    print("🚀 Bot is running... Напиши боту /start у Telegram!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())