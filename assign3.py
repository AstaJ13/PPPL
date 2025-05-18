import pandas as pd


df = pd.read_csv(r"C:\Users\astaj\Downloads\archive\advertising.csv")


column = "Daily Time Spent on Site"


mean = df[column].mean()
mode = df[column].mode()
median = df[column].median()

print(f"Mean of {column}: {mean}")
print(f"Mode of {column}: {mode.values.tolist()}")
print(f"Median of {column}: {median}")
