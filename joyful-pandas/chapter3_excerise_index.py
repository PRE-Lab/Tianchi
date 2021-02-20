# -*- coding: utf-8 -*- 
# @Time : 2021/2/18 下午 03:56 
# @Author : Preh 
# @File : chapter3_excerise_index.py

import pandas as pd
import numpy as np

# df_reindex = pd.DataFrame({"Weight":[60,70,80], "Height":[176,180,179]}, index=['1001','1003','1002'])
# print(df_reindex)
# a = df_reindex.reindex(index=['1001','1002','1003','1004'], columns=['Weight','Gender'])
# print(a)

'''
深浅拷贝
'''
# import copy
# a = [1,2,3,[4,5],6]
# b = copy.copy(a)
# c = copy.deepcopy(a)
# a.append(7)
# a[3].append(8)
# print(f'a 原型:{a}')  #a 原型:[1, 2, 3, [4, 5, 8], 6, 7]
# print(f'b浅拷贝:{b}') #b浅拷贝:[1, 2, 3, [4, 5, 8], 6]
# print(f'c深拷贝:{c}') #c深拷贝:[1, 2, 3, [4, 5], 6]

'''
SA.intersection(SB)=SA∩SB⇔{x|x∈SAandx∈SB}
 
SA.union(SB)=SA∪SB⇔{x|x∈SAorx∈SB}
 
SA.difference(SB)=SA−SB⇔{x|x∈SAandx∉SB}
 
SA.symmetric_difference(SB)=SA△SB⇔{x|x∈SA∪SB−SA∩SB}
'''
# df_set_1 = pd.DataFrame([[0,1],[1,2],[3,4]], index = pd.Index(['a','b','a'],name='id1'))
# df_set_2 = pd.DataFrame([[4,5],[2,6],[7,1]], index = pd.Index(['b','b','c'],name='id2'))
# print(df_set_1)
# print(df_set_2)
# id1, id2 = df_set_1.index.unique(), df_set_2.index.unique()
# print(id1)
# print(id2)
# ex = id1.intersection(id2)
# print(ex)
# ex = id1.union(id2)
# print(ex)
# ex = id1.difference(id2)
# print(ex)
# ex = id1.symmetric_difference(id2)
# print(ex)

# df = pd.read_csv('./data/company.csv')
# print(df.head(10))

'''
1.分别只使用query和loc选出年龄不超过四十岁且工作部门为Dairy或Bakery的男性。
'''
# def condition(x):
#     condition_1 = x.age <= 40
#     condition_2 = x.department == 'Dairy'
#     condition_3 = x.department == 'Bakery'
#     condition = condition_2 & (condition_1 | condition_3)
#     return condition
# print(df.loc[condition])
#
# a = df.loc[condition]
# b = df.query('age <= 40 and (department == "Dairy" or department == "Bakery")')
# b = df.query('age <= 40 & (department == "Dairy" | department == "Bakery")')
# print(b)
# print(type(a))
# print(type(b))
'''
2.选出员工ID号 为奇数所在行的第1、第3和倒数第2列。
'''
# print(df.iloc[lambda x:df.index % 2 == 0,[0,2,-2]])
'''
3.按照以下步骤进行索引操作：
把后三列设为索引后交换内外两层
恢复中间层索引
修改外层索引名为Gender
用下划线合并两层行索引
把行索引拆分为原状态
修改索引名为原表名称
恢复默认索引并将列保持为原表的相对位置
'''
#把后三列设为索引后交换内外两层
# a = df.set_index(['department','job_title','gender'])
# print(a)
# b = a.reorder_levels([2,1,0],axis=0).sort_index()#reorder_levels，可进行任意交换
# b = a.swaplevel(2,0,axis=0).sort_index() #swaplevel 只能两两交换， axis=0,行交换，axis=1,列交换
# print(b.head(5))

# #恢复中间层索引
# b = a.droplevel([1],axis=0)
# print(b.head(5))
# #修改外层索引名为Gender
# c = b.rename(columns={'age':'Age'},level=0)#改变列索引名称
# c= c.rename_axis(index={'gender':'GENDER'})#改变行索引名称
# print(c)
# #用下划线合并两层行索引
# new_index = c.index.map(lambda x: (x[0]+'-'+x[1]))
# c.index = new_index
# print(c.head(5))
# #把行索引拆分为原状态
# new_index = c.index.map(lambda x: tuple(x.split('-')))
# c.index = new_index
# print(c.head(5))
# #修改索引名为原表名称
# c.rename_axis(index=['department','GENDER'])
# print(c.head(5))
# c.reset_index().reindex(df.columns, axis=1)
# print(c.head(5))
# print(df.equals(c))
# answer
# df_copy = df.copy()
# a = df_copy.set_index(df_copy.columns[-3:].tolist()).reorder_levels([2,1,0],axis=0)
# # print(a.head(5))
# b = a.reset_index(level=1).rename_axis(index={'gender':'Gender'})
# # print(b.head(5))
# b.index = b.index.map(lambda x:'-'.join(x))
# print(b.head(5))
# b.index = b.index.map(lambda x:tuple(x.split('-')))
# print(b.head(5))
# c=b.rename_axis(index=['gender','department'])
# print(c.head(5))
# d=c.reset_index().reindex(df.columns,axis=1)#reset_index是set_index的逆操作，恢复多级索引，reindex可对行列索引重新编排
# print(d.head(5))

'''
1. 把列索引名中的 \n 替换为空格。 
2. 巧克力 Rating 评分为 1 至 5，每 0.25 分一档，请选出 2.75 分及以下且可可含量 Cocoa Percent 高于 中位数的样本。
3. 将 Review Date 和 Company Location 设为索引后，选出 Review Date 在 2012 年之后且 Company Location 不属于 France, Canada, Amsterdam, Belgium 的样本。

'''
df = pd.read_csv('./data/chocolate.csv')
print(df.head(5))
print(df.columns.tolist())
df.columns = [' '.join(i.split('\r\n')) for i in df.columns]
df.columns = [i if '\n' not in i else i.replace('\r\n',' ')  for i in df.columns]
df['Cocoa Percent'] = df['Cocoa Percent'].apply(lambda x:float(x[:-1])/100)
print(df.query('(Rating<3)&(`Cocoa Percent`>`Cocoa Percent`.median())').head(3))#百分数转化成小数才可以
idx = pd.IndexSlice
exclude = ['France','Canada','Amsterdam','Belgium']
res = df.set_index(['Review Date', 'Company Location']).sort_index(level=0)
print(res.index.get_level_values(1))
res = res.loc[idx[2012:,~res.index.get_level_values(1).isin(exclude)],:]
print(res.head(5))
