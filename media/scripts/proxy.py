from django.conf import settings
import os
from utils import log

def get_list_proxy():
    base_dir = settings.MEDIA_ROOT
    my_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'proxy_list.txt')
    log('Собираю прокси')
    with open(my_file, 'r') as f:
        proxies = f.read().split("\n")

    return proxies
