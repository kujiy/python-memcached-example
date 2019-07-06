from flask import Flask

DICTIONARY = {}  # DBでもなんでも良いです

app = Flask(__name__)

@app.route('/date')
def get_value():
    import datetime
    dt=datetime.datetime.strptime(data[4]+data[5],'%Y%m%d%H%M%S')
    print(dt)
    return dt


@app.route('/<key>')
def get_value(key):
    print(f'get_value({key})')
    return f'key={key}, value={DICTIONARY[key]}'


@app.route('/<key>/<value>', methods=['POST'])
def set_value(key, value):
    print(f'set_value({key},{value})')
    DICTIONARY[key] = value
    return 'OK'
