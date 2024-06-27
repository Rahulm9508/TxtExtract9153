import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import pyrogram
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
import time
from pyrogram.types import User, Message
from p_bar import progress_bar
from subprocess import getstatusoutput
import logging
import os
import sys
import re
from pyrogram import Client as bot
import time



@bot.on_message(filters.command(["khan"]))
async def khann(bot: Client, m: Message):
    if not one(m.from_user.id):
        return await m.reply_text(
            "✨ Hello Sir,\n\n• This Bot is paid\n• Click Below To Buy",
            reply_markup=keyboard,
        )
    editable = await m.reply_text(
        "➭ 𝗜 𝗔𝗺 𝗔𝗻 𝗞𝗛𝗔𝗡 𝗦𝗜𝗥 𝗘𝘅𝘁𝗿𝗮𝗰𝘁𝗼𝗿 𝗕𝗼𝘁. 𝗧𝗼 𝗨𝘀𝗲 𝗠𝗲 𝗦𝗲𝗻𝗱 𝗬𝗼𝘂𝗿 𝗔𝗨𝗧𝗛 𝗖𝗢𝗗𝗘 𝗜𝗻 𝗥𝗲𝗽𝗹𝘆 𝗧𝗼 𝗧𝗵𝗶𝘀 𝗠𝗲𝘀𝘀𝗮𝗴𝗲.\n\n➭ 𝗦𝗲𝗻𝗱 𝗔𝗨𝗧𝗛 𝗖𝗢𝗗𝗘 𝗜𝗻 𝗧𝗵𝗶𝘀 𝗠𝗮𝗻𝗻𝗲𝗿 𝗢𝘁𝗵𝗲𝗿𝘄𝗶𝘀𝗲 𝗕𝗼𝘁 𝗪𝗶𝗹𝗹 𝗡𝗼𝘁 𝗥𝗲𝘀𝗽𝗼𝗻𝗱\n➭ 𝗦𝗲𝗻𝗱 𝗟𝗶𝗸𝘀 𝗧𝗵𝗶𝘀:- 𝗔𝗨𝗧𝗛 𝗖𝗢𝗗𝗘"
    )
    input1: Message = await bot.listen(editable.chat.id)
    token = input1.text
    headers = {
        "Host": "admin2.khanglobalstudies.com",
        "authorization": f"Bearer {token}",
        "client-id": "5f439b64d553cc02d283e1b4",
        "client-version": "21.0",
        "user-agent": "Android",
        "randomid": "385bc0ce778e8d0b",
        "client-type": "MOBILE",
        "device-meta": "{APP_VERSION:19.0,DEVICE_MAKE:Asus,DEVICE_MODEL:ASUS_X00TD,OS_VERSION:6,PACKAGE_NAME:xyz.penpencil.khansirofficial}",
        "content-type": "application/json; charset=UTF-8",
    }
    params = {
        "mode": "2",
        "filter": "false",
        "exam": "",
        "amount": "",
        "organisationId": "5f439b64d553cc02d283e1b4",
        "classes": "",
        "limit": "20",
        "page": "1",
        "programId": "5f476e70a64b4a00ddd81379",
        "ut": "1652675230446",
    }
    response = requests.get(
        "https://admin2.khanglobalstudies.com/api/user/v2/courses?medium=0",
        params=params,
        headers=headers,
    ).json()
    aa = ""
    for data in response:
        batch_name = data["title"]
        batch_id = data["id"]
        aa = aa + f"**{batch_name}**  :  `{batch_id}`\n\n"
    await m.reply_text(aa)

    await m.reply_text("**Now send the Batch ID to Download**")
    input1 = message = await bot.listen(editable.chat.id)
    batch_ids = input1.text

    response2 = requests.get(
        f"https://admin2.khanglobalstudies.com/api/user/courses/{batch_id}/lessons?medium=0",
        headers=headers,
    ).json()["lessons"]
    to_write = ""
    for data in response2:
        batch_names = data["videos"]
        for vish in batch_names:
            vids = vish["video_url"]
            name = vish["name"]
            write = f"{name}:{vids}\n"
            to_write += write
    with open(f"{batch_ids}.txt", "w", encoding="utf-8") as f:
        f.write(to_write)
        print(1)
    with open(f"{batch_ids}.txt", "rb") as f:
        await asyncio.sleep(5)
        doc = await message.reply_document(document=f, caption="Here is your txt file.")
