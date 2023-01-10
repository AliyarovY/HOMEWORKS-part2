import psycopg2 as ps


conn = ps.connect(
    database='north',
    password='123',
    user='postgres'
)

with open('id', 'r') as emp:
    id = int(emp.read())
with open('id', 'w') as emp:
    emp.write(str(id + 1))
    id = str(id)

print('CUSTOMER =')
customer_id = input('customer_id: ')
company_name = input('company_name: ')
contact_name = input('contact_name: ')
print('\nEMPLOYEES =')
first_name = input('first_name: ')
last_name = input('last_name: ')
title = input('title: ')
birth_date = input('birth_date: ')
notes = input('notes: ')
print('\nORDER =')
order_date = input('order_date: ')
ship_city = input('ship_cuty: ')

try:
    with conn as conn:
        with conn.cursor() as curs:
            curs.execute('INSERT INTO customers VALUES(%s ,%s ,%s);', (customer_id, company_name, contact_name))
            curs.execute('INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s);', (id, first_name, last_name, title, birth_date, notes))
            curs.execute('INSERT INTO orders VALUES(%s, %s, %s, %s, %s);', (id, customer_id, id, order_date, ship_city))

finally:
    conn.close()
