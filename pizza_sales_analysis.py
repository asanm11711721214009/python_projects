import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt

# Load CSV
pizdf = pd.read_csv("pizza_sales.csv")
print(pizdf)
print(pizdf.columns)
# Preview
pizdf.head()

total_revenue = pizdf["total_price"].sum()
print(total_revenue)

pizdf['total_revenue'] = pizdf['total_price'] * pizdf['quantity']

total_orders = pizdf["order_id"].nunique()
print(total_orders)

total_quantity = pizdf["quantity"].sum()
print(total_quantity)

average_order_value = total_revenue / total_orders
print(average_order_value)

avg_pizzas_per_order = total_quantity / total_orders
print(avg_pizzas_per_order)

pizdf['order_date'] = pd.to_datetime(pizdf['order_date'], dayfirst=True, errors='coerce')
pizdf['year'] = pizdf['order_date'].dt.year
pizdf['month'] = pizdf['order_date'].dt.month
pizdf['day'] = pizdf['order_date'].dt.day

pizdf['order_time'] = pd.to_datetime(pizdf['order_time'], format='%H:%M:%S', errors='coerce')

pizdf['hour'] = pizdf['order_time'].dt.hour
pizdf['minute'] = pizdf['order_time'].dt.minute
pizdf['second'] = pizdf['order_time'].dt.second

qty_hour_cat = (
    pizdf.groupby(['hour', 'pizza_category'])['quantity']
    .sum()
    .unstack()
    .fillna(0)
)

qty_hour_cat.plot(kind='bar', stacked=True)
plt.title("Total Quantity Sold by Hour & Pizza Category")
plt.xlabel("Hour")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.show()

rev_size = pizdf.groupby('pizza_size')['total_price'].sum()

plt.figure()
plt.pie(
    rev_size,
    labels=rev_size.index,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'width': 0.4}
)
plt.title("Total Revenue by Pizza Size")
plt.show()

revenue_by_pizza = (
    pizdf.groupby('pizza_name')['total_revenue']
      .sum()
      .sort_values(ascending=False)
)

plt.figure()
revenue_by_pizza.head(10).plot(kind='barh')
plt.title("Total Revenue by Pizza Name")
plt.xlabel("Revenue")
plt.ylabel("Pizza Name")
plt.gca().invert_yaxis()
plt.show()

orders_by_pizza = (
    pizdf.groupby('pizza_name')['order_id']
      .nunique()
      .sort_values(ascending=False)
)

plt.figure()
orders_by_pizza.head(10).plot(kind='barh')
plt.title("Total Orders by Pizza Name")
plt.xlabel("Number of Orders")
plt.ylabel("Pizza Name")
plt.gca().invert_yaxis()
plt.show()