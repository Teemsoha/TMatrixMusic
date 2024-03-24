import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import *
from MatrixMusic import app

@app.on_message(filters.video_chat_started)
async def brah(client, message):
       await message.reply("<b>❆︙تم تشغيل ↫ ⦗ المحادثة المرئية ⦘</b>")
@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
       await message.reply("<b>❆︙تم ايقاف ↫ ⦗ المحادثة المرئية ⦘</b>")
@app.on_message(filters.video_chat_members_invited)
async def fuckoff(client, message):
           text = f"<b>❆︙قام الشخص ↫</b> ⦗ {message.from_user.mention} ⦘"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"\n<b>❆︙بدعوة شخص الى المحادثة المرئية </b> ⦗ {user.first_name} ⦘"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass  
