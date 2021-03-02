## Usando a API rest
Esta API permite visualizar dados resgatados e tratados da API V.2 do Twitter, conforme regras definidas .

## Rotas

* Home
##############

```python
@app.route('/', methods=['GET'])
def home():
    """  Estabelece método e rota da home da API  """
    return '''Prototipo de API para trazer dados sobre Tweets.'''

```

* ALL
##############

Total de postagens, agrupadas por hora do dia (independentemente da regra utilizada)

```python
@app.route('/api/tweet_all', methods=['GET'])
def api_all():
    """  Estabelece método e rota para busca de dados de horario dos tweets
    Arredondados a cada 30min e agrupados por timestamp  

    
    """
    conn = psycopg2.connect(host="192.168.9.36",database="Twitterdb",port=5432,user='postgres',password='hitest123')
    cur = conn.cursor()
    cur.execute('SELECT * FROM tweet_all;')
    tweet_covid = cur.fetchall()
    return json.dumps(tweet_covid, indent=4, sort_keys=True, default=str)

```

* Covid
##############

Total de postagens para regra Covid

```python
@app.route('/api/tweet_covid', methods=['GET'])
def api_covid():
    """  Estabelece método e rota para busca de dados de horario dos tweets com TAG COVID
    Arredondados a cada 30min e agrupados por timestamp      

    
    """
    conn = psycopg2.connect(host="192.168.9.36",database="Twitterdb",port=5432,user='postgres',password='hitest123')
    cur = conn.cursor()
    cur.execute('SELECT * FROM tweet_covid;')
    tweet_covid = cur.fetchall()
    return json.dumps(tweet_covid, indent=4, sort_keys=True, default=str)

```


* Saúde
##############

Total de postagens para regra Saúde

```python
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

```

## Erro
##############

```python
@app.errorhandler(404)
def page_not_found(e):
    """ Trativa de erro """
    return "ERROR 404. Recurso não encontrado !!!! .", 404 

```
## Execução da API

``` python
app.run(host="127.0.0.1", port=5000)
```

## Author
Guilherme Cardoso de Vargas

