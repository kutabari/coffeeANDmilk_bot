from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import random
import os

# МИЛЫЕ СООБЩЕНИЯ
MESSAGES = [
    "Ты мой солнечный лучик даже в самый серый день.",
    "Обожаю тебя всем сердцем.",
    "Ты — как глоток теплого какао зимой.",
    "Обнять бы тебя сейчас, и не отпускать.",
    "Спасибо, что ты у меня есть."
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

if __name__ == '__main__':
    from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
    import os

    # Создание приложения с токеном
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

    # Регистрируем обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    print("Бот запущен!")
    
    # Запуск бота
    app.run_polling()