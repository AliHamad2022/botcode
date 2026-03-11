from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")  # ضع التوكن في Environment Variable على Render

keyboard = [["تعليمات"]]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اهلا بك 👋\nارسل رقم هاتف حساب سويج\nيجب أن يبدأ بـ +9647\nاو اضغط زر تعليمات",
                                    reply_markup=markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text == "تعليمات":
        await update.message.reply_text("تعليمات...")
        return
    # باقي التحقق من الرقم كما في كودك السابق

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
