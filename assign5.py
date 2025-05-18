import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\astaj\Downloads\archive (2)\temperatures.csv")


df['YEAR'] = pd.to_numeric(df['YEAR'], errors='coerce')
df['JAN'] = pd.to_numeric(df['JAN'], errors='coerce')


plt.figure(figsize=(10, 5))
plt.plot(df['YEAR'], df['JAN'], marker='o', color='tab:blue', label='January')

plt.title('January Temperature Over Years', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
