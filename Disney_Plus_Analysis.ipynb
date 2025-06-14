# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv('disney_plus_titles.csv')
df
# Display first few rows
print(df.head())
# Using pandas - Basic data exploration
print("\nDataset Info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())
# Using numpy - some basic statistics (example on duration column if available)
# First, check if 'duration' column exists
if 'duration' in df.columns:
    # Extract numbers from duration (assuming format like '90 min')
    df['duration_num'] = df['duration'].str.extract('(\d+)').astype(float)
    print("\nDuration statistics:")
    print(f"Mean duration: {np.mean(df['duration_num'])}")
    print(f"Median duration: {np.median(df['duration_num'])}")
    print(f"Standard deviation: {np.std(df['duration_num'])}")
# Using matplotlib - simple plot (example: count of movies vs TV shows)
plt.figure(figsize=(6,4))
df['type'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
plt.title("Count of Titles by Type")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()
# If release_year column exists, plot number of titles over the years
if 'release_year' in df.columns:
    plt.figure(figsize=(10,6))
    df['release_year'].value_counts().sort_index().plot(kind='line')
    plt.title("Number of Titles by Release Year")
    plt.xlabel("Release Year")
    plt.ylabel("Number of Titles")
    plt.show()
