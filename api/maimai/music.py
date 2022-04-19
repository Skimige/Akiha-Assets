import json
import os

from flask import Flask, Response, jsonify


with open(os.path.join('data', 'maimai', 'music_data.json'), 'r', -1, 'utf-8') as f:
    music_data = json.load(f)

with open(os.path.join('data', 'maimai', 'chart_stats.json'), 'r', -1, 'utf-8') as f:
    chart_stats = json.load(f)

app = Flask(__name__)


@app.route('/<string:music_id>', methods=['GET'])
def maimai_dx_music_info(music_id):
    if music_id in music_data:
        print(music_data[music_id])
        return jsonify(music_data[music_id])
    else:
        return Response('Specified music not found.', status=404)


# if __name__ == '__main__':
#     app.run(debug=True)
