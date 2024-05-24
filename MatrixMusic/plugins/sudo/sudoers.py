from MatrixMusic.plugins.play.filters import command
from pyrogram import filters
from pyrogram.types import Message

from MatrixMusic import app
from MatrixMusic.misc import SUDOERS
from MatrixMusic.utils.database import add_sudo, remove_sudo
from MatrixMusic.utils.decorators.language import language
from MatrixMusic.utils.extraction import extract_user
from MatrixMusic.utils.inline import close_markup
from config import BANNED_USERS, OWNER_ID


@app.on_message(command(["/addsudo", "رفع مطور", "/رفع مطور"]) & filters.user(OWNER_ID))
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id in SUDOERS:
        return await message.reply_text(_["sudo_1"].format(user.mention))
    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(_["sudo_2"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(command(["/delsudo", "تنزيل مطور", "/تنزيل مطور"]) & filters.user(OWNER_ID))
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id not in SUDOERS:
        return await message.reply_text(_["sudo_3"].format(user.mention))
    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(_["sudo_4"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])
