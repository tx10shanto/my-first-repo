import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# BOT TOKEN
BOT_TOKEN = "9228446700:AAHVjtTAK0TBQhuI_tW5lId7pgNLrKqvjmE"

bot = telebot.TeleBot(BOT_TOKEN)

# CHANNEL LINKS
CHANNEL_1 = "https://t.me/inbox4451"
CHANNEL_2 = "https://t.me/+HxY5YihaPEczNmE1"


@bot.message_handler(commands=['start'])
def start(message):

    welcome_text = """
🌟 স্বাগতম আমাদের Telegram Bot-এ! 🌟

━━━━━━━━━━━━━━━━━━

👋 হ্যালো! আপনাকে আমাদের
অফিশিয়াল বটে স্বাগতম।

📢 আমাদের আপডেট পেতে নিচের
দুটি Telegram Channel-এ যুক্ত হন।

━━━━━━━━━━━━━━━━━━

💎 ধন্যবাদ আমাদের সাথে থাকার জন্য!
"""

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            "📢 JOIN CHANNEL 1",
            url=CHANNEL_1
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "🚀 JOIN CHANNEL 2",
            url=CHANNEL_2
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "✅ DONE",
            callback_data="done"
        )
    )

    bot.send_message(
        message.chat.id,
        welcome_text,
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: call.data == "done")
def done_callback(call):
    bot.answer_callback_query(
        call.id,
        "ধন্যবাদ! ❤️"
    )


print("🤖 BOT IS RUNNING...")

bot.infinity_polling()