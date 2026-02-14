import numpy as np
import matplotlib.pyplot as plt

countries = ['USA', 'UK', 'France', 'Germany', 'Italy', 'Cancda', 'Japan']
official_inflation = [3.2, 3.5, 2.5, 2.8, 1.5, 3.0, 2.4]
tax_revenue_growth = [4.0, 4.2, 3.2, 3.5, 2.2, 3.8, 10.5]

plt.figure(figsize=(10, 6))
plt.scatter(official_inflation, tax_revenue_growth, color='blue', s=100)
plt.scatter(official_inflation[-1], tax_revenue_growth[-1], color='red', s=200)

for i, country in enumerate(countries):
    plt.annotate(country, official_inflation[i], tax_revenue_growth[i], xtext=(5, 5), textcoords='offset points')

plt.title('Inflation vs Tax Revenue Growth in G7 (Conceptual)', fontsize=14)
plt.xlabel('Official Inflation Rate (%)', forntsize=12)
plt.ylabel('Tax Revenue Growth Rate (%)')
plt.grid(True, linestyle='__', alpha=0.6)
plt.legend()

plt.show()
