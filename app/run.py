from flask import Flask
import datetime
import time


DICTIONARY = {}  # DBでもなんでも良いです

app = Flask(__name__)

@app.route('/date')
def get_date():
    t =  time.strftime('%Y%m%d%H%I%S') 
    return t 


@app.route('/<key>')
def get_value(key):
    print(f'get_value({key})')
    return f'key={key}, value={DICTIONARY[key]}'


@app.route('/<key>/<value>', methods=['GET', 'POST'])
def set_value(key, value):
    print(f'set_value({key},{value})')
    DICTIONARY[key] = value
    return 'OK'

@app.route('/')
def get_root():
    return "ok"

if __name__ == '__main__':
    # def port 5000
    app.run(debug = True)
