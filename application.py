import sys

sys.path.insert(0, "./lib")

from flask import Flask, request, Response
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
application = app
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type'])
def test():
    return Response('Perch API v1.0.0')


@app.route('/hello', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type'])
def test_endpoints():
    return Response('Hello world!')


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=app.config.get("PORT", 7331),
            threaded=True)
