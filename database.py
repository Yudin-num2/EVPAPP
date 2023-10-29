import psycopg2


try:
    conn = psycopg2.connect(dbname='users', user='nonanon', 
                        password='admin', host='localhost')
except Exception as e:
    print(e)


def check_auth(login):
    try:
        with conn.cursor() as cursor:
            request = '''SELECT password FROM public.users_auth WHERE login = '%s'
                           '''
            cursor.execute(request, login)
            result = cursor.fetchone()
            if result:
                return True
            else:
                return False
    except Exception as e:
        print(e)
    
def get_user(login):
    try:
        with conn.cursor() as cursor:
            request = '''SELECT name, surname FROM public.users_auth WHERE login = '%s'
                           '''
            cursor.execute(request, login)
            credentials = cursor.fetchone()
            return credentials
    except Exception as e:
        return e


    #TODO bcrypt
