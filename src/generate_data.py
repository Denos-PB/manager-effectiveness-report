import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

manager_ids = list[int](range(1,11))
manager_data = {
    'ManagerID' : manager_ids,
    'Gender' : np.random.choice(['Male' , 'Female'] , size = 10),
    'Age': np.random.randint(25, 51, size=10),
    'WorkExperience': np.random.randint(1, 61, size=10)
}
df_managers = pd.DataFrame(manager_data)



customer_ids = list(range(1, 101))
customers_data = {
    'CustomerID': customer_ids,
    'Gender': np.random.choice(['Male', 'Female'], size=100),
    'Age': np.random.randint(25, 51, size=100)
}
df_customers = pd.DataFrame(customers_data)



num_orders = 1000

end_date = datetime.now()
start_date = end_date - timedelta(days=180)

def random_dates(start, end, n):
    start_u = int(start.timestamp())
    end_u = int(end.timestamp())
    return pd.to_datetime(np.random.randint(start_u, end_u, n), unit='s')

orders_data = {
    'OrderID': range(1, num_orders + 1),
    'CustomerID': np.random.choice(customer_ids, size=num_orders),
    'ManagerID': np.random.choice(manager_ids, size=num_orders),
    'OrderChannel': np.random.choice(['Web', 'Phone'], size=num_orders),
    'OrderDate': random_dates(start_date, end_date, num_orders).normalize(),
    'OrderSum': np.random.randint(1000, 5001, size=num_orders),
    'PaymentType': np.random.choice(['Online', 'Cash'], size=num_orders),
    'DeliveryType': np.random.choice(['Post1', 'Post2', 'Post3'], size=num_orders)
}

df_orders = pd.DataFrame(orders_data)

df_customers.to_csv('data/customers.csv', index=False)
df_orders.to_csv('data/orders.csv', index=False)
