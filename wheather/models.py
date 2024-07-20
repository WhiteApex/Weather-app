from django.db import models
from datetime import datetime as dt, timedelta as td
from utils import log

class SearchHistory(models.Model):
    request_datetime = models.CharField(max_length=30)
    login = models.CharField(max_length=30, blank=True)
    city_name = models.CharField(max_length=30)

def add_search_history(login, city):
    time = (dt.now() + td(hours=5)).strftime('%d.%m.%Y %H:%M:%S')
    log(f'Добавляю в базу Логин:{login}, город:{city}')
    SearchHistory.objects.create(login=login, city_name=city, request_datetime=time)

def get_search_history_by_login(login):
    log(f'Получаю статистику о пользователе:{login}')
    info = SearchHistory.objects.filter(login=login).values_list('request_datetime', 'login', 'city_name' )[::1]
    return info