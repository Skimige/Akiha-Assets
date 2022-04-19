import json
import os

from flask import Flask, Response, jsonify, request


with open(os.path.join('data', 'maimai', 'music_data.json'), 'r', -1, 'utf-8') as f:
    music_data = json.load(f)

with open(os.path.join('data', 'maimai', 'chart_stats.json'), 'r', -1, 'utf-8') as f:
    chart_stats = json.load(f)

app = Flask(__name__)


@app.route('/api/maimai/music', methods=['GET'])
def maimai_dx_music_info():
    args = request.args
    music_id = args.get('music_id', default='', type=str)
    if music_id in music_data:
        print(music_data[music_id])
        return jsonify(music_data[music_id])
    else:
        return Response('Specified music not found.', status=404)

@app.errorhandler(404)
def not_found(error):
    # Include request info in response
    print(error)
    return Response(jsonify({
        'path': request.path,
        'params': request.args,
        'method': request.method,
        'message': 'Not found'
    }), status=404)

# if __name__ == '__main__':
#     app.run(debug=True)
