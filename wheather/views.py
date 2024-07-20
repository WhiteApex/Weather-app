import requests
from django.shortcuts import render
from django.http import HttpResponse
from utils import log, number_to_weekday
from .models import add_search_history, get_search_history_by_login
from datetime import datetime as dt
import json


def home(request):
	log('Отрисовываю начальную страницу')
	return render(request, 'wheather/home.html')

def result(request):
	if request.method == 'GET':
		
		log('Выполняю GET запрос')
		city_name = request.GET.get('city')
		login = request.GET.get('login')

		if city_name is None:
			log('Неверный город')
			return
		else:
			if login is None:
				login = 'Не указан'
			#запрос в бд
			
			add_search_history(login=login, city=city_name)
			context = {
				'info' : get_info_for_city(city_name)
			}
			context['count'] = len(context['info'])
	if 'exception' in context['info']:
			log('Отрисовка ошибки')
			context['info']['error'] = 'Введите корректный город'
			
			log(f'ошибка поиска города:{city_name}')
			return render(request, 'wheather/home.html', context)

	log('Отрисовываю шаблон')
	return render(request, 'wheather/result.html', context)


def history(request):
	if request.method == 'GET':
		login = request.GET.get('login')
		info = {
			'search_history': get_search_history_by_login(login)
		}
	info = json.dumps(info, indent=4, ensure_ascii=False)
	return HttpResponse(info, content_type="application/json")

def get_info_for_city(city: str) -> list:
	
	key_2 = '1e564a4983b048fc8ae113217241907'
	api_2 = f'http://api.weatherapi.com/v1/forecast.json?key={key_2}&q={city}&days=5&aqi=no&alerts=no&lang=ru'


	# сервис не работает без vpn, прокси не помогает, возможно проблема в самом django, он как-то влияет на запросы
	# key = 'e1f511dd5c8865e16d1df42fd93f7bbf'
	# api = 'https://api.openweathermap.org/data/2.5/forecast?q=' + city + '&units=metric&lang=ru&appid=' + key
	#api = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=' + key

	info = get_forcast(api_2)

	return info

#на несколько дней
def get_forcast(api):
		
		log('Получаю данные')
		result = requests.get(api)
		if 'error' in result.json():
			info ={
					'exception': 'Вы ввели несуществующий город'
				}
			return info
		print(result.json())
		result = result.json()['forecast']['forecastday']
		log('Данные из API получены')
		info = []
		i = 0
		for item in result:

			date = dt.strptime(item['date'], '%Y-%m-%d')
			pre = {
				'temp': item['day']['avgtemp_c'],
				'temp_min': item['day']['mintemp_c'],
				'temp_max': item['day']['maxtemp_c'],
				'wheather': item['day']['condition']['text'],
				'date': date.strftime('%d.%m.%Y'),
				'weekday': number_to_weekday[date.weekday()]
			}

			info.append(pre)
		log('Данные сформированы')
		return info

# example_info = [
#{
# 		"temp": 22.93,
# 		"temp_min": 17.26,
# 		"temp_max": 22.93,
# 		"wheather": "дождь",
# 		"dt_txt": "2024-07-18 12:00:00"
#},
# ]

#для 1 дня
def get_one_day(api):
	result = requests.get(api)
	data = result.json()
	return data
