class script(object):
    START_TXT = """<b>👋 Hi .! {}
Add me in a Supergroup and promote me as Admin to let me get in action!</b>"""
    AREA_TXT = """<b>Hey {}
Welcome to Help Area 1 🎁</b>"""
    AREA_TXT2 ="""<b>Hey {}
Welcome to Help Area 3 🎁</b>"""
    HELP_TXT = """<b>Hey {}
Welcome to Help Area 2 🎁</b>"""
    ABOUT_TXT = """<b>
🤖 𝖡ᴏᴛ ɴᴀᴍᴇ : <a href=https://t.me/HerleyfilterBot/>Hᴀʀʟᴇʏ Qᴜɪɴɴ ! </a>

📝 𝖫ᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org/>Pʏᴛᕼᴏɴ</a>

📡 𝖧ᴏsᴛᴇᴅ ᴏɴ : <a href=http://heroku.com/>Hᴇʀᴏᴋᴜ</a>

📃 𝖲ᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href=https://pasty.lus.pm/QZxObR/raw>Cʟʜᴄᴋ ᕼᴇʀᴇ</a>

📚 𝖥ʀᴀᴍᴇᴡᴏʀᴋ : <a href=https://github.com/pyrogram/pyrogram>Pʏʀᴏɢʀᴀᴍ</a>

📊 Dᴀᴛᴀʙᴀsᴇs Sᴀʀᴠᴇʀ : <a href=https://www.mongodb.com/>Mᴏɴɢᴏᴅʙ</a>

👥 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : <a href=https://pasty.lus.pm/QZxObR/raw/>Cʟʜᴄᴋ ᕼᴇʀᴇ</a>

📢 𝖴ᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://pasty.lus.pm/QZxObR/raw/> Cʟʜᴄᴋ ᕼᴇʀᴇ</a> </b>"""
    
    FILE_TXT = """
ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ :

/link - ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇᴅɪᴀ ᴛᴏ ɢᴇᴛ ʟɪɴᴋ

/batch - ᴛᴏ ᴄʀᴇᴀᴛᴇ ʟɪɴᴋ ꜰᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ꜰɪʟᴇꜱ"""
    TEXT1 = """<b>This Is The Module Page Info

🔰 Your Taken Page Is 1/3 📖</b>"""
    TEXT2 = """<b>This Is The Module Page Info

🔰 Your Taken Page Is 2/3 📖</b>"""
    TEXT3 = """<b>This Is The Module Page Info

🔰 Your Taken Page Is 3/3 📖</b>"""
    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
   
 <b>ᴊᴜꜱᴛ ꜱᴏᴍᴇ ᴋɪɴᴅ ᴏꜰ ꜰᴜɴ ᴛʜɪɴɢꜱ</b>

𝟣. /dice - ʀᴏʟᴇ ᴛʜᴇ ᴅɪᴄᴇ 
𝟤. /Throw 𝗈𝗋 /Dart - ᴛᴏ ᴍᴀᴋᴇ ᴅᴀʀᴛ 
3. /Runs - ꜱᴏᴍᴇ ʀᴀɴᴅᴏᴍ ᴅɪᴀʟᴏɢᴜᴇꜱ 
4. /Goal ᴏʀ /Shoot - ᴍᴀᴋᴇ ᴀ ɢᴏᴀʟ ᴏʀ ꜱʜᴏᴏᴛ
5. /luck ᴏʀ /cownd - ꜱᴘɪɴ ᴀɴᴅ ᴛʀʏ ʏᴏᴜʀ ʟᴜᴄᴋ"""
    DEPLOY_TXT = """𝘐𝘢𝘮 𝘈 𝘚𝘪𝘮𝘱𝘭𝘦 𝘈𝘶𝘵𝘰 𝘍𝘪𝘭𝘵𝘦𝘳 + 𝘔𝘢𝘯𝘶𝘢𝘭 𝘍𝘪𝘭𝘵𝘦𝘳 + 𝘌𝘹𝘵𝘳𝘢 𝘍𝘦𝘢𝘵𝘶𝘳𝘦𝘴 𝘉𝘰𝘵. 𝘐 𝘊𝘢𝘯 𝘗𝘳𝘰𝘷𝘪𝘥𝘦 𝘔𝘰𝘷𝘪𝘦𝘴 𝘐𝘯 𝘛𝘦𝘭𝘦𝘨𝘳𝘢𝘮 𝘎𝘳𝘰𝘶𝘱𝘴.𝘐 𝘊𝘢𝘯 𝘈𝘭𝘴𝘰 𝘈𝘥𝘥 𝘍𝘪𝘭𝘵𝘦𝘳𝘴 𝘐𝘯 𝘛𝘦𝘭𝘦𝘨𝘳𝘢𝘮 𝘎𝘳𝘰𝘶𝘱𝘴.  𝘑𝘶𝘴𝘵 𝘈𝘥𝘥 𝘔𝘦 𝘛𝘰 𝘠𝘰𝘶𝘳 𝘎𝘳𝘰𝘶𝘱 𝘈𝘯𝘥 𝘌𝘯𝘫𝘰𝘺"""
    MANUELFILTER_TXT = """
 ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇꜱ:
 /filter - ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ
 /filters - ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ
 /del - ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ
 /delall - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ"""
    INFO_TXT = """<b>🤖Auto Filter + Manual Filter Bot + Somany Of Features ⚡

