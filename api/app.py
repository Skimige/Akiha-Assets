from flask import Flask
from flask_restful import Api

from ..src.maimai import MaimaiDXMusicInfo

app = Flask(__name__)
api = Api(app)

api.add_resource(MaimaiDXMusicInfo, '/api/maimai/<string:id>')
