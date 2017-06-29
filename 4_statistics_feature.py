
import pandas as pd
# 加入统计特征

TrainFeature_best_score=pd.read_csv('train_27-29.csv')
TestFeature_best_score=pd.read_csv('test.csv')


print('生成userID_sum')

df=TrainFeature_best_score[['userID']].append(TestFeature_best_score[['userID']])
groupby_userID=df.groupby('userID').size()
print('groupby_userID:')
print(groupby_userID)

TrainFeature_best_score['userID_sum']=TrainFeature_best_score['userID'].apply(lambda x:groupby_userID[x])
TestFeature_best_score['userID_sum']=TestFeature_best_score['userID'].apply(lambda x:groupby_userID[x])

print('生成appID_sum')

df=TrainFeature_best_score[['appID']].append(TestFeature_best_score[['appID']])
groupby_userID=df.groupby('appID').size()

TrainFeature_best_score['appID_sum']=TrainFeature_best_score['appID'].apply(lambda x:groupby_userID[x])
TestFeature_best_score['appID_sum']=TestFeature_best_score['appID'].apply(lambda x:groupby_userID[x])



print('生成userID_appID_sum')

df=TrainFeature_best_score[['userID','appID']].append(TestFeature_best_score[['userID','appID']])
df['userID_appID']=df['userID']+df['appID']/10000
groupby_userID=df.groupby('userID_appID').size()
print('groupby_userID:')
print(groupby_userID)

TrainFeature_best_score['userID_appID']=TrainFeature_best_score['userID']+TrainFeature_best_score['appID']/10000
TestFeature_best_score['userID_appID']=TestFeature_best_score['userID']+TestFeature_best_score['appID']/10000


TrainFeature_best_score['userID_appID_sum']=TrainFeature_best_score['userID_appID'].apply(lambda x:groupby_userID[x])

TestFeature_best_score['userID_appID_sum']=TestFeature_best_score['userID_appID'].apply(lambda x:groupby_userID[x])





# 加入userID_appID_day_sum     userID_day_sum

for i in range(27,30):
    TrainFeature_best_score_day=TrainFeature_best_score[(TrainFeature_best_score.clickTime//1000000)==i]
    TrainFeature_best_score_day = TrainFeature_best_score_day.ix[:, ['userID', 'userID_appID']]
    groupby_userID_day = TrainFeature_best_score_day.groupby('userID').size()
    groupby_userID_appID_day = TrainFeature_best_score_day.groupby('userID_appID').size()

    if i==16:
        TrainFeature_best_score_day_add = TrainFeature_best_score_day['userID'].apply(lambda x: groupby_userID_day[x])
        TrainFeature_best_score_day_appID_add = TrainFeature_best_score_day['userID_appID'].apply(lambda x: groupby_userID_appID_day[x])
    else:
        TrainFeature_best_score_day_tmp = TrainFeature_best_score_day['userID'].apply(lambda x: groupby_userID_day[x])
        TrainFeature_best_score_day_appID_tmp = TrainFeature_best_score_day['userID_appID'].apply(lambda x: groupby_userID_appID_day[x])

        TrainFeature_best_score_day_add = TrainFeature_best_score_day_add.append(TrainFeature_best_score_day_tmp)
        TrainFeature_best_score_day_appID_add = TrainFeature_best_score_day_appID_add.append(TrainFeature_best_score_day_appID_tmp)




print('拼接完成')


TrainFeature_best_score_day_add=TrainFeature_best_score_day_add.reset_index(drop=True)
TrainFeature_best_score_day_appID_add=TrainFeature_best_score_day_appID_add.reset_index(drop=True)


TrainFeature_best_score['userID_day_sum']=TrainFeature_best_score_day_add
TrainFeature_best_score['userID_appID_day_sum']=TrainFeature_best_score_day_appID_add


TrainFeature_best_score.to_csv('train_27-29.csv',index=False)




TestFeature_best_score_day=TestFeature_best_score[['userID','userID_appID']]

groupby_userID_day=TestFeature_best_score_day.groupby('userID').size()
groupby_userID_appID_day=TestFeature_best_score_day.groupby('userID_appID').size()

TestFeature_best_score['userID_day_sum']=TestFeature_best_score_day['userID'].apply(lambda x:groupby_userID_day[x])
TestFeature_best_score['userID_appID_day_sum']=TestFeature_best_score_day['userID_appID'].apply(lambda x:groupby_userID_appID_day[x])
print('写入CSV')



TestFeature_best_score.to_csv('test.csv',index=False)









