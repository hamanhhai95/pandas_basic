# import pandas as pd

# df = pd.read_csv('data.csv')

# # print(len(df))
# my_index = [x for x in range(0, len(df), 2)]
# # print(my_index)

# print(df.tail())


import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())
print('Additional info below \n')

print(df.info())


# import pandas as pd

# print(pd.options.display.max_rows)
