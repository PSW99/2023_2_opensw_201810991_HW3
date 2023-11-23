import asyncio
import platform
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def set_event_loop_policy():
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def main():
    bot_token = "???"

    set_event_loop_policy()

    # Build the application
    application = Application.builder().token(bot_token).build()

    # Set up handlers
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(message_handler)

    # Start polling
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
