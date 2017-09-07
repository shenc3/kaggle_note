# -*- coding: utf-8 -*-

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# load data
print("load data...")
DIR = r'D:\PlayGround\kaggle\WebTraffic'
train = pd.read_csv(os.path.join(DIR, 'train_1.csv')).fillna(0)
# keys = pd.read_csv(os.path.join(DIR, 'key_1.csv'))

# 用最后60天的median作为后60天的预测，如果有效数据小于60，则按照具体数据来计算
end = train.shape[1]  # 550
start_idx = end - 60 + 1
visits = []

# 对每一篇文章求访问量的60天中位数
print("开始计算中位数...")
for i in range(train.shape[0]):
    print("Processing Page # %d..." % i, end='\r')
    row = train.iloc[i, 1:]
    
    start = row.nonzero()[0]
    if (start == 0).all():
        start = 0
    else:
        start = start[0]

    if start_idx < start:
        visits.append(np.round(np.median(row[start:])))
    else:
        visits.append(np.round(np.median(row[start_idx:])))

print("合并keys和train...")
train['Visits'] = pd.Series(visits)
train[['Page', 'Visits']].to_csv(os.path.join(DIR, 'train_median_60days.csv'), index=False)
'''
keys['Page'] = keys['Id'].str[:-11]

keys = keys.merge(train, how='left', on='Page')

print("保存输出submission...")
keys[['Id', 'Visits']].to_csv(os.path.join(DIR, 'sub_median_base.csv'), index=False)
'''