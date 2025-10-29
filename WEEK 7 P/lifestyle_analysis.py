import pandas as pd
import matplotlib.pyplot as plt

# Load dataset with absolute path
df = pd.read_csv(r"c:\Users\POPPA\OneDrive\Desktop\PLP\Final_data.csv")

# Display the first few rows
print("🔹 First 5 rows of the dataset:")
print(df.head(), "\n")

# Inspect structure and data types
print("🔹 Dataset Info:")
print(df.info(), "\n")

# Check for missing values
print("🔹 Missing Values in Each Column:")
print(df.isnull().sum(), "\n")

# Clean data: drop rows with missing values (or use fillna() if appropriate)
df = df.dropna()
print("✅ After cleaning, dataset shape:", df.shape, "\n")

# Descriptive statistics
print("📊 Basic Statistical Summary:")
print(df.describe(), "\n")

# Example grouping (adjust column names to match your dataset)
# Suppose there’s a categorical column 'Region' and a numeric column 'Income'
if 'Region' in df.columns and 'Income' in df.columns:
    grouped_data = df.groupby('Region')['Income'].mean().sort_values(ascending=False)
    print("🌍 Average Income by Region:")
    print(grouped_data, "\n")
else:
    print("⚠️ Adjust grouping column names according to your dataset.\n")

# 1️⃣ Line Chart – Trends Over Time
if 'Date' in df.columns and 'Steps' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values('Date', inplace=True)
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Steps'], color='teal')
    plt.title('Trend of Steps Over Time')
    plt.xlabel('Date')
    plt.ylabel('Steps')
    plt.grid(True)
    plt.show()

# 2️⃣ Bar Chart – Comparison Across Categories
if 'Region' in df.columns and 'Income' in df.columns:
    plt.figure(figsize=(8,5))
    grouped_data.plot(kind='bar', color='coral')
    plt.title('Average Income by Region')
    plt.xlabel('Region')
    plt.ylabel('Average Income')
    plt.show()

# 3️⃣ Histogram – Distribution of a Numerical Column
if 'Age' in df.columns:
    plt.figure(figsize=(8,5))
    plt.hist(df['Age'], bins=20, color='slateblue', edgecolor='black')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

# 4️⃣ Scatter Plot – Relationship Between Two Numerical Variables
if 'Height' in df.columns and 'Weight' in df.columns:
    plt.figure(figsize=(8,5))
    plt.scatter(df['Height'], df['Weight'], color='seagreen', alpha=0.6)
    plt.title('Relationship between Height and Weight')
    plt.xlabel('Height')
    plt.ylabel('Weight')
    plt.show()

print("✅ Visualization Complete — Data Analysis Finished.")
