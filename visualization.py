import matplotlib.pyplot as plt
import pandas as pd

# Example data for sales performance in different regions
data = {'Region': ['North America', 'Europe', 'Asia-Pacific', 'Latin America', 'Middle East', 'Africa'],
        'Sales (in millions)': [450, 750, 1300, 580, 430, 42]}

sales_data = pd.DataFrame(data)

# Define a professional color palette
colors = ['#4C72B0', '#55A598', '#C44E52', '#8172B2', '#CCB974', '#64B5CD']

# Plotting a bar chart with customized colors and other professional elements
plt.figure(figsize=(12, 8))
bars = plt.bar(sales_data['Region'], sales_data['Sales (in millions)'], color=colors, edgecolor='black', linewidth=1.2)

# Adding data values on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, f"${int(yval)}M", ha='center', va='bottom', color='black', fontweight='bold')

# Adding labels and title
plt.title('Sales Performance by Region')
plt.xlabel('Region')
plt.ylabel('Sales (in millions)')

# Adding grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Rotating x-axis labels for better visibility
plt.xticks(rotation=45, ha='right')

# Adjusting layout
plt.tight_layout()

# Show the plot
plt.show()
