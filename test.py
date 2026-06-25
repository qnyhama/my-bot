import time
import telebot

bot = telebot.TeleBot('8299694849:AAG9wFRUER6LZhVBVWumNgVNp8X63z2zsVY')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    time.sleep(1)
    welcome_text = "🚀 **بەخێر بێیت بۆ بۆتی CyberGuard** 🛡️\n\nسڵاو کاک ئەحمەد گیان! ✨"
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown')

# ئەم بەشە زۆر گرنگە بۆ ئەوەی بۆتەکە نەوەستێت
while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=20)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10) # ئەگەر پچڕا، ١٠ چرکە چاوەڕێ بکات و دووبارە دەست پێ بکاتەوە
