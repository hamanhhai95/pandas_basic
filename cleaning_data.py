import pandas as pd

df = pd.read_csv('dirtydata.csv')

print('\nBefore cleaning up:\n')
print(df)

# x = df["Calories"].mode()[0]
# print(x)

# df["Calories"].fillna(x, inplace=True)


# print('\nAfter cleaning up:\n')
# print(df)

df['Date'] = pd.to_datetime(df['Date'])
df.dropna(subset=['Date'], inplace=True)
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)
df.drop_duplicates(inplace=True)

print(df)
print(df.duplicated())
