# import pandas as pd

# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }

# myvar = pd.DataFrame(data)

# print(myvar)


# import pandas as pd

# data = {
#     "calories": [420, 380, 390, 123],
#     "duration": [50, 40, 45, 123]
# }

# # load data into a DataFrame object:
# df = pd.DataFrame(data)

# print(df)

# # refer to the row index:
# print('Printing row 0\n')
# print(df.loc[[1, 3]])


# import pandas as pd

# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data, index=["day1", "day2", "day3"])

# print(df)
# print(df.loc[['day1', 'day3']])


import pandas as pd

df = pd.read_csv('Xpress data.csv')

print(df)
