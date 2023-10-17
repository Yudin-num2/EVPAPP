import psycopg2



conn = psycopg2.connect(dbname='users', user='nonanon', 
                        password='admin', host='localhost')

def check_auth(login, passw):
    try:
        with conn.cursor() as cursor:
            cursor.execute(f'SELECT {passw} in users WHERE login={login}')
    except:
        pass
