import pandas as pd

# Read CSV file
df = pd.read_csv("Data_Immersion_and_Wrangling/sales_data.csv",on_bad_lines='skip')

# Display dataset
print(df)

# Display first 5 rows
print(df.head())

# Check dataset information
print(df.info())

print(df.isnull().sum())

print(df.duplicated().sum())

print(df[df["Quantity"] < 1])

print(df[df["UnitPrice"] < 0])

print(df.describe())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows where Quantity is less than 1
df = df[df["Quantity"] >= 1]

# Remove rows where UnitPrice is negative
df = df[df["UnitPrice"] >= 0]

# Convert Date column into datetime format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

# Create a new Revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# # Save cleaned dataset
df.to_csv("Data_Immersion_and_Wrangling/sales_data_cleaned.csv", index=False)

print("Data cleaning completed successfully!")

# # Display cleaned dataset
print(df)

print(df.columns)