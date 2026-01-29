from typing import List, Dict, Any

from app.db import get_db_connection


def get_customers_by_credit_limit_range():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql1="""
    SELECT `customerName`,`creditLimit`
    FROM `customers`
    WHERE creditLimit > 100000 or creditLimit < 10000
    order by creditLimit DESC;
    """

    cursor.execute(sql1)
    q1=cursor.fetchall()
    cursor.close()
    conn.close()
    return q1


def get_orders_with_null_comments():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql2="""
            select orderNumber, comments 
            from orders
            where comments is null
            order by shippedDate;"""
    cursor.execute(sql2)
    q2 = cursor.fetchall()
    cursor.close()
    conn.close()
    return q2

def get_first_5_customers():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql3 = """
            select customerName, contactLastName, contactFirstName
            from customers
            order by contactLastName desc
            limit 5;'''
       """
    cursor.execute(sql3)
    q3 = cursor.fetchall()
    cursor.close()
    conn.close()
    return q3

def get_payments_total_and_average():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql4 = """
            select sum(amount) as sum_amount , avg(amount) as avg_amount, min(amount) as min_amount, max(amount) as max_amount
            from payments;
       """
    cursor.execute(sql4)
    q4 = cursor.fetchall()
    cursor.close()
    conn.close()
    return q4
def get_employees_with_office_phone():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql5 = """
            select e.firstName, e.lastName, o.phone
            from employees e
            join offices o
            on e.officeCode = o.officeCode
          """
    cursor.execute(sql5)
    q5 = cursor.fetchall()
    cursor.close()
    conn.close()
    return q5


def get_customers_with_shipping_dates():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql6 = """
            select c.customerName, o.shippedDate
            from customers c
            left join orders o
            on c.customerNumber = o.customerNumber;
              """
    cursor.execute(sql6)
    q6 = cursor.fetchall()
    cursor.close()
    conn.close()
    return q6

def get_customer_quantity_per_order():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql7 = """
             
    SELECT customers.customerName,
    orderdetails.quantityOrdered
    FROM customers
    INNER JOIN orders
    ON customers.customerNumber = orders.customerNumber
    INNER JOIN orderdetails
    ON orderdetails.orderNumber = orders.orderNumber
    ORDER BY customerName"""
    cursor.execute(sql7)
    q7 = cursor.fetchall()
    cursor.close()
    conn.close()
    return q7

def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql8 = """  
     
    SELECT c.customerName  ,
    e.firstName  ,
    SUM(p.amount) AS total
    FROM customers c
    JOIN employees e
    ON c.salesRepEmployeeNumber = e.employeeNumber
    JOIN payments p
    ON c.customerNumber = p.customerNumber
    WHERE c.contactFirstName LIKE '%Mu%' OR c.contactFirstName LIKE '%ly%'
    GROUP BY c.customerName, e.firstName
    ORDER BY total DESC;
    
                  """
    cursor.execute(sql8)
    q8 = cursor.fetchall()
    cursor.close()
    conn.close()
    return q8
