import telebot
import random

bot = telebot.TeleBot("5810646799:AAFn9sMDTJJJXQucWKnPgRYg35uqNbt5Xng")

@bot.message_handler(commands=['game'])
def lets_play(message):
    N = 117
    bot.reply_to(message, "Let's fire!!!")
    player = random.choice(['user', 'bot'])
    bot.send_message(message.chat.id, f'Первый ходит {player}')
    if player == 'bot':
        take_bot = random.randint(0, 28)
        N = N - take_bot
        bot.send_message(message.chat.id, f'Бот взял {take_bot} конфет')
        bot.send_message(message.chat.id, f'Осталось {N} конфет')
        player = 'user'
        msg = bot.send_message(message.chat.id, 'Теперь ходит user')
        bot.register_next_step_handler(msg, game_prosess)
    else:
        bot.send_message(message.chat.id, 'Возьмите конфеты')
        N -= int(message.text)
        bot.send_message(message.chat.id, f'Осталось {N} конфет')
        player = 'bot'
        msg = bot.send_message(message.chat.id, 'Теперь ходит бот')
        bot.register_next_step_handler(msg, game_prosess)
        
def game_prosess(message):
    if player == 'user':
        bot.send_message(message.chat.id, f'Возьмите конфеты')
        N -= int(message.text)
        bot.send_message(message.chat.id, f'Осталось {N} конфет')
        player = 'bot'
        if N < 28:
            bot.send_message(message.chat.id, f'Победил user!')
        else:
            bot.send_message(message.chat.id, f'Ходит бот')
            take_bot = random.randint(0, 28)
            N = N - take_bot
            msg = bot.send_message(message.chat.id, f'Осталось {N} конфет ')
            player = 'user'
            bot.register_next_step_handler(msg, game_prosess)
                    
    else:
        if N < 28:
            bot.send_message(message.chat.id, 'Победил бот!')
        else:
            bot.send_message(message.chat.id, f'Ходит бот')
            take_bot = random.randint(0, 28)
            N = N - take_bot
            msg = bot.send_message(message.chat.id, f'Осталось {N} конфет ')
            player = 'user'
            bot.register_next_step_handler(msg, game_prosess)
	
bot.infinity_polling()