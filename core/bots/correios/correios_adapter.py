from bs4 import BeautifulSoup

from core.utils import TextUtils


class CorreiosAdapter:
    @staticmethod
    def to_client(response):
        adapted_response = ''
        html = BeautifulSoup(response.text, 'html.parser')
        tracked_object_events = html.find_all('table', {'class': 'listEvent sro'})
        for event in tracked_object_events:
            event_date = TextUtils.remove_blank_spaces(event.find('td', {'class': 'sroDtEvent'}).text.split('\n')[0])
            event_hour = TextUtils.remove_blank_spaces(event.find('td', {'class': 'sroDtEvent'}).text.split('\n')[1].strip())
            event_location = TextUtils.remove_blank_spaces(event.find('td', {'class': 'sroDtEvent'}).text.split('\n')[2].strip())
            event_description = TextUtils.remove_text_formatters(event.find('td', {'class': 'sroLbEvent'}).text)
            event_description = TextUtils.remove_blank_spaces(event_description)
            adapted_response += f'[{event_date} - {event_hour} - {event_location}]: {event_description}.\n'
        return adapted_response
