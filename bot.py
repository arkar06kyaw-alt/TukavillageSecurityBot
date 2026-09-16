import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 သုခရွာ Security Bot အလုပ်လုပ်နေပါပြီ။"
    )


async def delete_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message

    if not message or not message.text:
        return

    text = message.text.lower()

    link_words = [
        "http://",
        "https://",
        "www.",
        "t.me/",
        "telegram.me/"
    ]

    if any(link in text for link in link_words):
        try:
            await message.delete()
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="⚠️ Link တင်ခြင်းကို ခွင့်မပြုပါ။"
            )
        except Exception:
            pass


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN မတွေ့ပါ")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, delete_links)
    )

    print("Tukavillage Security Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
