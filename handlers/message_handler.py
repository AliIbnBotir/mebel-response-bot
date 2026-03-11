from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_IDS
from handlers.keyword_rules import get_reply

NO_MATCH_TEXT = (
    "Kechirasiz, bu savol bo'yicha ma'lumot topilmadi.\n"
    "Iltimos, menejer bilan bog'laning: @manager_username"
)


async def handle_reply_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Fires when someone replies to an admin/owner's message."""
    message = update.message
    if not message or not message.reply_to_message:
        return

    replied_to = message.reply_to_message.from_user
    if not replied_to or replied_to.id not in ADMIN_IDS:
        return

    reply = get_reply(message.text or "")
    if reply:
        await message.reply_text(reply)


async def handle_mebelchi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Fires when someone uses the /mebelchi command."""
    message = update.message
    if not message:
        return

    # /mebelchi narx  →  search "narx" in rules
    query = " ".join(context.args) if context.args else ""

    if query:
        reply = get_reply(query)
        await message.reply_text(reply or NO_MATCH_TEXT)
    else:
        await message.reply_text(
            "Salom! Quyidagi mavzularda yordam bera olaman:\n\n"
            "• narx / price\n"
            "• yetkazib berish / delivery\n"
            "• ish vaqti / hours\n"
            "• manzil / address\n"
            "• garantiya / warranty\n"
            "• chegirma / discount\n\n"
            "Misol: /mebelchi narx"
        )
