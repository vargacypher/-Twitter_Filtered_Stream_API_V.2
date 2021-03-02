# Postgresql & PgAdmin powered by compose


## Requisitos:
* docker >= 17.12.0+
* docker-compose

## Quick Start
* Clone ou baixe o repositório
* Entre no diretorio,  `cd home/hitest/Dev/PostgreSQL`
* Execute `docker-compose up -d`


## Ambientes
Esse arquivo compose possui as seguintes variaveis:

* `POSTGRES_USER` the default value is **postgres**
* `POSTGRES_PASSWORD` the default value is **admin**
* `PGADMIN_PORT` the default value is **80**
* `PGADMIN_DEFAULT_EMAIL` the default value is **pgadmin4@pgadmin.org**
* `PGADMIN_DEFAULT_PASSWORD` the default value is **admin**

## Acesso ao postgres: 
* `localhost:5432`
* **Username:** postgres (default)

## Author
Guilherme Cardoso de Vargas