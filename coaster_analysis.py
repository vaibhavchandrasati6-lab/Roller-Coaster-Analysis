# Import required libraries for data analysis and visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('coaster.csv', encoding_errors='ignore')

# Display first few rows of dataset
print(df.head())

# Check dataset shape (rows, columns)
print(df.shape)

# Display column names
print(df.columns)

# Get dataset information (data types, null values)
print(df.info())


# Selecting only relevant columns for analysis
df = df[['coaster_name',
         'Location', 'Status', 'Manufacturer',
         'year_introduced', 'latitude', 'longitude',
         'Type_Main', 'opening_date_clean',
         'speed_mph', 'height_ft',
         'Inversions_clean', 'Gforce_clean']].copy()

print(df)
print(df.shape)


# Convert opening date column to datetime format
df['opening_date_clean'] = pd.to_datetime(df['opening_date_clean'])

print(df.info())


# Rename columns for better readability
df = df.rename(columns={
    'coaster_name': 'Coaster_Name',
    'year_introduced': 'Year_Introduced',
    'opening_date_clean': 'Opening_Date',
    'speed_mph': 'Speed_mph',
    'height_ft': 'Height_ft',
    'Inversions_clean': 'Inversions',
    'Gforce_clean': 'Gforce'
})

print(df)


# Check missing values in each column
print(df.isnull().sum())


# Remove duplicate records based on coaster name, location and opening date
df = df.drop_duplicates(subset=['Coaster_Name', 'Location', 'Opening_Date'])

print(df.shape)


# -----------------------------
# Data Visualization Section
# -----------------------------

# Top 10 years with most coaster introductions
data = df['Year_Introduced'].value_counts().head(10).sort_values().reset_index()

plt.figure(figsize=(10, 5))
sns.histplot(x='Year_Introduced', bins=10, data=data)
plt.title('Top 10 Years of Coasters Introduced')
plt.show()


# Distribution of coaster speed
plt.figure(figsize=(10, 5))
sns.histplot(x='Speed_mph', bins=10, data=df)
plt.title('Speed Distribution of Coasters (mph)')
plt.show()


# Relationship between height and speed
plt.figure(figsize=(10, 5))
sns.scatterplot(x='Height_ft', y='Speed_mph', data=df)
plt.title('Height vs Speed Analysis')
plt.xlabel('Height (ft)')
plt.ylabel('Speed (mph)')
plt.show()


# Height vs Speed with Year as color dimension
plt.figure(figsize=(10, 5))
sns.scatterplot(x='Height_ft', y='Speed_mph', hue='Year_Introduced', data=df)
plt.title('Height vs Speed with Year Introduced')
plt.xlabel('Height (ft)')
plt.ylabel('Speed (mph)')
plt.show()


# Pairplot to analyze relationships between multiple numerical variables
sns.pairplot(
    vars=['Year_Introduced', 'Speed_mph', 'Height_ft', 'Inversions', 'Gforce'],
    hue='Type_Main',
    data=df
)
plt.show()


# Correlation analysis between numerical features
df_corr = df[['Year_Introduced', 'Speed_mph', 'Height_ft', 'Inversions', 'Gforce']].dropna().corr()

plt.figure(figsize=(10, 5))
sns.heatmap(df_corr, annot=True)
plt.title('Correlation Heatmap')
plt.show()