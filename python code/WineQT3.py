import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = "/Users/mac/Desktop/DA projects/Wine Quality Project/WineQT.csv"  # Update path if needed
wine_data = pd.read_csv(file_path)

# Analyze quality distribution
quality_distribution = wine_data['quality'].value_counts().sort_index()
quality_percentage = (quality_distribution / len(wine_data)) * 100

# Display results in console
print("Wine Quality Distribution:")
print(quality_distribution)
print("\nPercentage Distribution:")
print(quality_percentage.round(2))

# Plot bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(quality_distribution.index, quality_distribution.values, color='maroon', alpha=0.7)

# Add labels
for i, val in enumerate(quality_distribution.values):
    plt.text(quality_distribution.index[i], val + 5, f"{quality_percentage.iloc[i]:.1f}%", 
             ha='center', fontsize=10)

plt.title("Distribution of Wine Quality", fontsize=14, weight='bold')
plt.xlabel("Wine Quality Score")
plt.ylabel("Number of Wines")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Interpretation Summary
print("\nInterpretation:")
print("- Most wines are of average quality (scores 5–6), making up about 83% of the dataset.")
print("- High-quality wines (7–8) are about 14%, suitable for premium marketing.")
print("- Low-quality wines (3–4) are rare (~3%), suggesting limited production or blending use.")
