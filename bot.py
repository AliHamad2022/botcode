import re

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8541212639:AAGIETbBhd8--jTpS7ouLrnG5K5LO7GjLlU"


# زر التعليمات
keyboard = [["تعليمات"]]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "اهلا بك 👋\n"
        "ارسل رقم هاتف حساب سويج\n"
        "يجب أن يبدأ بـ +9647\n"
        "او اضغط زر تعليمات",
        reply_markup=markup
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    # زر التعليمات
    if text == "تعليمات":

        await update.message.reply_text(
            "📌 تعليمات الاستخدام:\n"
            "1️⃣ ارسل رقم هاتفك المسجل في سويج\n"
            "2️⃣ يجب أن يبدأ الرقم بـ +9647\n"
            "3️⃣ مثال:\n"
            "+9647701234567\n\n"
            "❌ تأكد من إرسال رقم هاتف صحيح بدون نصوص أو رموز إضافية\n\n"
        )

        # الرسالة الثانية
        await update.message.reply_text(
            "📌 تعليمات إضافية:\n"
            "1️⃣ بعد تسجيل رقمك سوف تتلقى وقت دخول بصمة مثال 3:12:55\n"
            "2️⃣ بعد ظهور الكاميرا انتظر الوقت الآخر لالتقاط الصورة\n\n"
            "لأي استفسار، تواصل معنا في الدعم "
            "<a href='https://t.me/ansalif'>@ansalif</a>\n\n"
            "شكراً لاستخدامك البوت!",
            parse_mode="HTML"
        )

        return

    phone = text

    # إذا أرسل نص
    if any(c.isalpha() for c in phone):
        await update.message.reply_text("❌ ارسل رقم موبايل فقط بدون نص")
        return

    # التحقق من بداية الرقم
    if not phone.startswith("+9647"):
        await update.message.reply_text("❌ الرقم يجب أن يبدأ بـ +9647")
        return

    digits = phone[4:]

    # التحقق أن الباقي أرقام
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


# تشغيل البوت
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()