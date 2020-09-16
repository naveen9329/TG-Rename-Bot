@pyrogram.Client.on_message(pyrogram.Filters.command(["showthumbnail"]))
async def show_thumbnail(bot, update):
    thumb_image_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
    if not os.path.exists(thumb_image_path):
       mes = await get_thumb(update.from_user.id)
       if mes != None:
          m = await bot.get_messages(update.chat.id, mes.msg_id)
          await m.download(file_name=thumb_image_path)
          thumb_image_path = thumb_image_path
    if update.from_user.id in Config.BANNED_USERS:
        await bot.delete_messages(
            chat_id=update.chat.id,
            message_ids=update.message_id,
            revoke=True
        )
        return
    if update.from_user.id not in Config.BANNED_USERS:
       if thumb_image_path is not None:
         await bot.send_photo(chat_id=update.chat.id, photo=thumb_image_path)            
       if thumb_image is None:
         await update.reply_text("No thumbnail found 🤷‍♂️")

