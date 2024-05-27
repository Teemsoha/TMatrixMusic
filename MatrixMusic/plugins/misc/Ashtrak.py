from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant
from MatrixMusic import app
import config

channel = config.CHANNEL_LINK
Nem = config.BOT_NAME + " شغل"
async def subscription(_, __: Client, message: Message):
    user_id = message.from_user.id
    try: 
        await app.get_chat_member(channel, user_id)
    except UserNotParticipant: 
        return False
    return True
    
subscribed = filters.create(subscription)

# تعريف دالة لمعالجة الأوامر
@app.on_message(filters.command(["تشغيل", "شغل",Nem],"") & ~subscribed)
async def command_handler(_: Client, message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        user_id = message.from_user.id
        user = message.from_user.first_name
        markup = Markup([
            [Button(config.CHANNEL_NAME, url=f"https://t.me/{channel}")],
            [Button(text="الذكاء الاصطناعي", url="https://youtube.com/@nexpo01?si=wnNwUUoCgL3gl8V5}")],
        ])
        await message.reply(
            f"◇ عذرًا عزيزي {user} ، عليك الاشتراك في قنوات البوت أولاً.",
            reply_markup=markup
        )
        
