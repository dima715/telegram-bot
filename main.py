import asyncio
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes
)

TOKEN = "7939865066:AAFhpeLRbSp_yIYemSho_O-X3duOkBvfEas"
ADMIN_ID = 6774979870
paid_users = set()
user_state = {}

PAY_LINK = "http://t.me/send?start=IVXy7unLSl22"

keyboard = [
    [InlineKeyboardButton("🗑️ Снести сессии", callback_data="attack")],
    [InlineKeyboardButton("📚 Инструкция", callback_data="instruction")],
    [InlineKeyboardButton("💳 Оплатить доступ", url=PAY_LINK)]
]
markup = InlineKeyboardMarkup(keyboard)

async def clear_webhook_and_updates():
    bot = Bot(token=TOKEN)
    await bot.delete_webhook()
    await bot.get_updates(offset=-1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://i.postimg.cc/6Q2s4Hbn/Chat-GPT-Image-7-2025-13-31-06.png",
        caption="Привет! Я бот-ликвидатор сессий.\nВыбери действие ниже:",
        reply_markup=markup
    )

async def main():
    await clear_webhook_and_updates()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
