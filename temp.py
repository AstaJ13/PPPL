
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\astaj\Downloads\temp.csv")

df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

plt.figure(figsize=(10,6))
plt.plot(df['Year'], df['Average_Fahrenheit_Temperature'], label='Temperature (°F)', color='tab:blue')
plt.title('Average Temperature Over Years', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature (°F)', fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()