⚡ WithOut Force Sub ⚡

• Add This Bot To Your Group As Admin And Ask Movies 🔖

• You Can Add Manual Filters Too...✅

• Added File Store : Batch, Normal ✅

• Forcesub Removed ✅

• Files On PM / Files On Bot Channel✅

• Files On PM ✅
 
• Files On Bot Channel ⬇️

• Image Editing ⬇️

•  Fun Games ✅

•  TTS 🎤
 
• Purge ✅

•  Auto Filter On/Off ✅

•  Set Custom IMDB Template ✅

•  Song Download ✅

• 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘠𝘰𝘶𝘵𝘶𝘣𝘦 Video ❎

•  Pin A Message../ 💬

• Paste.../✅

• Youtube Thumbnail ✅

• Sticker ID✅

• 𝖢𝗈𝗏𝗂𝖽 🦠

• AudioBook✅

• URL Shortner✅

• File Store Module✅

•  📂200K +...Still Adding 🔄

Features info  🔰</b>"""
    PIN_TXT ="""
<b>ᴘɪɴ ᴍᴀꜱꜱᴀɢᴇ../</b>

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇꜱ:</b>

◉ /pin :- ᴛᴏ ᴘɪɴ ᴛʜᴇ ᴍᴀꜱꜱᴀɢᴇ ᴏɴ ʏᴏᴜ ᴄʜᴀᴛꜱ
◉ /unpin :- ᴛᴏ ᴜɴᴘɪɴ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘɪɴɴᴇᴅ ᴍᴀꜱꜱᴀɢᴇ"""
    PASTE_TXT = """
ᴘᴀꜱᴛᴇ ꜱᴏᴍᴇ ᴛᴇxᴛꜱ ᴏʀ ᴅᴏᴄᴜᴍᴇɴᴛꜱ ᴏɴ ᴀ ᴡᴇʙꜱɪᴛᴇ!

<b>ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>

• /paste [text] - ᴘᴀꜱᴛᴇ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴘᴀꜱᴛʏ

<b>ɴᴏᴛᴇ:</b>

• ᴛʜᴇꜱᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴡᴏʀᴋꜱ ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• ᴛʜᴇꜱᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""
    TTS_TXT = """
ᴛʀᴀɴꜱʟᴀᴛᴇ ᴛᴇxᴛ ᴛᴏ ꜱᴘᴇᴇᴄʜ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>

• /tts <text> : ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ ꜱᴘᴇᴇᴄʜ

<b>ɴᴏᴛᴇ:</b>

• ɪᴍᴅʙ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• ᴛʜᴇꜱᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴡᴏʀᴋꜱ ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ..
• ɪᴍᴅʙ ᴄᴀɴ ᴛʀᴀɴꜱʟᴀᴛᴇ ᴛᴇxᴛꜱ ᴛᴏ 200+ ʟᴀɴɢᴜᴀɢᴇꜱ."""
    PINGS_TXT ="""
ʜᴇʟᴘꜱ ʏᴏᴜ ᴛᴏ ᴋɴᴏᴡ ʏᴏᴜʀ ᴘɪɴɢ 📡

<b>ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>

 /alive - ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜ ᴀʀᴇ ᴀʟɪᴠᴇ..
 /help - ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ.
 /ping - ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴘɪɴɢ.

ɴᴏᴛᴇ :
• ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅꜱ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ɪɴ ᴘᴍꜱ ᴀɴᴅ ɢʀᴏᴜᴘꜱ
• ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅꜱ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ʙᴜʏ ᴇᴠᴇʀʏᴏɴᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ʙᴏᴛꜱ ᴘᴍ
• ꜱʜᴀʀᴇ ᴜꜱ ꜰᴏʀ ᴍᴏʀᴇ ꜰᴇᴀᴛᴜʀᴇꜱ"""
    TELE_TXT = """
ᴅᴏ ᴀꜱ ʏᴏᴜ ᴡɪꜱʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀ.ᴘʜ ᴍᴏᴅᴜʟᴇ!

</b>ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>

 /telegraph - ꜱᴇɴᴅ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇ ᴜɴᴅᴇʀ (5ᴍʙ)

<b>ɴᴏᴛᴇ:</b>

• ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ɢᴏᴜᴘꜱ ᴀɴᴅ ᴘᴍꜱ
• ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ʙʏ ᴇᴠᴇʀʏᴏɴᴇ"""

    PRIVATEBOT_TXT = """<b>👋 Hi .! {}
Add me in a Supergroup and promote me as Admin to let me get in action!</b>"""

    JSON_TXT ="""
ʙᴏᴛ ʀᴇᴛᴜʀɴꜱ ᴊꜱᴏɴ ꜰᴏʀ ᴀʟʟ ʀᴇᴘʟɪᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪᴛʜ /json

<b>ꜰᴇᴀᴛᴜʀᴇꜱ:</b>

ᴍᴇꜱꜱᴀɢᴇ ᴇᴅɪᴛᴛɪɴɢ ᴊꜱᴏɴ
ᴘᴍ ꜱᴜᴘᴘᴏʀᴛ
ɢʀᴏᴜᴘ ꜱᴜᴘᴘᴏʀᴛ

<b>ɴᴏᴛᴇ:</b>

ᴇᴠᴇʀʏᴏɴᴇ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ , ɪꜰ ꜱᴘᴀᴍɪɴɢ ʜᴀᴘᴘᴇɴꜱ ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʙᴀɴ ʏᴏᴜ ꜰʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ."""
    PURGE_TXT = """
ᴅᴇʟᴇᴛᴇ ᴀ ʟᴏᴛ ᴏꜰ ᴍᴇꜱꜱᴀɢᴇꜱ ꜰʀᴏᴍ ɢʀᴏᴜᴘꜱ! 
    
 <b>ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅ</b> 

/purge :- ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇꜱꜱᴀɢᴇꜱ ꜰʀᴏᴍ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇꜱꜱᴀɢᴇ, ᴛᴏ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴍᴇꜱꜱᴀɢᴇ"""
    
    AUTOFILTER_TXT = """Aᴜᴛᴏ ꜰɪʟᴛᴇʀ ᴏɴ /ᴏꜰꜰ Mᴏᴅᴜʟᴇ  ⚙

ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ɪꜱ ᴛʜᴇ ꜰᴇᴀᴛᴜʀᴇ ᴏꜰ ꜰɪʟᴛᴇʀ ᴀɴᴅ ꜱᴀᴠᴇ ᴛʜᴇ ꜰɪʟᴇꜱ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ꜰʀᴏᴍ ᴄʜᴀɴɴᴇʟ ᴛᴏ ɢʀᴏᴜᴘ.ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜᴇ ꜰᴏʟʟᴏᴡɪɴɢ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴏɴ ᴀɴᴅ ᴏꜰꜰ ᴛʜᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

Cᴏᴍᴍᴀɴᴅs ᴜsᴇ :

/autofilter ᴇɴᴀʙʟᴇ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘꜱ

/autofilter ᴅɪꜱᴀʙʟᴇᴅ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘꜱ"""
    CONNECTION_TXT = """

- ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
- ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.

<b>ɴᴏᴛᴇ:</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ <ᴄᴏᴅᴇ>/ᴄᴏɴɴᴇᴄᴛ ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ᴜʀ ᴘᴍ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
  /connect  - <ᴄᴏᴅᴇ>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ
 /disconnect  - <ᴄᴏᴅᴇ>ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ
 /connections - <ᴄᴏᴅᴇ>ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ"""
    EXTRAMOD_TXT = """
<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /id - <ᴄᴏᴅᴇ>ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰᴇᴅ ᴜꜱᴇʀ.
• /info  - <ᴄᴏᴅᴇ>ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.
• /imdb  - <ᴄᴏᴅᴇ>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.
• /search  - <ᴄᴏᴅᴇ>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ."""
    ADMIN_TXT = """

ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴏɴʟʏ ᴡᴏʀᴋꜱ ꜰᴏʀ ᴍʏ ᴀᴅᴍɪɴꜱ

 ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:
• /ʟᴏɢꜱ - <ᴄᴏᴅᴇ>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇꜱᴄᴇɴᴛ ᴇʀʀᴏʀꜱ
• /ꜱᴛᴀᴛꜱ - <ᴄᴏᴅᴇ>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ.
• /ᴅᴇʟᴇᴛᴇ - <ᴄᴏᴅᴇ>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.
• /ᴜꜱᴇʀꜱ - <ᴄᴏᴅᴇ>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.
• /ᴄʜᴀᴛꜱ - <ᴄᴏᴅᴇ>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛʜᴇ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ 
• /ʟᴇᴀᴠᴇ  - <ᴄᴏᴅᴇ>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.
• /ᴅɪꜱᴀʙʟᴇ  -  <ᴄᴏᴅᴇ>ᴅᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.
• /ʙᴀɴ_ᴜꜱᴇʀ  - <ᴄᴏᴅᴇ>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.
• /ᴜɴʙᴀɴ_ᴜꜱᴇʀ  - <ᴄᴏᴅᴇ>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.
• /ᴄʜᴀɴɴᴇʟ - <ᴄᴏᴅᴇ>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ
• /ʙʀᴏᴀᴅᴄᴀꜱᴛ - <ᴄᴏᴅᴇ>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ"""
    STATUS_TXT = """
 <b>📑 ғɪʟᴇs sᴀᴠᴇᴅ : <code>{}</code></b>
 <b>👩🏻‍💻 ᴜsᴇʀs: <code>{}</code></b>
 <b>👥 ɢʀᴏᴜᴘs: <code>{}</code></b>
 <b>🗂️ ᴏᴄᴄᴜᴘɪᴇᴅ: <code>{}</code> 𝙼𝙱</b>"""
    LOG_TEXT_G = """#ɴᴇᴡɢʀᴏᴜᴘ
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
"""
    LOG_TEXT_P = """#NewSub
    
<b>🆔 User ID - <code>{}</code></b>
<b>👤 User - {}</b>"""
    
    URLSHORT_TXT = """
ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘꜱ ʏᴏᴜ ᴛᴏ ꜱʜᴏʀᴛ ᴀ ᴜʀʟ

ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ:

/short: 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌

𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
/short ᴘᴀꜱᴛ ʏᴏᴜʀ ᴜʀʟ"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
•/whois :-give a user full details"""
    VIDEO_TXT ="""
ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ

• ᴜꜱᴀɢᴇ: 
ʏᴏᴜ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴠɪᴅᴇᴏ ꜰᴏʀᴍ ʏᴏᴜᴛᴜʙᴇ

ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ:

/video https://youtu.be/kB9TkCs8cX0"""

    ZOMBIES_TXT = """ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴋɪᴄᴋ ᴜꜱᴇʀ

ᴋɪᴄᴋ ɪɴᴄᴀᴛɪᴠᴇ ᴍᴇᴍʙᴇʀꜱ ꜰʀᴏᴍ ɢʀᴏᴜᴘ. ᴀᴅᴅ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴ ᴡɪᴛʜ ʙᴀɴ ᴜꜱᴇʀꜱ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ɪɴ ɢʀᴏᴜᴘ.

ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:
• /ɪɴᴋɪᴄᴋ - ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ʀᴇQᴜɪʀᴇᴅ ᴀʀɢᴜᴍᴇɴᴛꜱ ᴀɴᴅ ɪ ᴡɪʟʟ ᴋɪᴄᴋ ᴍᴇᴍʙᴇʀꜱ ꜰʀᴏᴍ ɢʀᴏᴜᴘ.
• /ɪɴꜱᴛᴀᴛᴜꜱ - ᴛᴏ ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀ ꜰʀᴏᴍ ɢʀᴏᴜᴘ.
• /ɪɴᴋɪᴄᴋ ᴡɪᴛʜɪɴ_ᴍᴏɴᴛʜ ʟᴏɴɢ_ᴛɪᴍᴇ_ᴀɢᴏ - ᴛᴏ ᴋɪᴄᴋ ᴜꜱᴇʀꜱ ᴡʜᴏ ᴀʀᴇ ᴏꜰꜰʟɪɴᴇ ꜰᴏʀ ᴍᴏʀᴇ ᴛʜᴀɴ 6-7 ᴅᴀʏꜱ.
• /ɪɴᴋɪᴄᴋ ʟᴏɴɢ_ᴛɪᴍᴇ_ᴀɢᴏ - ᴛᴏ ᴋɪᴄᴋ ᴍᴇᴍʙᴇʀꜱ ᴡʜᴏ ᴀʀᴇ ᴏꜰꜰʟɪɴᴇ ꜰᴏʀ ᴍᴏʀᴇ ᴛʜᴀɴ ᴀ ᴍᴏɴᴛʜ ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛꜱ.
• /ᴅᴋɪᴄᴋ - ᴛᴏ ᴋɪᴄᴋ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛꜱ."""

    IMAGE_TXT = """

ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘꜱ ʏᴏᴜ ᴛᴏ ᴇᴅɪᴛ ɪᴍɢ ᴠᴇʀʏ ᴇᴀꜱɪʟʏ 

ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ:

 𝖩𝗎𝗌𝗍 𝗌𝖾𝗇𝖽 𝗆𝖾 𝖺 𝗂𝗆𝖺𝗀𝖾 𝗍𝗈 𝖾𝖽𝗂𝗍 ✨"""

    STICKER_TXT = """ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴛᴏ ꜰɪɴᴅ ᴀɴʏ ꜱᴛɪᴄᴋᴇʀ ɪᴅ.

 
ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ:
 
◉ Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """ʜᴇʟᴘꜱ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴛʜᴜᴍʙɴᴀɪʟ
    
ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ:

