import telebot
from telebot import types

TOKEN = '8845835190:AAGhbntudV0o8U-EsK2TyTcviPnAm7a9ans'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Scam Alert & Verification", callback_data='scam_alert')
    btn2 = types.InlineKeyboardButton("Password Generator", callback_data='pass_gen')
    btn3 = types.InlineKeyboardButton("Port Scanner", callback_data='port_scan')
    btn4 = types.InlineKeyboardButton("Account Manager", callback_data='acc_mgr')
    markup.add(btn1, btn2, btn3, btn4)
    
    welcome_text = (
        "Welcome to Cyber Guard & Scam Alert BD Bot!\n\n"
        "Please select your required option below:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'scam_alert':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Scam Alert: Report any suspicious links or offers to keep yourself safe.")
    elif call.data == 'pass_gen':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Password Guide: Always use at least 12 characters with mixed letters and numbers.")
    elif call.data == 'port_scan':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Port Scanner tool is ready for local network security checking.")
    elif call.data == 'acc_mgr':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Account Manager: Keep 2FA (Two-Factor Authentication) enabled on your social media.")

bot.infinity_polling(timeout=60, long_polling_timeout=60)
