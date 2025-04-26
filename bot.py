from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import random
import os
import asyncio

# МИЛЫЕ СООБЩЕНИЯ
MESSAGES = [
    "ты мой солнечный лучик даже в самый серый день.",
    "обожаю тебя всем сердцем.",
    "ты — как глоток теплого какао зимой.",
    "обнять бы тебя сейчас, и не отпускать.",
    "cпасибо, что ты у меня есть."
]

# ОБРАБОТКА /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Пошли милость", callback_data="send_love")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Я — бот с милостями. Хочешь немного любви?", reply_markup=reply_markup)

# ОБРАБОТКА НАЖАТИЯ КНОПКИ
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    message = random.choice(MESSAGES)
    await query.edit_message_text(text=message)

# ЗАПУСК БОТА
async def main():
    token = os.getenv("BOT_TOKEN")  # Получаем токен из переменной окружения
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    print("Бот запущен!")
    await app.run_polling()

# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())  # Эта строка запускает цикл, и бот будет работать 24/7