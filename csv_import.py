import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv ('2022Season.csv')
# print(df)
df.head()
df.plot()
plt.show()

# with open('2022Season.csv', newline='') as csvfile:
#     nflreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in nflreader:
#         print(', '.join(row))

