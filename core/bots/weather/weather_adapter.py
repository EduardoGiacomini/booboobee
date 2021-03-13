class WeatherAdapter:
    @staticmethod
    def to_client(response):
        prevision_day = response['data'][0]['date_br']
        weather_resume = response['data'][0]['text_icon']['text']['phrase']['reduced']
        min_temperature = response['data'][0]['temperature']['min']
        max_temperature = response['data'][0]['temperature']['max']
        rain_probability = response['data'][0]['rain']['probability']
        rain_precipitation = response['data'][0]['rain']['precipitation']
        adapted_response = f'Previsão do dia {prevision_day}: {weather_resume} Temperatura entre {min_temperature:.0f}°C' \
                           f' e {max_temperature:.0f}°C. Probabilidade de {rain_probability:.0f}% para chuvas de até ' \
                           f'{rain_precipitation:.0f} mm.'
        return adapted_response
