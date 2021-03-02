import psycopg2

def openConn():
    conn = None
# Conexão com a database
    try:
        conn = psycopg2.connect(host="192.168.43.213",database="Twitterdb",port=5432,user='postgres',password='hitest123')
        print('Connecting to the PostgreSQL database...')
        cur = conn.cursor()
        cur.execute('SELECT version()')
        print('CONNECTION OPEN:PostgreSQL database version:')
        db_version = cur.fetchone()
        print(db_version)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn

def closeConn(conn):
    try:
        conn.close()
        print('Closed connection to the PostgreSQL database')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def main():
    openConn()
    closeConn(openConn())

if __name__ == "__main__":
    main()
