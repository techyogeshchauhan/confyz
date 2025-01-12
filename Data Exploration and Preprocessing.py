import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = "C:\Users\yc993\Downloads\confyz taskj\Dataset .csv"  # Replace with your file path
data = pd.read_csv(file_path)

# 1. Identify the number of rows and columns
rows, columns = data.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")

# 2. Check for missing values
missing_values = data.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# Handle missing values (example: fill numeric columns with the mean)
data.fillna(data.mean(numeric_only=True), inplace=True)

# Optionally fill non-numeric columns with the mode
for column in data.select_dtypes(include=['object']).columns:
    data[column].fillna(data[column].mode()[0], inplace=True)

# 3. Perform data type conversion if necessary
print("Data types before conversion:")
print(data.dtypes)

# Example: Convert a column to numeric (if needed)
# data['column_name'] = pd.to_numeric(data['column_name'], errors='coerce')

print("Data types after conversion:")
print(data.dtypes)

# 4. Analyze the distribution of the target variable
target_variable = "Aggregate rating"
if target_variable in data.columns:
    plt.figure(figsize=(8, 6))
    sns.histplot(data[target_variable], kde=True, bins=20, color="skyblue")
    plt.title("Distribution of Aggregate Rating")
    plt.xlabel(target_variable)
    plt.ylabel("Frequency")
    plt.show()

    # Check for class imbalance
    print("Value counts for target variable:")
    print(data[target_variable].value_counts())
else:
    print(f"Target variable '{target_variable}' not found in the dataset.")
