user_id = options.get("user_id")
msg_ids = options.get("message_ids", [])
media_id = options.get("media_id")

# Delete all sent messages
for mid in msg_ids:
    try:
        bot.deleteMessage(chat_id=user_id, message_id=mid)
    except Exception:
        pass

bot.sendMessage(
    chat_id=user_id,
    text="Your files have been deleted. 🔞+ আমাদের টেলিগ্রাম চ্যানেলের লিংক👇👇👇!",
    reply_markup={
        "inline_keyboard": [
            [{"text": "➤ ছোট বাচ্চাদের ডিরেক্ট ভিডিও", "url": "https://t.me/+7ggOOESyoRo0MjJl"}],
            [{"text": "➤ প্রিমিয়াম ডিরেক্ট ভাইরাল ভিডিও", "url": "https://t.me/+of34US1tstk5YzQ1"}],
            [{"text": "➤ দেশি আন্টি ডাইরেক্ট ভাইরাল ভিডিও", "url": "https://t.me/+1hImG4pywq9hNzNl"}],
            [{"text": "➤ ভাবিদের আকর্ষণীয় ভিডিও কালেকশন", "url": "https://t.me/+l35kWZtCgwQyNDU9"}],
            [{"text": "➤ এক্সক্লুসিভ ভিডিও কালেকশন", "url": "https://t.me/+nTdNDw1ps9cwYmE1"}],
            [{"text": "➤ বাংলাদেশি কালেকশন", "url": "https://t.me/+WH_DRCyBc4w3MTFl"}],
            [{"text": "➤ বৌদির ভাইরাল ডিরেক্ট ভিডিও", "url": "https://t.me/+T3n5y7jU08IwY2Y9"}],
            [{"text": "➤ আমাদের মুভি চ্যানেল লিংক", "url": "https://t.me/Moviebox_26"}],
            [{"text": "➤ দেশি ভাইরাল ডাইরেক্ট ভিডিও কালেকশন", "url": "https://t.me/+4Z6spztUJ49lNDk1"}],
            [{"text": "➤ এক্সক্লুসিভ ভিডিও কালেকশন", "url": "https://t.me/+nTdNDw1ps9cwYmE1"}],
            [{"text": "➤ ভাইরাল চ্যাট গ্রুপ", "url": "https://t.me/chat_group26"}]
        ]
    }
)
