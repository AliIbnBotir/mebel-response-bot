import logging

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from config import BOT_TOKEN, GROUP_ID
from handlers.message_handler import handle_mebelchi_command, handle_reply_to_admin

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

    print("Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
