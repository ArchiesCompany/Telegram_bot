import telebot
from telebot import types

bot = telebot.TeleBot('TOKEN')
 
@bot.message_handler(commands=['start'])



#---------------------------------------------------------------------------



def welcome(message):

 
    # keyboard (Создание кнопок и приветствие)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📋 Информация 📋")
    item2 = types.KeyboardButton("💎 Заказать сайт для бизнеса 💎")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, помогу тебе увеличить продажи!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])



#---------------------------------------------------------------------------



def lalala(message):
    if message.chat.type == 'private':
        if message.text == '💎 Заказать сайт для бизнеса 💎':
 
 			# keyboard (Создание кнопок под текстом)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("💸 Заказать интернет магазин. 💸", callback_data='1')
            item2 = types.InlineKeyboardButton("⚡ Заказать сайт-визитку. ⚡", callback_data='2')
            item3 = types.InlineKeyboardButton("🏢 Заказать корпоративный сайт. 🏢", callback_data='3')
            item4 = types.InlineKeyboardButton("🌟 Заказать электронное портфолио. 🌟", callback_data='4')
 
            markup.add(item1, item2, item3, item4)
 
            bot.send_message(message.chat.id, 'Что вам нужно?', reply_markup=markup)

        # elif message.text == ' '
        elif message.text == "📋 Информация 📋":
            bot.send_message(message.chat.id, " 📃 Мы работаем в сфере создания сайтов уже 5-й год." +
                " Наша профессиональная команда готова помочь вам с любыми трудностями, мы обладаем лучшей аппаратурой для выполнений всех" + 
                " задач в сфере Веб-разработки и дизайна. Наши услуги дают возможность максимально индивидуализировать продукт под себя.")

        
        else:
            bot.send_message(message.chat.id, 'По другим вопросам пишите сюда → @dev_archi')



#---------------------------------------------------------------------------



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:

        	# keyboard (Работа с кнопками под текстом)
            if call.data == '1':
                bot.send_message(call.message.chat.id, '💥 Пишите сюда → @dev_archi')
            elif call.data == '2':
                bot.send_message(call.message.chat.id, '💥 Пишите сюда → @dev_archi')
            elif call.data == '3':
                bot.send_message(call.message.chat.id, '💥 Пишите сюда → @dev_archi')
            elif call.data == '4':
                bot.send_message(call.message.chat.id, '💥 Пишите сюда → @dev_archi')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Спасибо за оброщение! 😘",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="Пишите, всегда поможем!")
 
    except Exception as e:
        print(repr(e))
 


#---------------------------------------------------------------------------


# Старт
bot.polling(none_stop=True)



#---------------------------------------------------------------------------