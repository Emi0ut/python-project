# 📌 Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📌 Load Dataset (you can replace with your own file)
# Example: Video Game Sales Dataset
df = pd.read_csv("/Users/abhimanyutarar/Downloads/Video_Games_Sales_as_at_22_Dec_2016.csv")


# 📌 Data Cleaning
df.dropna(inplace=True)

print(df.shape)

# Convert Year to integer
df['Year_of_Release'] = df['Year_of_Release'].astype(int)

print("Dataset Loaded Successfully ✅")
print(df.head())

# Set style
sns.set(style="whitegrid")

# -------------------------------
# 📊 1. Line Chart (Sales over Years)
# -------------------------------
year_sales = df.groupby('Year_of_Release')['Global_Sales'].sum()

plt.figure(figsize=(10,5))
plt.plot(year_sales.index, year_sales.values)
plt.title("Global Sales Over Years")
plt.xlabel("Year")
plt.ylabel("Sales (Millions)")
plt.show()

# -------------------------------
# 📊 2. Bar Chart (Top 10 Publishers)
# -------------------------------
top_publishers = df['Publisher'].value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_publishers.values, y=top_publishers.index)
plt.title("Top 10 Publishers")
plt.xlabel("Count")
plt.ylabel("Publisher")
plt.show()

# -------------------------------


# -------------------------------
# 📊 4. Scatter Plot (NA vs EU Sales)
# -------------------------------
na_total = df['NA_Sales'].sum()
eu_total = df['EU_Sales'].sum()

plt.bar(['NA Sales', 'EU Sales'], [na_total, eu_total])
plt.title("NA vs EU Total Sales")
plt.ylabel("Sales (Millions)")
plt.show()

# -------------------------------
# 📊 5. Box Plot (Sales by Genre)
# -------------------------------
genre_sales = df.groupby('Genre')['Global_Sales'].sum()

plt.figure(figsize=(6,6))
plt.pie(genre_sales, labels=genre_sales.index, autopct='%1.1f%%')
plt.title("Genre Contribution to Global Sales")
plt.show()

# -------------------------------
# 📊 6. Heatmap (Correlation)
# -------------------------------
corr = df[['NA_Sales','EU_Sales','JP_Sales','Global_Sales']].corr()

plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True)
plt.title("Sales Correlation Heatmap")
plt.show()

# -------------------------------
# 📊 7. Pie Chart (Genre Distribution)
# -------------------------------
genre_counts = df['Genre'].value_counts().head(5)

plt.figure(figsize=(6,6))
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%')
plt.title("Top 5 Genres Distribution")
plt.show()

print(df.shape)
