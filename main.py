ADMIN_ID = 8528241842 
 
# যদি কেউ লিংক ছাড়া সাধারণ স্টার্ট দেয় এবং সে যদি অ্যাডমিন না হয়, তবে আটকে দিবে
if (not params or params == "None") and message.from_user.id != ADMIN_ID:
    pass  # সাধারণ ইউজার হলে বট কোনো উত্তর দেবে না
else:
    # অ্যাডমিন অথবা যারা লিংক দিয়ে প্রবেশ করেছে তাদের জন্য নিচের কোড কাজ করবে
    if not params or params == "None":
        bot.sendMessage(
            text=(
                "<b>📤 Welcome to Multi File Sharing Bot!</b>\n\n"
                "With this bot, you can:\n"
                "• Upload <b>multiple photos, videos, documents, stickers, audios, voices, animations</b>.\n"
                "• Get a <b>unique shareable link</b> for your uploaded files.\n"
                "• Share that link anywhere, and anyone can open it to view/download your files.\n\n"
                "⚡ <b>How to use:</b>\n"
                "1. Type <code>/upload</code> to start an upload session.\n"
                "2. Send all your media files one by one.\n"
                "3. When finished, type ✅ to confirm upload.\n"
                "4. You will get a shareable link to your uploaded files.\n\n"
                "⏳ Files shared in chat are <b>auto-deleted after 30 minutes</b> to prevent spam.\n"
                "But don’t worry — you can always restore them using the shareable link.\n\n"
                "🚀 Start sharing your files now!"
            ),
            parse_mode="html",
            reply_markup={
                "inline_keyboard": [[
                    {"text": "📤 Start Uploading", "callback_data": "/upload"}
                ]]
            }
        )
    else:
        media_id = params
        files = Bot.getData(media_id)

        if not files:
            bot.sendMessage("❌ No media found for this link.")
        else:
            sent_msgs = []  # store message IDs for later deletion

            # Send all media
            for f in files:
                m = None
                if f["type"] == "photo":
                    m = bot.sendPhoto(f["file_id"], caption=f.get("caption", ""))
                elif f["type"] == "video":
                    m = bot.sendVideo(f["file_id"], caption=f.get("caption", ""))
                elif f["type"] == "audio":
                    m = bot.sendAudio(f["file_id"])
                elif f["type"] == "voice":
                    m = bot.sendVoice(f["file_id"])
                elif f["type"] == "document":
                    m = bot.sendDocument(f["file_id"])
                elif f["type"] == "animation":
                    m = bot.sendAnimation(f["file_id"])
                elif f["type"] == "sticker":
                    m = bot.sendSticker(f["file_id"])

                if m and "message_id" in m:
                    sent_msgs.append(m["message_id"])

            # Final note
            note = bot.sendMessage(
                "⚠️ <b>Note:</b> Files will be automatically deleted from chat after <b>30 minutes</b> to prevent spam.",
                parse_mode="html",
                reply_markup={
                    "inline_keyboard": [[
                        {"text": "🔗 Join Channel", "url": "https://t.me/+T3n5y7jU08IwY2Y9"}
                    ]]
                }
            )
            if "message_id" in note:
                sent_msgs.append(note["message_id"])

            # Schedule deletion of messages only
            Bot.runCommandAfter(
                1800,
                "/delete_messages",
                options={"user_id": message.chat.id, "message_ids": sent_msgs, "media_id": media_id}
            )
            
