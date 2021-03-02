# -*- coding: utf-8 -*-
__author__ = 'Guilherme Cardoso de Vargas'
__version__ = 1.0
__maintainer__ = 'Guilherme Cardoso de Vargas'
__email__ = 'vargas93626@gmail.com'
__status__ = 'Prototype'


import flask
import psycopg2
from flask import request
import json


app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Define método da API
@app.route('/', methods=['GET'])
def home():
    """  Estabelece método e rota da home da API  """
    return '''Prototipo de API para trazer dados sobre Tweets.'''

@app.route('/api/tweet_all', methods=['GET'])
def api_all():
    """  Estabelece método e rota para busca de dados de horario dos tweets
    Arredondados a cada 30min e agrupados por timestamp  

    Total de postagens, agrupadas por hora do dia (independentemente da regra utilizada)
    """
    conn = psycopg2.connect(host="192.168.9.36",database="Twitterdb",port=5432,user='postgres',password='hitest123')
    cur = conn.cursor()
    cur.execute('SELECT * FROM tweet_all;')
    tweet_covid = cur.fetchall()
    return json.dumps(tweet_covid, indent=4, sort_keys=True, default=str)

@app.route('/api/tweet_covid', methods=['GET'])
def api_covid():
    """  Estabelece método e rota para busca de dados de horario dos tweets com TAG COVID
    Arredondados a cada 30min e agrupados por timestamp      

    Total de postagens para regra Covid
    """
    conn = psycopg2.connect(host="192.168.9.36",database="Twitterdb",port=5432,user='postgres',password='hitest123')
    cur = conn.cursor()
    cur.execute('SELECT * FROM tweet_covid;')
    tweet_covid = cur.fetchall()
    return json.dumps(tweet_covid, indent=4, sort_keys=True, default=str)

@app.route('/api/tweet_saude', methods=['GET'])
def api_saude():
    """  Estabelece método e rota para busca de dados de horario dos tweets com TAG SAUDE
    Arredondados a cada 30min e agrupados por timestamp   

     Total de postagens para regra Saude   
    """
    conn = psycopg2.connect(host="192.168.9.36",database="Twitterdb",port=5432,user='postgres',password='hitest123')
    cur = conn.cursor()
    cur.execute('SELECT * FROM tweet_saude;')
    tweet_covid = cur.fetchall()
    return json.dumps(tweet_covid, indent=4, sort_keys=True, default=str)

@app.errorhandler(404)
def page_not_found(e):
    """ Trativa de erro """
    return "ERROR 404. Recurso não encontrado !!!! .", 404 

app.run(host="127.0.0.1", port=5000)

