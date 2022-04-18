import json
import os

from flask_restful import Resource


with open(os.path.join('..', 'data', 'maimai', 'music_data.json'), 'r', -1, 'utf-8') as f:
    music_data = json.load(f)

with open(os.path.join('..', 'data', 'maimai', 'chart_stats.json'), 'r', -1, 'utf-8') as f:
    chart_stats = json.load(f)


class MaimaiDXMusicInfo(Resource):
    @staticmethod
    def get(music_id: str):
        return music_data[music_id]
