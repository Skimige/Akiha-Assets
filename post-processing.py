import json

with open('shop_data.json', 'r', -1, 'utf_8') as f:
    shops = json.load(f)
    shops_ht = {}
    for i in shops:
        i_id = i['id']
        shops_ht[i_id] = i
        del shops_ht[i_id]['placeId']

with open('shop_data.json', 'w', -1, 'utf_8') as f:
    json.dump(shops_ht, f, indent=4, ensure_ascii=False)
