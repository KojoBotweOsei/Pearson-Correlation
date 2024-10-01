import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load the dataset
file_path = "C:/Users/kbamp/Downloads/FeedbackLoopsRecording final.xlsx"
df = pd.read_excel(file_path)

print(df.columns)
# Clean and select relevant columns (replace with the correct column names)
df_clean = df[['FeedbackLoopPartTurn Taking', 'Interruptions']].dropna()

# Convert 'Feedback Loop Duration' to numeric if it's in a different format
df_clean['FeedbackLoopPartTurn Taking'] = pd.to_numeric(df_clean['FeedbackLoopPartTurn Taking'], errors='coerce')

# Double-check for missing values
print(f"Missing values: {df_clean.isnull().sum()}")

# Calculate Pearson correlation coefficient and p-value
correlation, p_value = pearsonr(df_clean['FeedbackLoopPartTurn Taking'], df_clean['Interruptions'])

# Display the correlation results
print(f"Correlation coefficient: {correlation}, p-value: {p_value}")

# R-squared is simply the square of the correlation coefficient
r_squared = correlation**2
print(f"R-squared: {r_squared}")

# Scatter plot with regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='FeedbackLoopPartTurn Taking', y='Interruptions', data=df_clean, scatter_kws={'alpha':0.5})
plt.title("Scatter Plot of FeedbackLoopPartTurn Taking vs. Interruptions")
plt.xlabel("FeedbackLoopPartTurn Taking ")
plt.ylabel("Number of Interruptions")
plt.grid()
plt.show()



