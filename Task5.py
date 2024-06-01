import pandas as pd
import matplotlib.pyplot as plt

# Load the accident dataset
accident_data = pd.read_csv("C:\\Users\\aarth\\OneDrive\\Documents\\cleaned.csv")

# Data Cleaning
# Handle missing values if any
accident_data.dropna(inplace=True)


# Visualize distribution of variables

plt.figure(figsize=(12, 6))
accident_data['Road_surface_type'].value_counts().plot(kind='bar')
plt.title('Distribution of Road Surface Type')
plt.xlabel('Road Surface Type')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
accident_data['Weather_conditions'].value_counts().plot(kind='bar')
plt.title('Distribution of Weather Conditions')
plt.xlabel('Weather Conditions')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
accident_data['Light_conditions'].value_counts().plot(kind='bar')
plt.title('Distribution of Light Conditions')
plt.xlabel('Light Conditions')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# Visualize contributing factors
plt.figure(figsize=(12, 6))
accident_data['Cause_of_accident'].value_counts().plot(kind='bar')
plt.title('Distribution of Accident Causes')
plt.xlabel('Cause of Accident')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=90)
plt.show()
