import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class ValueConvertor:
    @staticmethod
    def get_price(quote: str, base: str, amount: int):

        if quote == base:
            raise ConvertionException(f'Нельзя конвертировать валюту {quote} в саму себя.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось конвертировать валюту {quote}'
                                      '\n\n\nСписок всех доступных валют: /values')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось конвертировать в валюту {base}'
                                      '\n\n\nСписок всех доступных валют: /values')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        total_base *= amount

        return total_base
