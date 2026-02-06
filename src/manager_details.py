import pandas as pd
import matplotlib.pyplot as plt
from generate_data import df_customers,df_managers,df_orders

def get_experience_diap(months):
    if months <= 6:
        return 'до 6 місяців'
    elif 7 <= months <= 12:
        return '7-12'
    elif 12 <= months <= 24:
        return '12-24'
    else:
        return 'більше 2 років'

df_managers['Experience_diap'] = df_managers['WorkExperience'].apply(get_experience_diap)

df_managers.to_csv('data/managers.csv', index=False)

experienced_mgr_ids = df_managers.loc[
    df_managers['Experience_diap'] == 'більше 2 років', 'ManagerID'
].tolist()

df_filtered = df_orders[df_orders['ManagerID'].isin(experienced_mgr_ids)].copy()
df_filtered = df_filtered.merge(
    df_customers[['CustomerID', 'Age']],
    on='CustomerID',
    how='left'
)

def get_client_age_group(age):
    if age <= 35:
        return 'до 35 років'
    elif 36 <= age <= 42:
        return '36-42 роки'
    else:
        return 'від 43 років'

age_series = pd.Series(df_filtered['Age'])
df_filtered['ClientAgeGroup'] = age_series.apply(get_client_age_group)

grouped_stats = df_filtered.groupby(['ClientAgeGroup', 'DeliveryType'])['OrderSum'].agg(
    Average_Order='mean',
    Median_Order='median'
)

grouped_stats.to_csv('data/grouped_analysis.csv')

df_orders['MonthYear'] = df_orders['OrderDate'].dt.to_period('M')

orders_trend = df_orders.groupby('MonthYear').size()

plt.figure(figsize=(10, 6))
orders_trend.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Динаміка кількості замовлень по місяцях')
plt.xlabel('Місяць')
plt.ylabel('Кількість замовлень')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('graph/orders_trend.png')
plt.show()