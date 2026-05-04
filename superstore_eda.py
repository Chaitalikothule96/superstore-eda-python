# ================================
# Superstore EDA Project
# ================================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# -------------------------------
# 1. Data Loading
# -------------------------------

df = pd.read_csv("sample_superstore.csv",encoding="latin1")

# Display first 10 rows
print(df.head(10))

# Basic information
print("\nShape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nInfo:")
df.info()

# -------------------------------
# 2. Data Cleaning
# -------------------------------

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())
df.drop(columns=['Postal Code'],inplace=True)

# Check data types
print(df.dtypes)
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'],dayfirst=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# -------------------------------
# 3. Visualization
# -------------------------------

# --- Bar Charts ---

plt.figure(figsize=(6,4))
df["Category"].value_counts().plot(kind="bar")
plt.title("Category Distribution")
plt.show()

plt.figure(figsize=(6,4))
df["Segment"].value_counts().plot(kind="bar")
plt.title("Segment Distribution")
plt.show()

plt.figure(figsize=(6,4))
df["State"].value_counts().plot(kind="bar")
plt.title("State Distribution")
plt.show()

# --- Scatter Plots ---
plt.figure(figsize=(6,4))
sns.scatterplot(x="Sales",y="Profit",data=df)
plt.title("Sales vs Profit")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x="Discount",y="Profit",data=df)
plt.title("Discount vs Profit")
plt.show()

# --- Histograms ---
numeric_cols=["Sales","Profit","Quantity","Discount"]
df[numeric_cols].hist(figsize=(10,6))
plt.suptitle("Distribution of Numeric Variables")
plt.show()

# --- Heatmap ---
plt.figure(figsize=(6,4))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# -------------------------------
# 4. Outlier Detection
# -------------------------------

plt.figure(figsize=(10,4))
sns.boxplot(data=df[["Sales", "Profit", "Discount"]])
plt.title("Outlier Detection using Boxplots")
plt.show()