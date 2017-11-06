# 目标: 
''' 目标
    在这个比赛中，需要预测在厄瓜多尔Favorita地区各个商店中成千上万的商品的单位销量（销售额），
    训练数据包含了日期、商家及商品信息，以及是否在促销，以及对应的单位销量（销售额）。
'''

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


DIR = r"D:\PlayGround\kaggle\Grocery"

# 训练集
train = pd.read_csv(os.path.join(DIR, "train.csv"))

# train: shape = 125497040 x 6
# cols: id, date, store_nbr, item_nbr, unit_sales, onpromotion
""" columns: 
id: integer
日期: string
商店id: integer
商品id: integer
销量: float
在促销: boolean
"""

# 训练数据中的日期节日
holidays = pd.read_csv(os.path.join(DIR, "holidays_events.csv"))

# item_nbr, family, class, perishable
items = pd.read_csv(os.path.join(DIR, "items.csv"))

# date, dcoilwtico
oil = pd.read_csv(os.path.join(DIR, "oil.csv"))

# store_nbr, city, state, type, cluster
stores = pd.read_csv(os.path.join(DIR, "stores.csv"))

# id, date, store_nbr, item_nbr, onpromotion
test = pd.read_csv(os.path.join(DIR, "test.csv"))

# date, store_nbr, transactions
transactions = pd.read_csv(os.path.join(DIR, "transactions.csv"))

""" Tips
id    日期        商店            商品    促销    销量
            |               \                     \
        假期信息    商家信息    商品信息
        月份
        季节信息
        星期
        油价

* 大概能用假期信息估计促销信息？

"""
