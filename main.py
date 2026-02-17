import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Load the data
df = pd.read_csv('Grammy_Awards_Winners_20260208_055452.csv')

# --- PART 1: INTERACTIVE TERMINAL SEARCH ---
print("=== Grammy Award Search Tool ===")
user_input = input("Enter a year (e.g., 2020): ")

try:
    # Convert input to integer
    search_year = int(user_input)
    
    # Filter data based on year
    results = df[df['Year'] == search_year][['Artist', 'Category', 'Winner']]
    
    if not results.empty:
        print(f"\nResults for the year {search_year}:")
        print("-" * 50)
        # Displaying the list of winners
        for index, row in results.iterrows():
            print(f"Artist: {row['Artist']} | Award: {row['Category']}")
        print("-" * 50)
    else:
        print(f"No records found for the year {search_year}.")

except ValueError:
    print("Invalid input! Please enter a four-digit number for the year.")


# --- PART 2: GRAPH GENERATION ---
# This creates a bar chart of how many awards were given in each decade
plt.figure(figsize=(10, 6))
decade_counts = df['Decade'].value_counts().sort_index()
decade_counts.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Grammy Awards Distributed by Decade', fontsize=14)
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Number of Awards', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('awards_by_decade.png')
print("\n[Graph saved as 'awards_by_decade.png']")


# --- PART 3: SCICKIT-LEARN & NUMPY ---
# A simple example predicting the next Ceremony Number based on the Year
X = df[['Year']].values # Features (NumPy Array)
y = df['Ceremony_Number'].values # Target

model = LinearRegression()
model.fit(X, y)

next_year = np.array([[2027]])
predicted_ceremony = model.predict(next_year)
print(f"ML Prediction: The year 2027 will likely be Ceremony #{int(predicted_ceremony[0])}")