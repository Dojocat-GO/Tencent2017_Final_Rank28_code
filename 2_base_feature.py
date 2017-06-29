
import pandas as pd



TrainFeature_best_score=pd.read_csv('train_27-29.csv')
TestFeature_best_score=pd.read_csv('test.csv')




print('加入4个时间特征')
TrainFeature_best_score['clickTime_day']=TrainFeature_best_score['clickTime'].apply(lambda x:str(x)[0]+str(x)[1])
TestFeature_best_score['clickTime_day']=TestFeature_best_score['clickTime'].apply(lambda x:str(x)[0]+str(x)[1])

TrainFeature_best_score['clickTime_hour']=TrainFeature_best_score['clickTime'].apply(lambda x:str(x)[2]+str(x)[3])
TestFeature_best_score['clickTime_hour']=TestFeature_best_score['clickTime'].apply(lambda x:str(x)[2]+str(x)[3])

TrainFeature_best_score['clickTime_min']=TrainFeature_best_score['clickTime'].apply(lambda x:str(x)[4]+str(x)[5])
TestFeature_best_score['clickTime_min']=TestFeature_best_score['clickTime'].apply(lambda x:str(x)[4]+str(x)[5])

TrainFeature_best_score['clickTime_second']=TrainFeature_best_score['clickTime'].apply(lambda x:str(x)[6]+str(x)[7])
TestFeature_best_score['clickTime_second']=TestFeature_best_score['clickTime'].apply(lambda x:str(x)[6]+str(x)[7])




print('生成appCategory_pre')

TrainFeature_best_score['appCategory_pre']=TrainFeature_best_score['appCategory'].apply(lambda x:str(x)[0])
TestFeature_best_score['appCategory_pre']=TestFeature_best_score['appCategory'].apply(lambda x:str(x)[0])



TrainFeature_best_score.to_csv('train_27-29.csv',index=False)

TestFeature_best_score.to_csv('test.csv',index=False)


