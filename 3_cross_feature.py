
import pandas as pd

# 加入交叉特征
TrainFeature_best_score=pd.read_csv('train_27-29.csv')
TestFeature_best_score=pd.read_csv('test.csv')

print('生成advertiserID_camgaignID')


TrainFeature_best_score['advertiserID_camgaignID']= TrainFeature_best_score['advertiserID'] * TrainFeature_best_score['camgaignID']
TestFeature_best_score['advertiserID_camgaignID'] = TestFeature_best_score['advertiserID'] * TestFeature_best_score['camgaignID']
print('生成advertiserID_camgaignID完成！！')

print('生成positionID_positionType')


TrainFeature_best_score['positionID_positionType'] = (TrainFeature_best_score['positionID']/1000) * TrainFeature_best_score['positionType']
TestFeature_best_score['positionID_positionType']  = (TestFeature_best_score['positionID']/1000) * TestFeature_best_score['positionType']

print('生成sitesetID_positionType')

TrainFeature_best_score['sitesetID_positionType']= TrainFeature_best_score['sitesetID'] * TrainFeature_best_score['positionType']
TestFeature_best_score['sitesetID_positionType']= TestFeature_best_score['sitesetID'] * TestFeature_best_score['positionType']


print('生成appCategory_pre')

TrainFeature_best_score['appCategory_pre']=TrainFeature_best_score['appCategory'].apply(lambda x:str(x)[0])
TestFeature_best_score['appCategory_pre']=TestFeature_best_score['appCategory'].apply(lambda x:str(x)[0])
print('生成appID_connectionType')

TrainFeature_best_score['appID_connectionType']=TrainFeature_best_score['appID']*10+TrainFeature_best_score['connectionType']
TestFeature_best_score['appID_connectionType']=TestFeature_best_score['appID']*10+TestFeature_best_score['connectionType']

print('生成userID_appID')

TrainFeature_best_score['userID_appID']=TrainFeature_best_score['appID']/10000+TrainFeature_best_score['userID']
TestFeature_best_score['userID_appID']=TestFeature_best_score['appID']/10000+TestFeature_best_score['userID']






TrainFeature_best_score.to_csv('train_27-29.csv',index=False)

TestFeature_best_score.to_csv('test.csv',index=False)



