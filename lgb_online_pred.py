
import lightgbm as lgb

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

best_score_zuhe=test_zuhe
print(best_score_zuhe)




#train_X = TrainFeature_best_score.ix[:,best_score_zuhe]
train_X = TrainFeature_best_score.ix[:,best_score_zuhe]

train_Y = TrainFeature_best_score.ix[:,0]



#pred_X = TestFeature_best_score.ix[:,best_score_zuhe]
# pred_Y = TestFeature_best_score[:,0]

print (train_X.shape)
print (train_Y.shape)

#print (pred_X.shape)

# print (pred_Y.shape)


print('Start training...')

gbm = lgb.LGBMClassifier(
    objective='binary',
    max_depth=6,
    num_leaves=128,
    silent=False,
    learning_rate=0.1,
    n_estimators=700

)
# del TrainFeature_best_score
# del TestFeature_best_score
#
# gc.collect()





gbm.fit(train_X, train_Y,
        # eval_set=[(X_test, y_test)],
        # eval_metric='l1',
        # early_stopping_rounds=5
        )









pred_X = TestFeature_best_score.ix[:,best_score_zuhe]



print('Start predicting...')
# predict

# print(res_dict)
#
# pred_Y = gbm.predict(pred_X)


pred_Y = gbm.predict_proba(pred_X, num_iteration=gbm.best_iteration)[:,1]




# eval
# print('The rmse of prediction is:', mean_squared_error(y_test, y_pred) ** 0.5)





print(pred_Y)

# print('Calculate feature importances...')
# # feature importances
# print('Feature importances:', list(gbm.feature_importances_))

submssion = pd.read_csv('submission.csv')
submssion['prob']=pred_Y


submssion.to_csv('submission_lgb.csv',index=False)
print('预测完成')




