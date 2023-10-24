import psycopg2



conn = psycopg2.connect(dbname='users', user='nonanon', 
                        password='admin', host='localhost')

def check_auth(login):
    try:
        with conn.cursor() as cursor:
            cursor.execute(f'''SELECT password FROM public.users_auth WHERE login = '{login}'
                           ''')
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
            cursor.execute(f'''SELECT name, surname FROM public.users_auth WHERE login = '{login}'
                           ''')
            credentials = cursor.fetchone()
            return credentials
    except Exception as e:
        return e


    #TODO bcrypt
