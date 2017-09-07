# -*- coding: utf-8 -*-

import os
import pandas as pd
import numpy as np


print("导入数据...")
DIR = r'E:\Projects\kaggle\WebTraffic'
train_visits = pd.read_csv(os.path.join(DIR, 'train_median_60days.csv'), encoding='gbk')
keys = pd.read_csv(os.path.join(DIR, 'key_1.csv'))

keys['Page'] = keys['Page'].str[:-11]
keys = keys.merge(train_visits, how='left', on='Page').fillna(0)

print("保存输出submission...")
keys[['Id', 'Visits']].to_csv(os.path.join(DIR, 'sub_median_base.csv'), index=False)
