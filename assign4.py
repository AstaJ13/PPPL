import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\astaj\Downloads\archive\advertising.csv")

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Clicked on Ad', hue='Male', palette='Set3')
plt.title('Ad Clicks by Gender')
plt.xlabel('Clicked on Ad (0 = No, 1 = Yes)')
plt.legend(title='Male')
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Daily Time Spent on Site', y='Age', hue='Clicked on Ad', palette='Set1')
plt.title('Time on Site vs Age by Ad Click')
plt.show()