/ytthumb ᴘᴀꜱᴛᴇ ᴀɴʏ ᴠɪᴅᴇᴏ ᴜʀʟ"""

    ABOOK_TXT = """

ʏᴏᴜ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ᴀ ᴘᴅꜰ ꜰɪʟᴇ ᴛᴏ ᴀ ᴀᴜᴅɪᴏ ꜰɪʟᴇ ᴡɪᴛʜ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ

ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ:

 /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    GTRANS_TXT = """
ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘꜱ ʏᴏᴜ ᴛᴏ ᴛʀᴀɴꜱʟᴀᴛᴇ ᴀ ᴛᴇxᴛ ᴛᴏ ᴀɴʏ ʟᴀɴɢᴜᴀɢᴇ ʏᴏᴜ ᴡᴀɴᴛ

ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ:

/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾

𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾

𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    RESTRIC_TXT = """

ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴀ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜꜱᴇ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴛʜᴇɪʀ ɢʀᴏᴜᴘ ᴍᴏʀᴇ ᴇꜰꜰɪᴄɪᴇɴᴛʟʏ.

/ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
/unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
/tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
/mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
/unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
/tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌"""
    SONG_TXT = """🔰  Song Download Module  🔰

Song Download Module, For Those Who Love Music. You Can Use This Feature For Download Any Song With Suoer Fast Speed...🚀

Commands
/song Song Name"""
    CREATOR_REQUIRED = """❗<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """Add Me Again with all admin rights.</b>"""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ഇപ്പൊ എല്ലാം അടിച്ചുമാറ്റി തരാം...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>"""
