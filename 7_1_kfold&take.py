# encoding: utf-8
'''
Created on 2017年6月19日

@author: c
'''
from sklearn.cross_validation import KFold
import sklearn
import numpy as np
import pandas as pd
import gc
#

# 生成转化率特征；训练集合n_folds

train=pd.read_csv('train_27-29.csv')
train['ins']=pd.Series(range(0,len(train)))
n_of_lines=len(train)
print (n_of_lines)
kf = KFold(n_of_lines, n_folds=5,shuffle=True,random_state=10000)

i=0
for train_index, test_index in kf:
    # print("TRAIN:", train_index, "TEST:", test_index)
    df=train.ix[test_index,:]
    df.to_csv('ttr'+str(i)+'.csv',index=False)
    i+=1
    del df
    gc.collect()
    print (i)


# a=[]
# content=[['positionID','connectionType'],['advertiserID','positionID'],['userID','sitesetID'],['appID','positionID'],
#          ['creativeID','positionID'],['creativeID','connectionType'],['userID','positionType']]
# for train_index, test_index in kf:
# #     print("TRAIN:", train_index, "TEST:", test_index)
#     a.append(train[test_index])
# del train
# gc.collect()
# 
# for pie in a:
#     dicts=process(pie,content)
#     
# 
# 
# print(np.concatenate((a[0],a[1])))