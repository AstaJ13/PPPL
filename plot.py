import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data= pd.read_csv(r"C:\Users\astaj\Downloads\archive\advertising.csv")

print(data.columns)
print(data.head())

#Bar PLot

plt.figure(figsize=(5,4))
sns.countplot(data=data,x='Clicked on Ad',hue='Male')
plt.title("Gender vs Click")
plt.xlabel("Click Ad")
plt.ylabel("Male")
plt.legend()
plt.show()


#Scatter Plot

plt.figure(figsize=(5,4))
sns.scatterplot(data=data,x='Daily Time Spent on Site',y='Daily Internet Usage',hue='Clicked on Ad')
plt.title("Time vs Age")
plt.xlabel('Time')
plt.ylabel('Age')
plt.legend()
plt.show()



#Line Plot

plt.figure(figsize=(5,4))
plt.plot(data['Male'], data['Clicked on Ad'])
plt.title('Line Plot')
plt.xlabel('Age')
plt.ylabel('Time Spent')
plt.legend()
plt.show()
