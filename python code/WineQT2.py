import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the Wine Quality dataset
df = pd.read_csv('WineQT.csv')

# Define quality categories
high_quality = df[df['quality'] >= 7]
standard_quality = df[(df['quality'] >= 5) & (df['quality'] <= 6)]

# Key physiochemical features
features = [
    'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
    'pH', 'sulphates', 'alcohol'
]

# Compute the means for high-quality wines
high_means = high_quality[features].mean().round(2)

# Compute the means for standard wines
standard_means = standard_quality[features].mean().round(2)

# Create a comparison DataFrame
comparison = pd.DataFrame({
    'High-Quality Mean (>=7)': high_means,
    'Standard Mean (5-6)': standard_means
})

# Add sample sizes
print(f"High-Quality samples: {len(high_quality)}")
print(f"Standard samples: {len(standard_quality)}")
print("\nChemical Profiles Comparison:")
print(comparison)

# Create the bar chart for the comparison
x = np.arange(len(features))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 8))
rects1 = ax.bar(x - width/2, high_means, width, label='High-Quality (>=7)', color='#4CAF50')
rects2 = ax.bar(x + width/2, standard_means, width, label='Standard (5-6)', color='#FF9800')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Chemical Features')
ax.set_ylabel('Mean Value')
ax.set_title('Physicochemical Profiles Comparison: High-Quality vs Standard Wines')
ax.set_xticks(x)
ax.set_xticklabels(features, rotation=45, ha='right')
ax.legend()

# Attach a text label above each bar in *rects*, displaying its height.
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.show()
