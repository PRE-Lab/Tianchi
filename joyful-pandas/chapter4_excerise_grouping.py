# -*- coding: utf-8 -*- 
# @Time : 2021/2/19 下午 02:31 
# @Author : Preh 
# @File : chapter4_excerise_grouping.py

import pandas as pd


'''
1.先过滤出所属Country数超过2个的汽车，即若该汽车的Country在总体数据集中出现次数不超过2则剔除，再按Country分组计算价格均值、价格变异系数、该Country的汽车数量，其中变异系数的计算方法是标准差除以均值，并在结果中把变异系数重命名为CoV。
2.按照表中位置的前三分之一、中间三分之一和后三分之一分组，统计Price的均值。
3.对类型Type分组，对Price和HP分别计算最大值和最小值，结果会产生多级索引，请用下划线把多级列索引合并为单层索引。
4.对类型Type分组，对HP进行组内的min-max归一化。
5.对类型Type分组，计算Disp.与HP的相关系数。
'''
df = pd.read_csv('./data/car.csv')
print(df)
gb = df.groupby('Country')
print(gb.size())
#将Country出现次数不超过2的删除
a = gb.filter(lambda x: x.shape[0]>2)
# print(a)
gb = a.groupby(['Country'])['Price'].agg([('CoV',lambda x:x.std()/x.mean()),'mean','count'])
print(gb)

condition = ['Head']*20 + ['Mid']*20 + ['Tail']*20
print(df.groupby(condition)['Price'].mean())

res = df.groupby('Type').agg({'Price':['max'],'HP':['min']})
print(res)
res.columns = res.columns.map(lambda x: '_'.join(x))
print(res)

def normalize(s):
    s_min, s_max = s.min(), s.max()
    res = (s - s_min)/(s_max - s_min)
    return res
res = df.groupby('Type')['HP'].apply(normalize)
print(res)