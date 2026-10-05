import pandas as pd

#load the dataset
df = pd.read_csv("C:\\Users\\HP\\OneDrive\\文档\\GitHub\\internship\\week_4\\ecommerce_sales_analysis\\data\\sales_data.csv")

print("=" * 50)
print("          E-COMMERCE SALES ANALYSIS          ")
print("=" * 50)

#Display first five rows of the dataset
print("\nFirst five rows of the dataset:")
print(df.head())

#Display dataset shape
print("\n Dataset shape:")
print(df.shape)

#Display column names
print("\nColumn names:")
print(df.columns.tolist())

#Display data types
print("\nData Types:")
print(df.dtypes)

#Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

#Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())



# ==========================================
#           DATA EXPLORATION
# ==========================================

print("\n" + "=" * 50)
print("          DATA EXPLORATION          ")
print("=" * 50)

#Statistical summary
print("\nStatistical Summary:")
print(df.describe())

#Unique products
print("\nUnique Products:")
print(df['Product'].unique())

#Number of products
print("\nNumber of Products:")
print(df['Product'].nunique())

#Number of regions
print("\nNumber of Regions:")
print(df['Region'].unique())

#Number of Customers
print("\nNumber of Customers:")
print(df['Customer_ID'].nunique())

#Total quantity sold
print("\nTotal Quantity Sold:")
print(df['Quantity'].sum())

#Total Sales
print("\nTotal Sales:")
print(df['Total_Sales'].sum())

#Average Sales
print("\nAverage Sale:")
print(df['Total_Sales'].mean())


# ==========================================
#           DATA CLEANING
# ==========================================


print("\n" + "=" * 50)
print("          DATA CLEANING          ")
print("=" * 50)

#Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

#Check missing values
print("\nMissing Values after cleaning:")
print(df.isnull().sum())

#Check duplicate rows
print("\nDuplicate Rows after cleaning:")
print(df.duplicated().sum())

#Check updated data types
print("\nData Types after cleaning:")
print(df.dtypes)

#Check for invalid quantities
print("\nInvalid Quantities:")
print(df[df["Quantity"] <= 0])

#Check for invalid prices
print("\nInvalid Prices:")
print(df[df["Price"] <= 0])

#Check for invalid total sales
print("\nInvalid Total Sales:")
print(df[df["Total_Sales"] <= 0])



# ==========================================
#           BASIC SALES ANALYSIS
# ==========================================

print("\n" + "=" * 50)
print("          BASIC SALES ANALYSIS          ")
print("=" * 50)

#Total Revenue
total_revenue = df["Total_Sales"].sum()

#Total quantity sold
total_quantity = df["Quantity"].sum()

#Average sale
average_sale = df["Total_Sales"].mean()

#Sales by product
product_sales = df.groupby("Product")["Total_Sales"].sum()

#Quantity sold by product
product_quantity = df.groupby("Product")["Quantity"].sum()

#Sales by region
region_sales = df.groupby("Region")["Total_Sales"].sum()

#Best-performing product by revenue
best_product = product_sales.idxmax()
best_product_sales = product_sales.max()

#Best-performing region
best_region = region_sales.idxmax()
best_region_sales = region_sales.max()

#Display overall metrics
print(f"\nTotal Revenue:: ${total_revenue:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Average Sale: ${average_sale:,.2f}")

#Display product analysis
print("\nSales by Product:")
print(product_sales)

print("\nQuantity Sold by Product:")
print(product_quantity)

#Display regional analysis
print("\nSales by Region:")
print(region_sales)

#Display best performers
print(f"\nBest Performing Product: {best_product} with Sales: ${best_product_sales:,.2f}")
print(f"Product Revenue: ${best_product_sales:,.2f}")

print(f"\nBest Performing Region: {best_region}")
print(f"Region Revenue: ${best_region_sales:,.2f}")


# ==========================================
#           DATA VISUALIZATION
# ==========================================

import matplotlib.pyplot as plt

print("\n" + "=" * 50)
print("          DATA VISUALIZATION          ")
print("=" * 50)

# ------------------------------------------
#   BAR CHART - SALES BY PRODUCT
# ------------------------------------------

plt.figure(figsize=(8,5))

product_sales.plot(kind = "bar")

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("C:\\Users\\HP\\OneDrive\\文档\\GitHub\\internship\\week_4\\ecommerce_sales_analysis\\visualizations\\sales_by_product.png")
plt.show()


# ------------------------------------------
#   LINE CHART - SALES OVER TIME
# ------------------------------------------

daily_sales = df.groupby("Date")["Total_Sales"].sum()

plt.figure(figsize=(10,5))

daily_sales.plot(kind = "line", marker="o")

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("C:\\Users\\HP\\OneDrive\\文档\\GitHub\\internship\\week_4\\ecommerce_sales_analysis\\visualizations\\daily_sales_trend.png")
plt.show()

# ------------------------------------------
#   PIE CHART - SALES BY REGION
# ------------------------------------------

plt.figure(figsize=(7,7))

region_sales.plot(kind = "pie", autopct = "%1.1f%%")

plt.title("Sales Distribution by Region")
plt.ylabel("")  # Hide y-label for pie chart
plt.tight_layout()

plt.savefig("C:\\Users\\HP\\OneDrive\\文档\\GitHub\\internship\\week_4\\ecommerce_sales_analysis\\visualizations\\sales_by_region.png")
plt.show()

print("\nCharts created and saved in the 'visualizations' folder.")
