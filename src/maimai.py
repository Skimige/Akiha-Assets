import json
import os

from flask_restful import Resource


with open(os.path.join('..', 'data', 'maimai', 'music_data.json'), 'r', -1, 'utf-8') as f:
    music_data = json.load(f)


class MaimaiDXMusicInfo(Resource):
    def get(self, id: str):
        return music_data[id]
