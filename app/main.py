from fastapi import FastAPI

from app.dal import *
from db_init import init_database

app = FastAPI()

init_database()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/q1/customers-credit-limit-outliers")
def customers_credit_limit_outliers():
    result = get_customers_by_credit_limit_range()
    return result

@app.get("/q2/orders-null-comments")
def orders_null_comments():
    result = get_orders_with_null_comments()
    return result

@app.get("/q3/customers-first-5")
def customers_first_5():
    result =get_first_5_customers()
    return result

@app.get("/q4/payments-total-average")
def payments_total_average():
    result =get_payments_total_and_average()
    return result

@app.get("/q5/employees-office-phone")
def employees_office_phone():
    result =get_employees_with_office_phone()
    return result

@app.get("/q6/customers-shipping-dates")
def customers_shipping_dates():
    result =get_customers_with_shipping_dates()
    return result

@app.get("/q7/customer-quantity-per-order")
def customer_quantity_per_order():
    result =get_customer_quantity_per_order()
    return result

@app.get("/q8/customers-payments-by-lastname-pattern")
def customers_payments_by_lastname_pattern(pattern: str = "son"):
    result =get_customers_payments_by_lastname_pattern()
    return result
