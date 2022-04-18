from flask import Flask

from src.maimai import MaimaiDXMusicInfo

app = Flask(__name__)


@app.route('/api/maimai/music/<string:music_id>')
def maimai_dx_music_info(music_id):
    return MaimaiDXMusicInfo.get(music_id)


if __name__ == '__main__':
    app.run(debug=True)