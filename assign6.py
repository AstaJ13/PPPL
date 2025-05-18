import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.read_csv(r"C:\Users\astaj\Downloads\archive (4)\student_exam_data_new.csv")

X = df[['Study Hours']]
y = df['Pass/Fail']

trainx, testx, trainy, testy = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(trainx, trainy)


predy = model.predict(testx)

plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.xlabel("Study Hours")
plt.ylabel("Pass/Fail (0/1)")
plt.title("Linear Regression: Study Hours vs Pass/Fail")
plt.legend()
plt.show()
