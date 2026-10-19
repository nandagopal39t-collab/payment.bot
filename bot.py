import asyncio
import logging

from telegram import (
    BotCommand,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.error import TelegramError
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


TOKEN = "8931401709:AAHrbS2vSvmHLKBQLwa9YfGokBxNIHCs_zE"
ADMIN_ID = 8630635305


async def set_commands(app):
    commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("groups", "View premium groups"),
        BotCommand("demo", "View demo content"),
    ]
    await app.bot.set_my_commands(commands)


# AUTO DELETE
async def auto_delete(message):
    await asyncio.sleep(180)

    try:
        await message.delete()
    except TelegramError:
        logger.exception("Failed to auto-delete message_id=%s chat_id=%s", message.message_id, message.chat_id)


# GROUP DATA
GROUPS = {
    "g1": {
        "name": "𝗪𝗲𝗯𝗰𝗮𝗺 🎥",
        "price": "₹99",
        "chat_id": -1002774622402,
    },
    "g2": {
        "name": "𝗥𝗲𝘀𝗺𝗶 𝗼𝗻𝗹𝘆 😋",
        "price": "₹100",
        "chat_id": -1003214334957,    
    },
    "g3": {
        "name": "𝐑𝐞𝐝 𝐋𝐢𝐠𝐡𝐭 𝗔𝗿𝗲𝗮🚨",
        "price": "₹100",
        "chat_id": -1004297303025,
    },
    "g4": {
        "name": "𝗕𝗹𝗼𝘄𝗷𝗼𝗯 🍌 ",
        "price": "₹100",
        "chat_id": -1003537454192,
    },
    "g5": {
        "name": "𝗞𝗼𝗼𝗹𝘂𝗺𝘂𝘁𝘁𝗮𝘆𝗶 🍭 ",
        "price": "₹149",
        "chat_id": -1003907780060,
    },
    "g6": {
        "name": "𝗠𝘂𝘀𝗹𝗶𝗺 𝗵𝘂𝗯🌺 ",
        "price": "₹150",
        "chat_id": -1003689413427,
    },
    "g7": {
        "name": "𝗧𝗮𝗺𝗶𝗹 𝗼𝗻𝗹𝘆 🌷",
        "price": "₹160",
        "chat_id": -1003172988753,
    },
    "g8": {
        "name": "𝗥𝗲𝗮𝗹 𝘀𝗽𝘆📸",
        "price": "₹200",
        "chat_id": -1003802511334,
    },
    "g9": {
        "name": "𝗦𝗻𝗮𝗽𝗰𝗵𝗮𝘁👻",
        "price": "₹239",
        "chat_id": -1003919279614,
    },
    "g10": {
        "name": "🌴കേരള's 𝗹𝗮𝘁𝗲𝘀𝘁🤤 ",
        "price": "₹249",
        "chat_id": -1004486646514,
    },
    "g11": {
        "name": "𝗘𝘅𝗰𝗹𝘂𝘀𝗶𝘃𝗲 𝗰𝗼𝗻𝘁𝗲𝗻𝘁🌸🔞",
        "price": "₹250",
        "chat_id": -1003906717077,
    },
    "g12": {
        "name": "𝗔𝗹𝗹 𝗟𝗲𝗮𝗸 𝗖𝗼𝗹𝗹𝗲𝗰𝘁𝗶𝗼𝗻💎🍒",
        "price": "₹549",
        "link": "https://t.me/m/eJh5roTINjM1",
      },
    "g13": {
        "name": "40 𝗚𝗥𝗢𝗨𝗣𝗦📈💋",
        "price": "₹599",
        "link": "https://t.me/m/eJh5roTINjM1",
    },
}
# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🌸 View Groups", callback_data="groups")],
        [InlineKeyboardButton("🎬 Demo", callback_data="demo")],
        [
            InlineKeyboardButton(
                "📖 How To Buy",
                url="https://t.me/Keralaslatestbot?start=Z2V0Oi0xMDAzMzgxNTg5NzE0OjMzMg",
            )
        ],
        [
            InlineKeyboardButton(
                "📩 Contact Admin",
                url="https://t.me/MuskanKariaAssistant_bot?text=Hello%20%F0%9F%91%8B%F0%9F%8F%BB",
            )
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    msg = await update.message.reply_text(
        "🌴𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 𝗧𝗲𝗮𝗺 മുലച്ചിപ്പെണ്ണ് 🦋",
        reply_markup=reply_markup,
    )

    asyncio.create_task(auto_delete(msg))


# BUTTONS
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # GROUPS
    if query.data == "groups":
        keyboard = []

        for key, value in GROUPS.items():
            keyboard.append(
                [
                    InlineKeyboardButton(
                        f"{value['name']} - {value['price']}",
                        callback_data=f"buy_{key}",
                    )
                ]
            )

        reply_markup = InlineKeyboardMarkup(keyboard)

        msg = await query.message.reply_text(
            "💎 Select Your Group",
            reply_markup=reply_markup,
        )

        asyncio.create_task(auto_delete(msg))

    # DEMO
    elif query.data == "demo":
        keyboard = [
            [
                InlineKeyboardButton(
                    "🎬 Open Demo Collection",
                    url="https://t.me/TeamKeralasV2Bot?start=Z2V0Oi0xMDAzOTE2MzgxMTAzOjU5Ojc1",
                )
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        msg = await query.message.reply_text(
            "🔥 Click below to view latest demo collection",
            reply_markup=reply_markup,
        )

        asyncio.create_task(auto_delete(msg))

    # BUY
    elif query.data.startswith("buy_"):
        group_key = query.data.replace("buy_", "", 1)
        group = GROUPS.get(group_key)
        if not group:
            logger.error("Unknown group_key=%s from user_id=%s", group_key, query.from_user.id)
            await query.message.reply_text("❌ Unknown group selected. Please try again.")
            return

        context.user_data["selected_group"] = group_key

        keyboard = [[InlineKeyboardButton("✅ Payment Done", callback_data="paid")]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        with open("qr.jpg", "rb") as qr_file:
            msg = await query.message.reply_photo(
                photo=qr_file,
                caption=(
                    f"💰 {group['name']}\n"
                    f"Price: {group['price']}\n\n"
                    "📸 After payment click Payment Done"
                ),
                reply_markup=reply_markup,
            )

        asyncio.create_task(auto_delete(msg))

    # PAYMENT DONE
    elif query.data == "paid":
        if "selected_group" not in context.user_data:
            logger.warning("Payment clicked without selected group user_id=%s", query.from_user.id)
            await query.message.reply_text("❌ Please select a group first.")
            return

        msg = await query.message.reply_text("📸 Please upload payment screenshot")

        asyncio.create_task(auto_delete(msg))

        context.user_data["waiting_payment"] = True


# PAYMENT SCREENSHOT
async def payment_screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("waiting_payment"):
        return

    group_key = context.user_data.get("selected_group")
    group = GROUPS.get(group_key)
    if not group:
        logger.error("Screenshot received with invalid group_key=%s user_id=%s", group_key, update.effective_user.id)
        await update.message.reply_text("❌ Group selection expired. Please select the group again.")
        context.user_data["waiting_payment"] = False
        return

    photo = update.message.photo[-1]
    user = update.effective_user
    target_chat_id = group.get("chat_id", "external-link")

    keyboard = [
        [
            InlineKeyboardButton(
                "✅ Approve",
                callback_data=f"approve_{user.id}_{group_key}",
            ),
            InlineKeyboardButton(
                "❌ Reject",
                callback_data=f"reject_{user.id}_{group_key}",
            ),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    logger.info(
        "Payment request user_id=%s username=%s group_key=%s target_chat_id=%s",
        user.id,
        user.username,
        group_key,
        target_chat_id,
    )

    # SEND TO ADMIN
    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=photo.file_id,
        caption=(
            "🔥 New Payment Request\n\n"
            f"User: @{user.username or 'no_username'}\n"
            f"User ID: {user.id}\n"
            f"Target Chat ID: {target_chat_id}\n"
            f"Group: {group['name']}\n"
            f"Price: {group['price']}"
        ),
        reply_markup=reply_markup,
    )

    msg = await update.message.reply_text("⏳𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭 𝐩𝐚𝐭𝐢𝐞𝐧𝐭𝐥𝐲 𝐲𝐨𝐮𝐫 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐚𝐩𝐩𝐫𝐨𝐯𝐞𝐝 𝐬𝐨𝐨𝐧💯")

    asyncio.create_task(auto_delete(msg))

    context.user_data["waiting_payment"] = False


async def notify_admin_of_approval_error(context, query, user_id, group_key, group, error):
    target_chat_id = group.get("chat_id", "external-link") if group else "unknown"
    error_text = f"{type(error).__name__}: {error}"
    logger.exception(
        "Approval failed admin_id=%s user_id=%s group_key=%s target_chat_id=%s",
        query.from_user.id,
        user_id,
        group_key,
        target_chat_id,
    )
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=(
            "❌ Approval Error\n\n"
            f"Admin ID: {query.from_user.id}\n"
            f"User ID: {user_id}\n"
            f"Group Key: {group_key}\n"
            f"Target Chat ID: {target_chat_id}\n"
            f"Error: {error_text}"
        ),
    )


# APPROVE / REJECT
async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer("Processing...")

    # APPROVE
    if query.data.startswith("approve_"):
        _, user_id_text, group_key = query.data.split("_", 2)
        user_id = int(user_id_text)
        group = GROUPS.get(group_key)
        if not group:
            await query.answer("Unknown group.", show_alert=True)
            logger.error("Unknown approval group_key=%s admin_id=%s user_id=%s", group_key, query.from_user.id, user_id)
            return

        target_chat_id = group.get("chat_id", "external-link")
        logger.info(
            "Approval clicked admin_id=%s user_id=%s group_key=%s target_chat_id=%s",
            query.from_user.id,
            user_id,
            group_key,
            target_chat_id,
        )

        try:
            if "chat_id" in group:
                invite = await context.bot.create_chat_invite_link(
                    chat_id=group["chat_id"],
                    member_limit=1,
                )

                join_link = invite.invite_link

            else:
                join_link = group["link"]

            msg = await context.bot.send_message(
                chat_id=user_id,
                text=(
                    "✅ Payment Approved\n\n"
                    f"🔥 {group['name']}\n\n"
                    "🔗 Your Private Link:\n"
                    f"{join_link}\n\n"
                    "🎁 𝗙𝗿𝗲𝗲 𝗙𝗼𝗿𝗲𝗶𝗴𝗻 𝗚𝗿𝗼𝘂𝗽:\n"
                    "https://t.me/+CzoS2chB3FgyYTY1\n\n"
                    "⚠️ One-time use only\n\n"
                ),
            )

            await query.edit_message_caption(
                caption=(
                    "✅ Payment Approved\n\n"
                    f"User ID: {user_id}\n"
                    f"Target Chat ID: {target_chat_id}\n"
                    f"Group: {group['name']}"
                )
            )
        except TelegramError as error:
            await notify_admin_of_approval_error(context, query, user_id, group_key, group, error)

    elif query.data.startswith("reject_"):
        parts = query.data.split("_", 2)
        user_id = int(parts[1])
        group_key = parts[2] if len(parts) > 2 else "unknown"
        group = GROUPS.get(group_key)
        target_chat_id = group.get("chat_id", "external-link") if group else "unknown"

        try:
            msg = await context.bot.send_message(
                chat_id=user_id,
                text=(
                    "❌ Payment Rejected\n\n"
                    "Please send valid screenshot."
                ),
            )

            asyncio.create_task(auto_delete(msg))

            await query.edit_message_caption(
                caption=(
                    "❌ Payment Rejected\n\n"
                    f"User ID: {user_id}\n"
                    f"Target Chat ID: {target_chat_id}"
                )
            )
        except TelegramError as error:
            logger.exception(
                "Reject failed admin_id=%s user_id=%s group_key=%s target_chat_id=%s",
                query.from_user.id,
                user_id,
                group_key,
                target_chat_id,
            )
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=(
                    "❌ Reject Error\n\n"
                    f"Admin ID: {query.from_user.id}\n"
                    f"User ID: {user_id}\n"
                    f"Group Key: {group_key}\n"
                    f"Target Chat ID: {target_chat_id}\n"
                    f"Error: {type(error).__name__}: {error}"
                ),
            )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    user_id = None
    chat_id = None
    callback_data = None

    if isinstance(update, Update):
        if update.effective_user:
            user_id = update.effective_user.id
        if update.effective_chat:
            chat_id = update.effective_chat.id
        if update.callback_query:
            callback_data = update.callback_query.data

    logger.exception(
        "Unhandled error user_id=%s chat_id=%s callback_data=%s",
        user_id,
        chat_id,
        callback_data,
        exc_info=context.error,
    )

    try:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=(
                "❌ Bot Error\n\n"
                f"User ID: {user_id}\n"
                f"Chat ID: {chat_id}\n"
                f"Callback: {callback_data}\n"
                f"Error: {type(context.error).__name__}: {context.error}"
            ),
        )
    except TelegramError:
        logger.exception("Failed to notify admin about unhandled error")


def build_app():
    app = ApplicationBuilder().token(TOKEN).post_init(set_commands).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(approve, pattern="^(approve_|reject_)"))
    app.add_handler(CallbackQueryHandler(buttons))
    app.add_handler(MessageHandler(filters.PHOTO, payment_screenshot))
    app.add_error_handler(error_handler)

    return app


if __name__ == "__main__":
    logger.info("Bot Running...")
    build_app().run_polling()
