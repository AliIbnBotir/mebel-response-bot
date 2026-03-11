import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from config import BOT_TOKEN, GROUP_ID
from handlers.message_handler import handle_mebelchi_command, handle_reply_to_admin

logger = logging.getLogger(__name__)


async def debug_all(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message
    if msg:
        logger.info("DEBUG | chat_id=%s | from=%s | is_reply=%s | text=%r",
                    msg.chat.id, msg.from_user.id if msg.from_user else None,
                    bool(msg.reply_to_message), msg.text)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    group_only = filters.Chat(GROUP_ID)

    # /mebelchi command
    app.add_handler(CommandHandler("mebelchi", handle_mebelchi_command, filters=group_only))

    # Reply to admin/owner message
    app.add_handler(
        MessageHandler(group_only & filters.TEXT & filters.REPLY, handle_reply_to_admin)
    )

    # Temporary: log ALL messages to find correct chat_id
    app.add_handler(MessageHandler(filters.ALL, debug_all), group=1)

    print("Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
