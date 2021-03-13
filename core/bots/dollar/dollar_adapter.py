from core.utils import CurrencyUtils, DatetimeUtils


class DollarAdapter:
    @staticmethod
    def to_client(response):
        cotation_day, cotation_hour = response['USD']['create_date'].split(' ')
        formatted_cotation_day = DatetimeUtils.to_brazilian_format(cotation_day)
        cotation_value = response['USD']['high']
        formatted_cotation_value = CurrencyUtils.to_brazilian_format(cotation_value)
        adapted_response = f'Cotação do dólar comercial do dia {formatted_cotation_day}: R${formatted_cotation_value}.'
        return adapted_response
