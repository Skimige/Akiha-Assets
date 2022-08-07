import os
import json
from functools import wraps
from traceback import format_exc

import requests


def wrap_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            print(format_exc())
            return None
    return wrapper


# Shop Data
@wrap_exception
def update_shop_data():
    games = ['chunithm', 'maimai']
    for game in games:
        resp = requests.get(os.getenv(f'WAHLAP_{game.upper()}_SHOP_DATA_URL'))
        resp.raise_for_status()

        shop_data = resp.json()
        shop_data_ht = {}
        for i in shop_data:
            i_id = i['id']
            shop_data_ht[i_id] = i
            del shop_data_ht[i_id]['placeId']
        with open(f'data/{game}/shop_data.json', 'w', -1, 'utf-8') as f:
            json.dump(shop_data_ht, f, indent=4, ensure_ascii=False)


# Maimai: Alias Data
@wrap_exception
def update_maimai_alias_data():
    alias_data = requests.get(os.getenv('ALIAS_SHEET_TSV_URL'))
    alias_data.raise_for_status()
    alias_data.encoding = 'utf-8'
    with open('data/maimai/aliases.tsv', 'w', -1, 'utf-8') as f:
        f.write(alias_data.text)


# Maimai: Music Data
@wrap_exception
def update_maimai_music_data():
    music_data = requests.get(os.getenv('MUSIC_DATA_URL')).json()
    music_data = {i['id']: i for i in music_data}
    with open('data/maimai/music_data.json', 'w', -1, 'utf-8') as f:
        json.dump(music_data, f, indent=4, ensure_ascii=False)


# Maimai: Chart Stats Data
@wrap_exception
def update_maimai_chart_stats_data():
    chart_stats_data = requests.get(os.getenv('CHART_STATS_DATA_URL')).json()
    with open('data/maimai/chart_stats.json', 'w', -1, 'utf-8') as f:
        json.dump(chart_stats_data, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    print('Updating Shop Data...')
    update_shop_data()
    print('Updating Maimai Alias Data...')
    update_maimai_alias_data()
    print('Updating Maimai Music Data...')
    update_maimai_music_data()
    print('Updating Maimai Chart Stats Data...')
    update_maimai_chart_stats_data()
    exit(0)
