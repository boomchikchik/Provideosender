#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, PersonId
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={PersonId}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://www.gooogle.com'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://www.gooogle.com'>Click Here</a>\n○ Channel : @bot_list_hub\n○ Support Group : @botlistdisc</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
