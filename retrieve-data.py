import os
import json

import requests


shop_data = requests.get(os.getenv('WAHLAP_SHOP_API_URL')).json()
alias_data = requests.get(os.getenv('ALIAS_SHEET_TSV_URL'))
music_data = requests.get(os.getenv('MUSIC_DATA_URL')).json()
chart_stats_data = requests.get(os.getenv('CHART_STATS_DATA_URL')).json()

# Shop Data
shop_data_ht = {}
for i in shop_data:
    i_id = i['id']
    shop_data_ht[i_id] = i
    del shop_data_ht[i_id]['placeId']

with open('shop_data.json', 'w', -1, 'utf-8') as f:
    json.dump(shop_data_ht, f, indent=4, ensure_ascii=False)

# Alias
with open('aliases.tsv', 'w', -1, 'utf-8') as f:
    f.write(alias_data.text)

# Music
music_data = {i['id']: i for i in music_data}
with open('music_data.json', 'w', -1, 'utf-8') as f:
    json.dump(music_data.json(), f, indent=4, ensure_ascii=False)

# Chart Stats
with open('chart_stats.json', 'w', -1, 'utf-8') as f:
    json.dump(chart_stats_data, f, indent=4, ensure_ascii=False)
