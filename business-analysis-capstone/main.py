# =====================================
# CAPSTONE PROJECT
# Real World Business Analysis
# =====================================

import pandas as pd
import matplotlib.pyplot as plt

print("Starting Business Analysis Project...")

# -----------------------------
# LOAD DATA
# -----------------------------
sales = pd.read_csv("data/sales_data.csv")
house = pd.read_csv("data/house_prices.csv")
churn = pd.read_csv("data/customer_churn.csv")

print("Datasets Loaded")

# -----------------------------
# DATA CLEANING
# -----------------------------
sales["Date"] = pd.to_datetime(sales["Date"])

# Feature Engineering
sales["Revenue_Category"] = pd.cut(
    sales["Total_Sales"],
    bins=3,
    labels=["Low", "Medium", "High"]
)

# -----------------------------
# SALES ANALYSIS
# -----------------------------
total_revenue = sales["Total_Sales"].sum()

plt.figure()
sales["Total_Sales"].hist()
plt.title("Sales Distribution")
plt.show()

# -----------------------------
# HOUSE PRICE ANALYSIS
# -----------------------------
avg_house_price = house["Price"].mean()

plt.figure()
house["Price"].hist()
plt.title("House Price Distribution")
plt.show()

plt.figure()
plt.scatter(house["Area"], house["Price"])
plt.title("Area vs Price")
plt.show()

# -----------------------------
# CUSTOMER CHURN ANALYSIS
# -----------------------------
churn_rate = churn["Churn"].mean() * 100

plt.figure()
churn["Churn"].value_counts().plot(kind="bar")
plt.title("Customer Churn Count")
plt.show()

# -----------------------------
# VALIDATION TESTS
# -----------------------------
assert sales["Total_Sales"].min() >= 0
assert churn["Churn"].isin([0,1]).all()
assert house["Price"].min() > 0

print("Validation Tests Passed")

# -----------------------------
# SAVE CLEAN DATA
# -----------------------------
sales.to_csv("data/cleaned_sales.csv", index=False)
house.to_csv("data/cleaned_house.csv", index=False)
churn.to_csv("data/cleaned_churn.csv", index=False)

# -----------------------------
# FINAL SUMMARY
# -----------------------------
print("\n===== BUSINESS SUMMARY =====")
print("Total Revenue:", total_revenue)
print("Average House Price:", avg_house_price)
print("Churn Rate:", round(churn_rate,2), "%")

print("\nProject Completed Successfully!")