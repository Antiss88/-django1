import psycopg2
from config import host,user,password,db_name

try:
    #connect to exist datebase
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    #the cursor for perfoming database operations
    cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version():"

        )
        print(f"Server version:{cursor.fetchone()}")


except Exception as ex:
    print("[INFO] Error while working with PostgresSQL", _ex)
finally:
    if connection:
        #cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed ")
