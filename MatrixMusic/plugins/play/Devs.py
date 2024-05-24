import asyncio
import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import app
from random import  choice, randint
from config import ASAAQ_ID
def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

@app.on_message(
    command(["المطور","اسحاق","اليسع","مطور السورس","مبرمج السورس"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat(ASAAQ_ID)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"– – – – – – – – – – – – – – – – – –\n↯︙𝖣𝖾𝗏 ↬ ⦗ {name} ⦘\n↯︙𝖴𝗌𝖤𝗋 ↬ ⦗ @{usr.username} ⦘\n↯︙𝖨𝖣 ↬ ⦗ {usr.id} ⦘\n↯︙𝖡𝗂𝖮 ↬ ⦗ {usr.bio} ⦘\n– – – – – – – – – – – – – – – – – –",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    
@app.on_message(
    command(["لبيه"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("My1mind1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"– – – – – – – – – – – – – – – – – –\n↯︙𝖣𝖾𝗏 ↬ ⦗ {name} ⦘\n↯︙𝖴𝗌𝖤𝗋 ↬ ⦗ @{usr.username} ⦘\n↯︙𝖨𝖣 ↬ ⦗ {usr.id} ⦘\n↯︙𝖡𝗂𝖮 ↬ ⦗ {usr.bio} ⦘\n– – – – – – – – – – – – – – – – – –",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    
@app.on_message(
    command(["مطورين","مطورين السورس","المطورين","سورس","السورس"])
  
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5e261225b0770e4888ef7.jpg",
        caption=f"""↯︙اهلا بك عزيزي {message.from_user.mention}\n↯︙مطورين سورس دينا ميوزك""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ : ᯓ ˹ أليسع .↓ : ›", url=f"https://t.me/Mjtre7"), 
                 ],[
                    InlineKeyboardButton(
                        "‹ :ليطمـ𓆰ٰ⍣⃟ٰٰٖٖ۪۬🇾🇪۬ـئن عقلـ۬ۦٕ٘۬ﹻٰ۬ۛۛـي : ›", url=f"https://t.me/My1mind1"),
                ],[
                    InlineKeyboardButton(
                        "‹ : 𝚂𝙾𝚄𝚁𝙲𝙴  : ›", url=f"https://t.me/My1mind1"),
                ],

            ]

        ),

    )

@app.on_message(command(["تخ"]) & filters.group)
async def huhh(client, message):
    to_id = int(ahmed.split("to")[-1].split("in")[0])
    from_id = int(ahmed.split("ahmed")[-1].split("to")[0])
    in_id = int(caption.split("in")[-1])
    to_url = f"tg://openmessage?user_id={to_id}"
    from_url = f"tg://openmessage?user_id={from_id}"
    ahmed = message.text
    await message.reply_animation(
        animation=f"https://telegra.ph/file/5a18fe591860a8a98f39f.mp4",
        caption=f"""↯︙قتل ↫ ⦗ {app.get_chat(to_id).first_name}]({to_url}) ⦘\nالضحيه دا 😢 ↫ ⦗ [{app.get_chat(from_id).first_name}]({from_url}) ⦘\nانا لله وانـا اليـه راجعـون 😢😢""",
    )
    reply_markup=InlineKeyboardMarkup(

       [
           [
               InlineKeyboardButton(
                   "‹ : 𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 : ›", url=f"https://t.me/k_40_x"),
           ],
       ]
    ),
