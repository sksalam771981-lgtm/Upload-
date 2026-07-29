import os
import telebot

# রেন্ডার পরিবেশ থেকে টোকেন নেওয়ার জন্য os.environ ব্যবহার করা হয়েছে
API_TOKEN = os.getenv('8162257584:AAGu6N2FrHhkVUWF67ifGQmbD_0V-5m_UAI')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['video'])
def handle_video(message):
    bot.reply_to(message, "এখন ভিডিওর Title লিখুন।")

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    share_link = f"https://t.me/PrivateVideoXBot?start=example_id"
    
    response_text = (
        f"✅ **Video Uploaded Successfully**\n\n"
        f"📁 **Title:** {message.text}\n\n"
        f"🔗 **Share Link:**\n{share_link}"
    )
    bot.reply_to(message, response_text, parse_mode="Markdown")

# রেন্ডারে বট চালু রাখার জন্য infinite_polling ব্যবহার করা最优
bot.infinity_polling()
