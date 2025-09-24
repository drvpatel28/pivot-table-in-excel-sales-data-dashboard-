import pandas as pd


# Load your data
df = pd.read_excel("SaleData.xlsx")
print(df.head())


# Check for duplicate rows
duplicates = df[df.duplicated()]
print(f"Number of duplicate rows: {duplicates.shape[0]}")
# View duplicate rows (optional)
print(duplicates)

# Remove duplicate rows
df_cleaned = df.drop_duplicates()
# Save to new Excel file
df_cleaned.to_excel("Cleaned_Data.xlsx",index=False)

# Check for missing values

print(df.isnull().sum())
