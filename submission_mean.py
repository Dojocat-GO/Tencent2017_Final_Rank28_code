import pandas as pd
import math
# 提升2个万分点

sub1=pd.read_csv('submission_xgb.csv')
sub2=pd.read_csv('submission_lgb.csv')
# 算术均值
sub1['prob2']=sub2['prob']
tmp=sub1.ix[:,1:]
print(tmp)
sub1['mean']=tmp.mean(axis=1)
print(sub1)

sub1=sub1.drop(['prob','prob2'],axis=1)
print(sub1)
sub1.columns=['instanceID','prob']
sub1.to_csv("submission_mean.csv",index=False)
