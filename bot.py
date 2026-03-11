import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ---------------------------------------------
# التوكن من Environment Variable (آمن للنشر)
# ---------------------------------------------
TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError("ضع التوكن في Environment Variable باسم TELEGRAM_TOKEN")

# ---------------------------------------------
# إعداد زر التعليمات
# ---------------------------------------------
keyboard = [["تعليمات"]]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ---------------------------------------------
# دالة /start
# ---------------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "اهلا بك 👋\n"
        "ارسل رقم هاتف حساب سويج\n"
        "يجب أن يبدأ بـ +9647\n"
        "او اضغط زر تعليمات",
        reply_markup=markup
    )

# ---------------------------------------------
# دالة التعامل مع الرسائل
# ---------------------------------------------
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "تعليمات":
        await update.message.reply_text(
            "📌 تعليمات الاستخدام:\n"
            "1️⃣ ارسل رقم هاتفك المسجل في سويج\n"
            "2️⃣ يجب أن يبدأ الرقم بـ +9647\n"
            "3️⃣ مثال: +9647701234567\n\n"
            "❌ تأكد من إرسال رقم هاتف صحيح بدون نصوص أو رموز إضافية\n"
        )
        return

    phone = text

    # التحقق من النصوص
    if any(c.isalpha() for c in phone):
        await update.message.reply_text("❌ ارسل رقم موبايل فقط بدون نص")
        return

    # التحقق من البداية
    if not phone.startswith("+9647"):
        await update.message.reply_text("❌ الرقم يجب أن يبدأ بـ +9647")
        return

    digits = phone[4:]

    # التحقق من الأرقام
    if not digits.isdigit():
        await update.message.reply_text("❌ ارسل رقم موبايل صحيح بدون رموز")
        return

    # التحقق من الطول
    if len(digits) < 10:
        await update.message.reply_text("❌ الرقم ناقص")
    elif len(digits) > 10:
        await update.message.reply_text("❌ الرقم يحتوي أرقام زائدة")
    else:
        await update.message.reply_text("✅ الرقم صحيح وتم التحقق منه")

# ---------------------------------------------
# تشغيل البوت
# ---------------------------------------------
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
