class Translation(object):
    START_TEXT = """Hello,
This is a telegram file to streamable video converter bot

You can convert any Telegram Document, using this bot! With custom thumbnail

Created by <a href='https://t.me/anonymous9329'>My Father 👨‍💻</a>
    """
text = PM_START_TEXT

    keyboard = [[InlineKeyboardButton(text="🤝Help",callback_data="help_back"),InlineKeyboardButton(text="🛡Creator🛡",url="https://t.me/TheUnusualPsychopath")]]
    keyboard += [[InlineKeyboardButton(text="🌐Connect Group", callback_data="main_connect"),InlineKeyboardButton(text="⚜️Add Me⚜️",url="t.me/{}?startgroup=true".format(bot.username))]]

    update.effective_message.reply_photo(img, PM_START_TEXT.format(escape_markdown(first_name), escape_markdown(bot.first_name), OWNER_NAME, OWNER_ID), 
                                         reply_markup=InlineKeyboardMarkup(keyboard), disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)

    ABS_TEXT = " Please don't be selfish."
    BANNED_USER_TEXT = "you are banned 🚫. Because you misused me. Please as my boss @anonymous9329 in the <a href='https://t.me/anonymousbotsupporte'>Discussion group 🗣</a>.Don't pm him"
    UPGRADE_TEXT = "No upgrade plan 🥰. You are free for now"
    DOWNLOAD_START = "trying to download to my server....📥"
    UPLOAD_START = "Started to convert as Video 📹"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Please join the <a href='https://t.me/anonymousbotsupporte'>Discussion group 🗣</a>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \nPlease rate me if you find me useful. https://t.me/tlgrmcbot?start=anydl_bot-bot \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    SAVED_CUSTOM_THUMB_NAIL = "✅ Custom video or file thumbnail saved. This image will be used in next 24 hr. Now enjoy the bot 🤖 with you thumbnail"
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = ""
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found.😔"
    CURENT_PLAN_DETAILS = """There is no plan till now you are free to use me 🤩"""
    HELP_USER = """Hi there. I can convert telegram file to video
How to use me :

Step-1👉 Forward the file which you wanted to convert as streamable video 

Step-2👉Reply to the message as /converttovideo.
(Long press on the file which you need to convert and check the left bottom you can find reply button)

Thanks to @TGBotsz, @InFoTelGroup 

special thanks to @viruZs and @TheUnusualPsychopath



<b>I am created by <a href='https://t.me/anonymous9329'>My Father 👨‍💻</a>
Discuss with us in <a href='https://t.me/anonymousbotsupporte'>Discussion group 🗣</a></b>
"""

    REPLY_TO_DOC_FOR_C2V = "🤦‍♂️ Reply to a Telegram media to convert.Don't you know how to reply please check /help"
