# Task 5: Data Analysis on CSV Files

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file using full path
try:
    df = pd.read_csv(r"C:\Users\manch\OneDrive\Desktop\sales.csv")
    print("CSV file loaded successfully.\n")
except FileNotFoundError:
    print("Error: sales.csv file not found.")
    exit()

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display shape
print("\nShape of DataFrame:")
print(df.shape)

# Display column names
print("\nColumn names:")
print(df.columns)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Calculate total sales by product
total_sales = df.groupby("Product")["Sales"].sum()

print("\nTotal Sales by Product:")
print(total_sales)

# Calculate overall total sales
overall_sales = df["Sales"].sum()
print("\nOverall Total Sales:", overall_sales)

# Calculate average sales
average_sales = df["Sales"].mean()
print("Average Sales:", average_sales)

# Create bar chart
plt.figure(figsize=(6,4))
total_sales.plot(kind="bar")

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

print("\nTask completed successfully.")