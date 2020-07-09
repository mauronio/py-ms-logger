from flask import Flask
app = Flask(__name__)

from flask import request
from flask import Response

from datetime import datetime
import os

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/save', methods=['POST'])
def save():
    timestamp = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    report_header = '*** ' + timestamp + '\n'
    report_footer = '\n***\n\n'
    with open('saved.log', 'a') as f:
        f.write(report_header)
        f.write(str(request.data))
        f.write(report_footer)

    print('Saving', request.form)
    result = '{"status": "OK"}'
    resp = Response(result)
    resp.headers['Content-Type'] = 'application/json'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
