import telebot
from config import keys, TOKEN
from extensions import ConvertionException, ValueConvertor

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    text = 'Для перевода валют введите через проблел следующие параметры: \n \n<Имя валюты, цену которой хотите узнать> ' \
           '\n<Имя валюты, в которой надо узнать цену первой валюты> ' \
           '\n<Количество первой валюты>' \
           '\n \n \n Пример: доллар рубль 16' \
           '\n \n \n Список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message):
    try:
        value = message.text.split(' ')

        if len(value) != 3:
            raise ConvertionException('Введите корректное количество параметров.')

        quote, base, amount = value
        total_base = ValueConvertor.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'{amount} {keys[quote]} = {total_base} {keys[base]}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
