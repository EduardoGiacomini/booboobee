class DatetimeUtils:
    @staticmethod
    def to_brazilian_format(date):
        year, month, day = date.split('-')
        return f'{day}/{month}/{year}'
