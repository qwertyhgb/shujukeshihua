import pandas as pd

data = pd.read_csv('./data/第四章数据/presidential_approval_rate.csv')

print(data['political_issue'])
print(data['support'])