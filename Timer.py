import os
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Command to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! I can send you a photo after a timer. Use /set_timer <seconds>."
    )

# Command to set the timer
async def set_timer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Extract the timer duration
        duration = int(context.args[0])
        if duration <= 0:
            raise ValueError

        await update.message.reply_text(
            f"Timer set for {duration} seconds. I'll send a photo when the timer expires!"
        )

        # Wait for the specified time
        time.sleep(duration)

        # Send the photo
        photo_path = "photos/sample.jpg"
        if os.path.exists(photo_path):
            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=open(photo_path, "rb"),
                caption="Here’s your photo!"
            )
        else:
            await update.message.reply_text("Photo not found on the server!")

    except (IndexError, ValueError):
        await update.message.reply_text(
            "Usage: /set_timer <seconds> (e.g., /set_timer 10)"
        )

# Main function to run the bot
def main():
    TOKEN = "8195540398:AAFbRDBS8N1GCIu8MzWFui_YF-yiAxN6moQ"  # Replace with your Bot's token
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("set_timer", set_timer))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
