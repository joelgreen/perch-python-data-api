from flask import Flask, request, Response, jsonify
from flask.ext.cors import CORS, cross_origin

from perch.data.truck_schedule import generate_truck_schedule

app = Flask(__name__)
application = app
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type'])
def test():
    return Response('Perch API v1.0.0')


@app.route('/hello', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type'])
def hello_world():
    return Response('Hello world!')


@app.route('/random_truck_schedule', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type'])
def random_truck_schedule():
    trucks = generate_truck_schedule(5)
    resp = {
        "trucks": trucks
    }
    return jsonify(resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=app.config.get("PORT", 7331),
            threaded=True)
