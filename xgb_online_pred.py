
import xgboost as xgb

import pandas as pd
# load or create your dataset
print('Load data...')
TrainFeature_best_score=pd.read_csv('train_27-29.csv')
TestFeature_best_score=pd.read_csv('test.csv')




sz = TrainFeature_best_score.shape
szpred=TestFeature_best_score.shape
print (sz)
print (szpred)



test_zuhe=list(range(2,szpred[1]))


best_score_zuhe = test_zuhe

print(best_score_zuhe)


train_X = TrainFeature_best_score.ix[:,best_score_zuhe]

train_Y = TrainFeature_best_score.ix[:,0]



print (train_X.shape)
print (train_Y.shape)



print('Start training...')

gbm = xgb.XGBClassifier(learning_rate=0.1,max_depth=8,n_estimators=250, silent=False,objective="binary:logistic")
# xgb_model=clf.fit(train_X, train_Y)

gbm.fit(train_X, train_Y)



pred_X = TestFeature_best_score.ix[:,best_score_zuhe]



print('Start predicting...')



pred_Y = gbm.predict_proba(pred_X)[:,1]




print(pred_Y)

# print('Calculate feature importances...')
# # feature importances
# print('Feature importances:', list(gbm.feature_importances_))

submssion = pd.read_csv('submission.csv')
submssion['prob']=pred_Y


submssion.to_csv('submission_xgb.csv',index=False)
print('预测完成')




