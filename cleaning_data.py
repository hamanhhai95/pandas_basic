import pandas as pd

df = pd.read_csv('dirtydata.csv')

print('\nBefore cleaning up:\n')
print(df)

x = df["Calories"].mode()[0]
print(x)

df["Calories"].fillna(x, inplace=True)


print('\nAfter cleaning up:\n')
print(df)
