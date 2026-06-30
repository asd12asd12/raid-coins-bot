# Simple placeholder Telegram bot
# Install: pip install pyTelegramBotAPI
import telebot
TOKEN="PASTE_YOUR_TOKEN_HERE"
bot=telebot.TeleBot(TOKEN)

balances={}

@bot.message_handler(commands=['start'])
def s(m): bot.reply_to(m,"Raid Coins Bot is running!")

@bot.message_handler(commands=['balance'])
def bal(m):
    uid=str(m.from_user.id)
    bot.reply_to(m,f"Balance: {balances.get(uid,0)} RC")

@bot.message_handler(commands=['add'])
def add(m):
    if len(m.text.split())!=2:
        bot.reply_to(m,"Usage: /add 100"); return
    uid=str(m.from_user.id)
    balances[uid]=balances.get(uid,0)+int(m.text.split()[1])
    bot.reply_to(m,f"Added. Balance: {balances[uid]} RC")

bot.infinity_polling()
