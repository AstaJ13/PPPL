import pandas as pd
import random

# Creating a Pandas Series and performing basic statistics
l = [1, 2, 3.3]
b = pd.Series(l, index=['a', 'b', 'c'])
print(b)

print("Mean:", b.mean())
print("Median:", b.median())
print("Mode:\n", b.mode())

# Creating a Pandas DataFrame
data = {
    'name': ["Asta", "Dodo", "Riya"],
    'age': [19, 12, 34],
    'class': [12, 11, 10]
}
df = pd.DataFrame(data, index=['x', 'y', 'z'])
print(df)

# Printing dictionary in series
s = pd.Series(data)
print(s)

# Printing random numbers
print("Random Numbers:", random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
    