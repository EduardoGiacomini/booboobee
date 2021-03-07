import locale


class CurrencyUtils:
    @staticmethod
    def to_brazilian_format(value):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(float(value), grouping=True, symbol=False)
