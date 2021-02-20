# -*- coding: utf-8 -*- 
# @Time : 2021/2/20 上午 11:40 
# @Author : Preh 
# @File : chapter5_excerise_changing.py

import pandas as pd
import numpy as np

# df = pd.DataFrame({'Class':[1,1,2,2],
#                    'Name':['San Zhang','San Zhang','Si Li','Si Li'],
#                    'Subject':['Chinese','Math','Chinese','Math'],
#                    'Grade':[80,75,90,85]})
# print(df)
#
# print(df.pivot(index='Name',columns='Subject',values='Grade'))

# df = pd.DataFrame({'Class':[1, 1, 2, 2, 1, 1, 2, 2],
#                    'Name':['San Zhang', 'San Zhang', 'Si Li', 'Si Li',
#                               'San Zhang', 'San Zhang', 'Si Li', 'Si Li'],
#                    'Examination': ['Mid', 'Final', 'Mid', 'Final',
#                                     'Mid', 'Final', 'Mid', 'Final'],
#                    'Subject':['Chinese', 'Chinese', 'Chinese', 'Chinese',
#                                  'Math', 'Math', 'Math', 'Math'],
#                    'Grade':[80, 75, 85, 65, 90, 85, 92, 88],
#                    'rank':[10, 15, 21, 15, 20, 7, 6, 2]})
# print(df)
# print(df.pivot(index=['Class','Name','Subject'],columns=['Examination'],values=['Grade','rank']))

# df = pd.DataFrame({'Name':['San Zhang', 'San Zhang',
#                               'San Zhang', 'San Zhang',
#                               'Si Li', 'Si Li', 'Si Li', 'Si Li'],
#                    'Subject':['Chinese', 'Chinese', 'Math', 'Math',
#                                  'Chinese', 'Chinese', 'Math', 'Math'],
#                    'Grade':[80, 90, 100, 90, 70, 80, 85, 95]})
# print(df)
# print(df.pivot_table(index = 'Name',
#                columns = 'Subject',
#                values = 'Grade',
#                aggfunc = 'mean',margins=True))

# df = pd.DataFrame({'Class':[1,2],
#                    'Name':['San Zhang', 'Si Li'],
#                    'Chinese':[80, 90],
#                    'Math':[80, 75]})
# print(df)
# df_melted = df.melt(id_vars = ['Class', 'Name'],
#                     value_vars = ['Chinese', 'Math'],
#                     var_name = 'Subject',
#                     value_name = 'Grade')
# print(df_melted)
# df_unmelted = df_melted.pivot(index=['Class','Name'],columns='Subject',values='Grade')
# print(df_unmelted)
# df_unmelted = df_unmelted.reset_index().rename_axis(columns={'Subject':''})
# print(df_unmelted)

# df = pd.DataFrame({'Class':[1,2],'Name':['San Zhang', 'Si Li'],
#                    'Chinese_Mid':[80, 75], 'Math_Mid':[90, 85],
#                    'Chinese_Final':[80, 75], 'Math_Final':[90, 85]})
# print(df)
# print(pd.wide_to_long(df,
#                 stubnames=['Chinese', 'Math'],
#                 i = ['Class', 'Name'],
#                 j='Examination',
#                 sep='_',
#                 suffix='.+'))

# df = pd.DataFrame({'Class':[1, 1, 2, 2, 1, 1, 2, 2],
#                    'Name':['San Zhang', 'San Zhang', 'Si Li', 'Si Li',
#                               'San Zhang', 'San Zhang', 'Si Li', 'Si Li'],
#                    'Examination': ['Mid', 'Final', 'Mid', 'Final',
#                                     'Mid', 'Final', 'Mid', 'Final'],
#                    'Subject':['Chinese', 'Chinese', 'Chinese', 'Chinese',
#                                  'Math', 'Math', 'Math', 'Math'],
#                    'Grade':[80, 75, 85, 65, 90, 85, 92, 88],
#                    'rank':[10, 15, 21, 15, 20, 7, 6, 2]})
# pivot_multi = df.pivot(index = ['Class', 'Name'],
#                        columns = ['Subject','Examination'],
#                        values = ['Grade','rank'])
# print(pivot_multi)
# res = pivot_multi.copy()
# res.columns = res.columns.map(lambda x:'_'.join(x))
# res = res.reset_index()
# res = pd.wide_to_long(res, stubnames=['Grade', 'rank'],
#                            i = ['Class', 'Name'],
#                            j = 'Subject_Examination',
#                            sep = '_',
#                            suffix = '.+')
# print(res)
# res = res.reset_index()
# res[['Subject', 'Examination']] = res['Subject_Examination'].str.split('_', expand=True)
# res = res[['Class', 'Name', 'Examination', 'Subject', 'Grade', 'rank']].sort_values('Subject')
# res = res.reset_index(drop=False)
# print(res)
# res = res.reset_index(drop=True)
# print(res)