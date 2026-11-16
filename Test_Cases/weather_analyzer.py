
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Load CSV file
filename = input("Enter CSV file name: ")

if not os.path.exists(filename):
    print(f"Error: File '{filename}' not found. Please enter a valid file name.")
    exit()

df = pd.read_csv(filename)

# Check required columns
required = ["Date", "Temp", "Humidity", "Rainfall"]

if not all(col in df.columns for col in required):
    print("Error: CSV must contain Date, Temp, Humidity and Rainfall.")
    exit()

# Convert data types
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

for col in ["Temp", "Humidity", "Rainfall"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove duplicate rows
original_rows = len(df)
df = df.drop_duplicates()
duplicates_removed = original_rows - len(df)

# Remove rows with missing dates
df = df.dropna(subset=["Date"])

# Fill missing numeric values with column mean
missing_temp = df["Temp"].isna().sum()

for col in ["Temp", "Humidity", "Rainfall"]:
    if df[col].isna().any():
        mean_value = df[col].mean()
        df[col] = df[col].fillna(
            mean_value if pd.notna(mean_value) else 0
        )

print("\nWeather Data Analyzer")
print("---------------------")

while True:
    print("\n1. Summary")
    print("2. Clean & Plot")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nWeather Summary")

        print(f"Average Temp: {df['Temp'].mean():.2f} C")
        print(f"Max Temp: {df['Temp'].max():g} C")
        print(f"Min Temp: {df['Temp'].min():g} C")

        max_date = df.loc[df["Temp"].idxmax(), "Date"]
        min_date = df.loc[df["Temp"].idxmin(), "Date"]

        print(f"Max Date: {max_date.strftime('%Y-%m-%d')}")
        print(f"Min Date: {min_date.strftime('%Y-%m-%d')}")

        print(f"Std Dev: {np.std(df['Temp']):.2f}")
        print(f"Total Rainfall: {df['Rainfall'].sum():g} mm")

    elif choice == "2":

        print("\nData Cleaning Report")
        print(f"Duplicates removed: {duplicates_removed}")
        print(f"Missing Temp filled: {missing_temp}")
        print(f"Cleaned rows: {len(df)}")

        # Line chart
        plt.figure(figsize=(8, 5))
        plt.plot(df["Date"], df["Temp"], marker="o")
        plt.title("Temperature Trend")
        plt.xlabel("Date")
        plt.ylabel("Temperature (C)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        print("Line chart 'Temperature Trend' displayed")

        # Bar chart
        plt.figure(figsize=(8, 5))
        plt.bar(df["Date"].dt.strftime("%Y-%m-%d"),
                df["Rainfall"])
        plt.title("Rainfall Analysis")
        plt.xlabel("Date")
        plt.ylabel("Rainfall (mm)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        print("Bar chart 'Rainfall Analysis' displayed")

    elif choice == "3":
        print("Thank you for using Weather Data Analyzer!")
        break

    else:
        print("Invalid choice. Please enter 1, 2 or 3.")
