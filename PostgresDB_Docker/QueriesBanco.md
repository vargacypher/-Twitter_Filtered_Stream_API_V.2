## Conta registros e agrupa pela horario arredondado a cada 30 minutos
~~~~sql
SELECT COUNT(*), 
    date_trunc('hour', created_at) +
    (((date_part('minute', created_at)::integer / 30::integer) * 30::integer)
     || ' minutes')::interval AS timestamp
INTO tweet_all
FROM twittertweet
GROUP BY timestamp;
~~~~


## Conta registros e agrupa pela Covid Rule
~~~~sql
SELECT RULE,COUNT(*), 
    date_trunc('hour', created_at) +
    (((date_part('minute', created_at)::integer / 30::integer) * 30::integer)
     || ' minutes')::interval AS timestamp
INTO tweet_covid
FROM twittertweet
where rule ilike '%COVID%'
GROUP BY RULE,timestamp;
~~~~

## Conta registros e agrupa pela Saude Rule
~~~~sql
SELECT RULE,COUNT(*), 
    date_trunc('hour', created_at) +
    (((date_part('minute', created_at)::integer / 30::integer) * 30::integer)
     || ' minutes')::interval AS timestamp
INTO tweet_saude
FROM twittertweet
where rule ilike '%SAUDE%'
GROUP BY RULE,timestamp;
~~~~
