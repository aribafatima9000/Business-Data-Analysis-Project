import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Order_ID": [101,102,103,104,105,106,107,108],
    "Date": pd.to_datetime([
        "2024-01-05","2024-01-10","2024-02-01","2024-02-15",
        "2024-03-01","2024-03-10","2024-03-20","2024-03-25"
    ]),
    "Region": ["East","West","East","South","North","West","North","South"],
    "Product": ["Laptop","Mobile","Tablet","Laptop","Mobile","Tablet","Laptop","Mobile"],
    "Sales": [50000,30000,20000,55000,32000,21000,60000,35000],
    "Cost": [40000,20000,15000,42000,25000,16000,48000,27000]
}

df = pd.DataFrame(data)
df
df["Profit"] = df["Sales"] - df["Cost"]
df
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
avg_order_value = df["Sales"].mean()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Average Order Value:", avg_order_value)

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
region_sales
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()
product_profit = df.groupby("Product")["Profit"].sum()
product_profit
product_profit.plot(kind="bar")
plt.title("Profit by Product")
plt.ylabel("Profit")
plt.show()
df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()
monthly_sales
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
top_product = df.groupby("Product")["Sales"].sum().idxmax()
print("Top Selling Product:", top_product)
print("""
Business Insights:
1. Best selling product identified
2. Most profitable region found
3. Monthly sales trend analyzed
4. Data-driven decisions possible
""")
