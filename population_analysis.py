# Step 1: Import Pandas library
import pandas as pd

# Step 2: Load the CSV dataset
df = pd.read_csv("population_data.csv")

# Step 3: Display the dataset
print("INDIA POPULATION AGE DISTRIBUTION")
print(df)

# Step 4: Display first five rows
print("\nFirst Five Rows:")
print(df.head())

# Step 5: Check dataset information
print("\nDataset Information:")
print(df.info())

# Step 6: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 7: Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Step 8: Statistical Analysis
print("\nStatistical Summary:")
print(df["Population_Percentage"].describe())

# Step 9: Check total population percentage
total = df["Population_Percentage"].sum()

print("\nTotal Population Percentage:", total)

# Step 10: Create Population Distribution Bar Chart

import matplotlib.pyplot as plt

# Set chart size
plt.figure(figsize=(10, 6))

# Create bar chart
bars = plt.bar(
    df["Age_Group"],
    df["Population_Percentage"],
    color=["skyblue", "orange", "green", "royalblue", "purple"]
)

# Add chart title and labels
plt.title("India Population Distribution by Age Group (2022)",
          fontsize=15, fontweight="bold")

plt.xlabel("Age Groups", fontsize=12)
plt.ylabel("Population Percentage (%)", fontsize=12)

# Set Y-axis limit
plt.ylim(0, 75)

# Add percentage values above bars
for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 1,
        f"{height}%",
        ha="center",
        fontsize=11
    )

# Add grid
plt.grid(axis="y", linestyle="--", alpha=0.4)

# Adjust layout
plt.tight_layout()

# Save chart as image
plt.savefig("population_distribution.png", dpi=300)

# Display chart
plt.show()

