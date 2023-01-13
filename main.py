from passw import password
import psycopg2 as ps
import json


conn = ps.connect(
    host='localhost',
    database='NorthWind Traders',
    password=password,
    user='postgres',
)

try:
    with conn as conn:
        with conn.cursor() as cur:
            cur.execute(
                '''create table if not exists suppliers(
                company_name varchar(255) not null,
                contact varchar(255),
                address text,
                phone varchar(30) DEFAULT NULL,
                fax varchar(255) DEFAULT NULL,
                homepage varchar(255) DEFAULT NULL,
                product varchar(255) unique
                )
                ''')

            with open('json.suppliers', encoding='UTF-8') as sup_file:
                suppliers = json.load(sup_file)
                used_products = set()

                for sup in suppliers:
                    for product in sup['products']:
                        if product in used_products:
                            continue
                        used_products.add(product)

                        ex = ','.join(["'" + x.replace('\'', '"') + "'" for k, x in sup.items() if k != 'products'])
                        ex = """INSERT INTO SUPPLIERS VALUES(
                        {},  '{}'
                        )""".format(ex, product.replace('\'', '"'))
                        cur.execute(ex)



finally:
    conn.close()
