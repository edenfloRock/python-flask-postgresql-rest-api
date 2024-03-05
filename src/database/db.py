import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        print ("PGSQL_HOST: " + config('PGSQL_HOST'))
        return psycopg2.connect(            
            host=config('PGSQL_HOST'),
            port =config('PGSQL_PORT'),
            database=config('PGSQL_DATABASE'),
            user = config('PGSQL_USER'),
            password = config('PGSQL_PASSWORD')
        )
    except DatabaseError as ex:
        raise ex