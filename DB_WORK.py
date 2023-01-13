import json
from psycopg2 import connect


def get_product_by_id(config: dict, id: int) -> tuple:
    database = config['database']
    host = config.get('host', 'localhost')
    password = config['password']
    user = config.get('user', 'postgres')

    conn = connect(database=database, password=password, host=host, user=user)

    try:
        with conn as conn:
            with conn.cursor() as cr:
                cr.execute(F'SELECT * FROM PRODUCTS WHERE PRODUCT_ID = {id}')
                values = [str(x) for x in cr.fetchone()]
                cr.execute("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'products' ")
                columns = [x[0] for x in cr.fetchall()]
                result = dict(zip(columns, values))
                return json.dumps(result)
    finally:
        conn.close()


def get_category_by_id(config: dict, id: int) -> tuple:
    database = config['database']
    host = config.get('host', 'localhost')
    password = config['password']
    user = config.get('user', 'postgres')

    conn = connect(database=database, password=password, host=host, user=user)

    try:
        with conn as conn:
            with conn.cursor() as cr:
                cr.execute(F'SELECT * FROM CATEGORIES WHERE CATEGORY_ID = {id}')
                values = [str(x) for x in cr.fetchone()]
                cr.execute("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'categories' ")
                columns = [x[0] for x in cr.fetchall()]
                result = dict(zip(columns, values))
                return json.dumps(result)
    finally:
        conn.close()
