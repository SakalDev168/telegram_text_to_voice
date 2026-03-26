import os
from gtts import gTTS
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Get token from environment
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN not set")

def text_to_speech(text, filename="voice.mp3"):
    tts = gTTS(text=text, lang='km')
    tts.save(filename)
    return filename

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    file_path = text_to_speech(user_text)

    await update.message.reply_text("🔊 កំពុងបំលែងសំឡេង...")

    with open(file_path, "rb") as audio:
        await update.message.reply_voice(audio)

    os.remove(file_path)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("✅ Bot running...")
app.run_polling()
