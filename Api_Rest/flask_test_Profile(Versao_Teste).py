# -*- coding: utf-8 -*-
__author__ = 'Guilherme Cardoso de Vargas'
__version__ = 1.0
__maintainer__ = 'Guilherme Cardoso de Vargas'
__email__ = 'vargas93626@gmail.com'
__status__ = 'Development'

import flask
import psycopg2
from flask import request
import json
import flask_profiler

app = flask.Flask(__name__) 
app.config["DEBUG"] = True

# flask-profiler :
app.config["flask_profiler"] = {
    "enabled": app.config["DEBUG"],
    "storage": {
        "engine": "sqlalchemy",
        "db_url": "192.168.43.213:5432/flask_profiler"  
    },
    "basicAuth":{
        "enabled": True,
        "username": "postgres",
        "password": "hitest123"
    },
    "ignore": [
	    "^/static/.*"
	]
}

@app.route('/', methods=['GET'])
def home():
    return '''Prototipo de API para trazer dados sobre Tweets.'''

@app.route('/api/tweet_all', methods=['GET'])
def api_all():
    conn = psycopg2.connect(host="192.168.43.213",database="Twitterdb",port=5432,user='postgres',password='hitest123')
    cur = conn.cursor()
    cur.execute('SELECT rule as Rules, count as Count, timestamp as Time FROM teste;')
    tweet_covid = cur.fetchall()
    return json.dumps(tweet_covid, indent=4, sort_keys=True, default=str)

@app.route('/api/tweet_covid', methods=['GET'])
def api_covid():
    conn = psycopg2.connect(host="192.168.43.213",database="Twitterdb",port=5432,user='postgres',password='hitest123')
    cur = conn.cursor()
    cur.execute('SELECT rule as Rules, count as Count, timestamp as Time FROM teste;')
    tweet_covid = cur.fetchall()
    return json.dumps(tweet_covid, indent=4, sort_keys=True, default=str)

@app.route('/api/tweet_saude', methods=['GET'])
def api_saude():
    conn = psycopg2.connect(host="192.168.43.213",database="Twitterdb",port=5432,user='postgres',password='hitest123')
    cur = conn.cursor()
    cur.execute('SELECT rule as Rules, count as Count, timestamp as Time FROM teste;')
    tweet_covid = cur.fetchall()
    return json.dumps(tweet_covid, indent=4, sort_keys=True, default=str)

flask_profiler.init_app(app)

@app.errorhandler(404)
def page_not_found(e):
    return "404. The resource could not be found.", 404 

app.run(host="127.0.0.1", port=5000)

