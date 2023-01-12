
import requests
import json
from config import list
class ConversionException(Exception):
    pass
class CryptoConverter:
    @staticmethod# Метод
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConversionException(f'Невозможно перевести одинаковые валюты {base}')
        try:
            quote_ticker = list[quote]  # проверка соответствия вводимого значения словарю
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = list[base]  # проверка соответствия вводимого значения словарю
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количество{amount}')  # проверка соответствия кол-ва
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[list[base]]
        return total_base