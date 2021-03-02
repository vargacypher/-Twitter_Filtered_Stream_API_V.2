## Usando a Twitter API
A API do Twitter nos permite resgatar e analisar dados de diferentes fontes e categorias.

A API permite o acesso a uma variedade de recursos como:

-Tweets

-Users

-Trends

-Media

-Places

Com base nisso, este projeto foi desenvolvido para analisar dados de tweets relacionados a Covid e a Saúde, utilizando o método
Filtered Stream da API V.2 do Twitter.

## Salvar dados no banco
##############

A função pega os campos id_tweet,created_at,text,author_id,matching_rules' e salva eles no banco PostgreSQL

```python

    
def save_data(id_tweet,created_at,text,author_id,matching_rules):
    """  Armazena os dados nos paramentros selecionados e os insere no banco de dados definido """
    # Conexão com a database    
    conn = psycopg2.connect(host="192.168.9.36",database="Twitterdb",port=5432,user='postgres',password='hitest123')
    print('Connecting to the PostgreSQL database...')
    conn.set_session(autocommit=True)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO twittertweet (author_id,tweet_id,tweet,rule,created_at) VALUES (%s,%s,%s,%s,%s)", (author_id,id_tweet,text,matching_rules,created_at))
    cursor.close()
    conn.close()
    print('Closed connection to the PostgreSQL database')
    return

```

## Token de acesso a API

```python
BEARER_TOKEN='<your_bearer_token>'
```

## Autenticação com a API
##############

```python

    
def auth():
    """  Busca token de autenticação definido na variavel  """
    return os.environ.get("BEARER_TOKEN")

#Headers de acesso, cabeçalho de requisição HTTP
def create_headers(bearer_token): 
    """  Armazena os dados nos paramentros e os insere no banco de dados definido  """
    #### Corrige os caracteres que estiverem bugado e coloca esse header:
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}", 'Content-Type': 'application/json',}
    return headers
```

## Regras API (Filtered_Stream)
##############

```python

    
def get_rules(headers, bearer_token):
    """  Busca as regras definidas na API do Twitter  """
    requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", headers=headers
    )

    # Definindo as regras
def set_rules(headers, bearer_token):
    """  Define as regras de COVID e SAUDE nas rules da API do Twitter """   
    sample_rules = [
        {"value": "COVID lang:pt", "tag": "Covid rule"},
        {"value": "Saude lang:pt","tag": "Saude rule"},
    ]
    payload = {"add": sample_rules}
    requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload,
    )
```

## Conexão com a API
##############
Estabelece a conexão com a Stream API V.2 do Twitter

```python

def connect_endpoint(headers, bearer_token):
    """  Define o endpoint conectado, buscando dados da API e os insere no banco de dados. """  

    response = requests.get("https://api.twitter.com/2/tweets/search/stream?tweet.fields=attachments,author_id,created_at", headers=headers, stream=True )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
        "Cannot get stream (HTTP {}): {}".format(response.status_code, response.text)
        )
#print(response.content[:100])
    for response_line in response.iter_lines():
        if response_line:        
            tweet= json.loads(response_line) # Carrega o tweet como um Objeto JSON
            print (tweet)

#Filtando as colunas

            id_tweet = tweet.get('data',{}).get('id')  # {} Retorna um objeto vazio caso o campo esteja nulo no JSON
            created_at = tweet.get('data',{}).get('created_at')
            text = tweet.get('data',{}).get('text')
            author_id = tweet.get('data',{}).get('author_id')
            matching_rules = tweet.get('matching_rules',[None])[0].get('tag')

# Inserir Tweet na database
                #save_data(id_tweet,created_at,text,author_id,matching_rules)
```

## Documentação Oficial API twitter

* Website: https://developer.twitter.com/en/docs/twitter-api/early-access
* Getting started: https://developer.twitter.com/en/docs/twitter-api/getting-started


## AUTHOR:

Guilherme Cardoso de Vargas

