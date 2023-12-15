import pymysql

try:
    connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='qwadratz4323',
    database='EVPDB',
    cursorclass=pymysql.cursors.DictCursor
)
    print('[INFO] Connection is successfull!')
except Exception as e:
    print(e)


def check_auth(log, passw):
    # try:
    with connection.cursor() as cursor:
        query = '''SELECT * FROM users_auth WHERE login = %s AND password = %s'''
        cursor.execute(query, (log, passw,))
        result = cursor.fetchone()
        print(result)
        if result:
            return True
        else:
            return False
    # except Exception as e:
    #     print(e)
    
def get_user(login):
    try:
        with connection.cursor() as cursor:
            query = '''SELECT name, surname FROM public.users_auth WHERE login = %s'''
            cursor.execute(query, (login,))
            credentials = cursor.fetchone()
            return credentials
    except Exception as e:
        print(e)


    #TODO bcrypt
