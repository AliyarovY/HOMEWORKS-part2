-- Название компании заказчика (company_name из табл. customers) и ФИО сотрудника, работающего над заказом этой компании (см таблицу employees), когда и заказчик и сотрудник зарегистрированы в городе London, а доставку заказа ведет компания United Package (company_name в табл shippers)
SELECT CS.COMPANY_NAME, CONCAT(first_name, ' ', last_name) AS FIO
FROM CUSTOMERS CS
JOIN EMPLOYEES EP ON EP.CITY=CS.CITY
JOIN SHIPPERS SH ON EP.EMPLOYEE_ID = SH.SHIPPER_ID
WHERE CS.CITY = 'London' AND SH.COMPANY_NAME = 'United Package'



-- Наименование продукта, количество товара (product_name и units_in_stock в табл products), имя поставщика и его телефон (contact_name и phone в табл suppliers) для таких продуктов, которые не сняты с продажи (поле discontinued) и которых меньше 25 и которые в категориях Dairy Products и Condiments. Отсортировать результат по возрастанию количества оставшегося товара.
SELECT PD.product_name , PD.units_in_stock , SP.CONTACT_NAME , SP.PHONE
FROM PRODUCTS PD
JOIN SUPPLIERS SP USING(SUPPLIER_ID)
JOIN CATEGORIES CT USING(CATEGORY_ID)
WHERE PD.DISCONTINUED = 0 AND CT.CATEGORY_NAME IN ('Dairy Products', 'Condiments')
GROUP BY PD.units_in_stock, PD.product_name ,  SP.CONTACT_NAME , SP.PHONE
HAVING COUNT(*) < 25
ORDER BY COUNT(*)



-- Список компаний заказчиков (company_name из табл customers), не сделавших ни одного заказа
SELECT COMPANY_NAME FROM CUSTOMERS
WHERE CUSTOMER_ID NOT IN (SELECT CUSTOMER_ID FROM ORDERS)
