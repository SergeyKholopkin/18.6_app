import telebot
from config import list, TOKEN
from utils import ConversionException, CryptoConverter
bot=telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text='Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты> \
<в какую валюту перевести>\
<количество переводимой валюты>\n<Увидеть список всех доступных валют: /values'
    bot.reply_to(message,text)
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text='Доступные валюты:'
    for a in list.keys():
        text='\n'.join((text,a,))
    bot.reply_to (message,text)

@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    try:

        values=message.text.split(' ')
        if len(values) != 3:
            raise ConversionException('слишком много параметров')#Ошибка пользователя
        quote, base, amount = values
        total_base = CryptoConverter.convert(quote,base,amount)# вызываем метод
    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена{amount}{quote} в {base} - {total_base*float(amount)}'
        bot.send_message(message.chat.id,text)


# @bot.message_handler()
# def echo_test(message: telebot.types.Message):
#     bot.send_message(message.chat.id,'Hello')
bot.polling()
