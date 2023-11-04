import psycopg2


try:
    conn = psycopg2.connect(dbname='users', user='nonanon', 
                        password='admin', host='localhost')
except Exception as e:
    print(e)


def check_auth(log, passw):
    try:
        with conn.cursor() as cursor:
            query = '''SELECT * FROM public.users_auth WHERE login = %s AND password = %s'''
            cursor.execute(query, (log, passw,))
            result = cursor.fetchone()
            print(result)
            if result:
                return True
            else:
                return False
    except Exception as e:
        print(e)
    
def get_user(login):
    try:
        with conn.cursor() as cursor:
            query = '''SELECT name, surname FROM public.users_auth WHERE login = %s'''
            cursor.execute(query, (login,))
            credentials = cursor.fetchone()
            return credentials
    except Exception as e:
        print(e)


    #TODO bcrypt
