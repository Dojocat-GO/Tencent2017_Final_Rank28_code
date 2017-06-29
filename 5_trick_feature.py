import pandas as pd
import math

# 加入trick特征：3个千分点提升

TrainFeature_best_score=pd.read_csv('train_27-29.csv')
TestFeature_best_score=pd.read_csv('test.csv')



# 加入连续点击同一个creativeid特征，第一次点击，中间点击，最后一次点击和每次点击事件时间差



# 加入连续点击同一个creativeid特征，第一次点击，中间点击，最后一次点击标志
# 0：user只点击过一次creativeid  1：user有过多次点击行为，1代表第一次点击
# 2：user有过多次点击行为，2代表中间的点击过程  3：user有过多次点击行为，3代表最后一次点击
def interclick(clicktime1,clicktime2):
    second1=clicktime1%100
    clicktime1 = clicktime1 // 100
    min1=clicktime1%100
    hour1=math.floor((clicktime1%10000)/100)
    day1=math.floor(clicktime1/10000)

    second2 = clicktime2 % 100
    clicktime2 = clicktime2 // 100
    min2=clicktime2%100
    hour2=math.floor((clicktime2%10000)/100)
    day2=math.floor(clicktime2/10000)
    interclicktime_min=((day2*1440+hour2*60+min2)-(day1*1440+hour1*60+min1))
    interclicktime_second=((day2*1440+hour2*60+min2)*60+second2)-((day1*1440+hour1*60+min1)*60+second1)
    return interclicktime_min,interclicktime_second

train_tmp=TrainFeature_best_score.ix[:,['clickTime','creativeID','userID']]
test_tmp=TestFeature_best_score.ix[:,['clickTime','creativeID','userID']]


train_tmp=train_tmp.sort_values(by=['userID','creativeID','clickTime'])
test_tmp=test_tmp.sort_values(by=['userID','creativeID','clickTime'])
test_tmp['click_crea_lab']=0
train_tmp['click_crea_lab']=0




preix=-1
prerow={'clickTime': -1,
'creativeID ': -1,
'userID':  -1,
'click_crea_lab':  -1}

for ix, row in train_tmp.iterrows():
    # print(ix)
    # print(row)
    if(row['userID']==prerow['userID'] and row['creativeID']==prerow['creativeID']):
        row['click_crea_lab']=2
        if prerow['click_crea_lab'] != 2:
            prerow['click_crea_lab'] = 1
    elif prerow['click_crea_lab'] ==2:
        prerow['click_crea_lab'] = 3
        # print(prerow)
        # print(row)
    preix=ix
    prerow=row
print('train_tmp')
print(train_tmp)
train_tmp=train_tmp.sort_index()
print('train_tmp ater sort')
print(train_tmp)


TrainFeature_best_score['click_crea_lab']=train_tmp['click_crea_lab']




preix=-1
# prerow={'clickTime': -1,
# 'creativeID ': -1,
# 'userID':  -1,
# 'click_crea_lab':  -1}

for ix, row in test_tmp.iterrows():
    # print(ix)
    # print(row)
    if(row['userID']==prerow['userID'] and row['creativeID']==prerow['creativeID']):
        row['click_crea_lab']=2
        if prerow['click_crea_lab'] != 2:
            prerow['click_crea_lab'] = 1
    elif prerow['click_crea_lab'] ==2:
        prerow['click_crea_lab'] = 3
        # print(prerow)
        # print(row)
    preix=ix
    prerow=row
print('test_tmp')
print(test_tmp)
test_tmp=test_tmp.sort_index()
print('test_tmp ater sort')
print(test_tmp)


TestFeature_best_score['click_crea_lab']=test_tmp['click_crea_lab']






# 加入user连续点击同一个creativeid特征时间差




train_tmp=TrainFeature_best_score.ix[:,['clickTime','creativeID','userID']]
test_tmp=TestFeature_best_score.ix[:,['clickTime','creativeID','userID']]


train_tmp=train_tmp.sort_values(by=['userID','creativeID','clickTime'])
test_tmp=test_tmp.sort_values(by=['userID','creativeID','clickTime'])
test_tmp['us_creaid_interclickTime_min']=-1
train_tmp['us_creaid_interclickTime_min']=-1

test_tmp['us_creaid_interclickTime_second']=-1
train_tmp['us_creaid_interclickTime_second']=-1

preix=-1
prerow={'clickTime': -1,
        'creativeID ': -1,
        'userID':  -1,
        'us_creaid_interclickTime_min':-1,
        'us_creaid_interclickTime_second':-1}

for ix, row in train_tmp.iterrows():
    # print(ix)
    # print(row)
    if(row['userID']==prerow['userID'] and row['creativeID']==prerow['creativeID']):
        row['us_creaid_interclickTime_min'],row['us_creaid_interclickTime_second']=interclick(int(prerow['clickTime']),int(row['clickTime']))
    preix=ix
    prerow=row
print('train_tmp')
print(train_tmp)
train_tmp=train_tmp.sort_index()
print('train_tmp ater sort')
print(train_tmp)


TrainFeature_best_score['us_creaid_interclickTime_min']=train_tmp['us_creaid_interclickTime_min']
TrainFeature_best_score['us_creaid_interclickTime_second']=train_tmp['us_creaid_interclickTime_second']




preix=-1


for ix, row in test_tmp.iterrows():
    # print(ix)
    # print(row)
    if(row['userID']==prerow['userID'] and row['creativeID']==prerow['creativeID']):
        row['us_creaid_interclickTime_min'],row['us_creaid_interclickTime_second']=interclick(int(prerow['clickTime']),int(row['clickTime']))
    preix=ix
    prerow=row
print('test_tmp')
print(test_tmp)
test_tmp=test_tmp.sort_index()
print('test_tmp ater sort')
print(test_tmp)


TestFeature_best_score['us_creaid_interclickTime_min']=test_tmp['us_creaid_interclickTime_min']
TestFeature_best_score['us_creaid_interclickTime_second']=test_tmp['us_creaid_interclickTime_second']








#click_appID_lab
# 加入连续点击同一个appID特征，第一次点击，中间点击，最后一次点击标志
# 0：user只点击过一次appID  1：user有过多次点击行为，1代表第一次点击
# 2：user有过多次点击行为，2代表中间的点击过程  3：user有过多次点击行为，3代表最后一次点击

print('加入连续点击同一个appID特征，第一次点击，中间点击，最后一次点击')

train_tmp=TrainFeature_best_score.ix[:,['clickTime','appID','userID']]
test_tmp=TestFeature_best_score.ix[:,['clickTime','appID','userID']]


train_tmp=train_tmp.sort_values(by=['userID','appID','clickTime'])
test_tmp=test_tmp.sort_values(by=['userID','appID','clickTime'])
test_tmp['click_appID_lab']=0
train_tmp['click_appID_lab']=0


preix=-1
prerow={'clickTime': -1,
'appID ': -1,
'userID':  -1,
'click_appID_lab':  -1}

for ix, row in train_tmp.iterrows():
    # print(ix)
    # print(row)
    if(row['userID']==prerow['userID'] and row['appID']==prerow['appID']):
        row['click_appID_lab']=2
        if prerow['click_appID_lab'] != 2:
            prerow['click_appID_lab'] = 1
    elif prerow['click_appID_lab'] ==2:
        prerow['click_appID_lab'] = 3
        # print(prerow)
        # print(row)
    preix=ix
    prerow=row
print('train_tmp')
print(train_tmp)
train_tmp=train_tmp.sort_index()
print('train_tmp ater sort')
print(train_tmp)


TrainFeature_best_score['click_appID_lab']=train_tmp['click_appID_lab']



preix=-1

for ix, row in test_tmp.iterrows():
    # print(ix)
    # print(row)
    if(row['userID']==prerow['userID'] and row['appID']==prerow['appID']):
        row['click_appID_lab']=2
        if prerow['click_appID_lab'] != 2:
            prerow['click_appID_lab'] = 1
            print(row)
    elif prerow['click_appID_lab'] ==2:
        prerow['click_appID_lab'] = 3
        # print(prerow)
        # print(row)
    preix=ix
    prerow=row
print('test_tmp')
print(test_tmp)
test_tmp=test_tmp.sort_index()
print('test_tmp ater sort')
print(test_tmp)


TestFeature_best_score['click_appID_lab']=test_tmp['click_appID_lab']









# us_appID_interclickTime_min   us_appID_interclickTime_second
# 加入user连续点击同一个appID特征时间差

def interclick(clicktime1,clicktime2):
    second1=clicktime1%100
    clicktime1 = clicktime1 // 100
    min1=clicktime1%100
    hour1=math.floor((clicktime1%10000)/100)
    day1=math.floor(clicktime1/10000)

    second2 = clicktime2 % 100
    clicktime2 = clicktime2 // 100
    min2=clicktime2%100
    hour2=math.floor((clicktime2%10000)/100)
    day2=math.floor(clicktime2/10000)
    interclicktime_min=((day2*1440+hour2*60+min2)-(day1*1440+hour1*60+min1))
    interclicktime_second=((day2*1440+hour2*60+min2)*60+second2)-((day1*1440+hour1*60+min1)*60+second1)
    return interclicktime_min,interclicktime_second

print('加入user连续点击同一个appID特征时间差')



train_tmp=TrainFeature_best_score.ix[:,['clickTime','appID','userID']]
test_tmp=TestFeature_best_score.ix[:,['clickTime','appID','userID']]


train_tmp=train_tmp.sort_values(by=['userID','appID','clickTime'])
test_tmp=test_tmp.sort_values(by=['userID','appID','clickTime'])
test_tmp['us_appID_interclickTime_min']=-1
train_tmp['us_appID_interclickTime_min']=-1

test_tmp['us_appID_interclickTime_second']=-1
train_tmp['us_appID_interclickTime_second']=-1


preix=-1
prerow={'clickTime': -1,
        'appID ': -1,
        'userID':  -1,
        'us_appID_interclickTime_min':-1,
        'us_appID_interclickTime_second':-1}

for ix, row in train_tmp.iterrows():
    # print(ix)
    # print(row)
    if(row['userID']==prerow['userID'] and row['appID']==prerow['appID']):
        row['us_appID_interclickTime_min'],row['us_appID_interclickTime_second']=interclick(int(prerow['clickTime']),int(row['clickTime']))
    preix=ix
    prerow=row
print('train_tmp')
print(train_tmp)
train_tmp=train_tmp.sort_index()
print('train_tmp ater sort')
print(train_tmp)


TrainFeature_best_score['us_appID_interclickTime_min']=train_tmp['us_appID_interclickTime_min']
TrainFeature_best_score['us_appID_interclickTime_second']=train_tmp['us_appID_interclickTime_second']




preix=-1


for ix, row in test_tmp.iterrows():
    # print(ix)
    # print(row)
    if(row['userID']==prerow['userID'] and row['appID']==prerow['appID']):
        row['us_appID_interclickTime_min'],row['us_appID_interclickTime_second']=interclick(int(prerow['clickTime']),int(row['clickTime']))
    preix=ix
    prerow=row
print('test_tmp')
print(test_tmp)
test_tmp=test_tmp.sort_index()
print('test_tmp ater sort')
print(test_tmp)


TestFeature_best_score['us_appID_interclickTime_min']=test_tmp['us_appID_interclickTime_min']
TestFeature_best_score['us_appID_interclickTime_second']=test_tmp['us_appID_interclickTime_second']






# 加入user点击同一个appID距离第一次点击和最后一次点击时间差
print('加入user点击同一个appID距离第一次点击和最后一次点击时间差')


def interclick(clicktime1, clicktime2):
    second1 = clicktime1 % 100
    clicktime1 = clicktime1 // 100
    min1 = clicktime1 % 100
    hour1 = math.floor((clicktime1 % 10000) / 100)
    day1 = math.floor(clicktime1 / 10000)

    second2 = clicktime2 % 100
    clicktime2 = clicktime2 // 100
    min2 = clicktime2 % 100
    hour2 = math.floor((clicktime2 % 10000) / 100)
    day2 = math.floor(clicktime2 / 10000)
    interclicktime_min = ((day2 * 1440 + hour2 * 60 + min2) - (day1 * 1440 + hour1 * 60 + min1))
    interclicktime_second = ((day2 * 1440 + hour2 * 60 + min2) * 60 + second2) - (
    (day1 * 1440 + hour1 * 60 + min1) * 60 + second1)
    return interclicktime_min, interclicktime_second



first_dict = {}
last_dict = {}

for ix, row in TrainFeature_best_score.iterrows():
    # print(ix)
    # print(row)
    tmp = row['click_appID_lab']
    tmp_click_appID = row['userID_appID']
    if tmp == 1:
        first_dict[tmp_click_appID] = row['clickTime']
    elif tmp == 3:
        last_dict[tmp_click_appID] = row['clickTime']

TrainFeature_best_score['click_appID_min_first'] = 0
TrainFeature_best_score['click_appID_min_last'] = 0
TrainFeature_best_score['click_appID_second_first'] = 0
TrainFeature_best_score['click_appID_second_last'] = 0
print(TrainFeature_best_score)
for ix, row in TrainFeature_best_score.iterrows():
    # print(ix)
    # print(row)
    tmp = row['click_appID_lab']
    tmp_click_appID = row['userID_appID']

    if tmp == 2:
        row['click_appID_min_first'], row['click_appID_second_first'] = interclick(first_dict[tmp_click_appID],
                                                                                   row['clickTime'])
        row['click_appID_min_last'], row['click_appID_second_last'] = interclick(row['clickTime'],
                                                                                 last_dict[tmp_click_appID])
    elif tmp == 1:
        row['click_appID_min_first'] = 0
        row['click_appID_second_first'] = 0
        row['click_appID_min_last'], row['click_appID_second_last'] = interclick(row['clickTime'],
                                                                                 last_dict[tmp_click_appID])
    elif tmp == 3:
        row['click_appID_min_first'], row['click_appID_second_first'] = interclick(first_dict[tmp_click_appID],
                                                                                   row['clickTime'])
        row['click_appID_min_last'] = 0
        row['click_appID_second_last'] = 0
    TrainFeature_best_score.ix[ix, :] = row
print('处理完Train')
print(TrainFeature_best_score)



first_dict = last_dict
last_dict = {}

for ix, row in TestFeature_best_score.iterrows():
    # print(ix)
    # print(row)
    tmp = row['click_appID_lab']
    tmp_click_appID = row['userID_appID']
    if tmp == 1:
        first_dict[tmp_click_appID] = row['clickTime']
    elif tmp == 3:
        last_dict[tmp_click_appID] = row['clickTime']

TestFeature_best_score['click_appID_min_first'] = 0
TestFeature_best_score['click_appID_min_last'] = 0
TestFeature_best_score['click_appID_second_first'] = 0
TestFeature_best_score['click_appID_second_last'] = 0
print(TestFeature_best_score)
for ix, row in TestFeature_best_score.iterrows():
    # print(ix)
    # print(row)
    tmp = row['click_appID_lab']
    tmp_click_appID = row['userID_appID']

    if tmp == 2:
        row['click_appID_min_first'], row['click_appID_second_first'] = interclick(first_dict[tmp_click_appID],
                                                                                   row['clickTime'])
        row['click_appID_min_last'], row['click_appID_second_last'] = interclick(row['clickTime'],
                                                                                 last_dict[tmp_click_appID])
    elif tmp == 1:
        row['click_appID_min_first'] = 0
        row['click_appID_second_first'] = 0
        row['click_appID_min_last'], row['click_appID_second_last'] = interclick(row['clickTime'],
                                                                                 last_dict[tmp_click_appID])
    elif tmp == 3:
        row['click_appID_min_first'], row['click_appID_second_first'] = interclick(first_dict[tmp_click_appID],
                                                                                   row['clickTime'])
        row['click_appID_min_last'] = 0
        row['click_appID_second_last'] = 0
    TestFeature_best_score.ix[ix, :] = row
print('处理完Test')
print(TestFeature_best_score)






print('生成day_click_lab')

# 加入一天内连续点击同一个appID特征，第一次点击，中间点击，最后一次点击
# 0：user只点击过一次appID  1：user有过多次点击行为，1代表第一次点击
# 2：user有过多次点击行为，2代表中间的点击过程  3：user有过多次点击行为，3代表最后一次点击

print('加入一天内连续点击同一个appID特征，第一次点击，中间点击，最后一次点击')
for i in range(27, 30):
    TrainFeature_best_score_day = TrainFeature_best_score[(TrainFeature_best_score.clickTime // 1000000) == i]

    train_tmp = TrainFeature_best_score_day.ix[:, ['clickTime', 'appID', 'userID']]
    train_tmp = train_tmp.sort_values(by=['userID', 'appID', 'clickTime'])
    train_tmp['click_appID_day_lab'] = 0

    preix = -1
    prerow = {'clickTime': -1,
              'appID ': -1,
              'userID': -1,
              'click_appID_day_lab': -1}

    for ix, row in train_tmp.iterrows():
        # print(ix)
        # print(row)
        if (row['userID'] == prerow['userID'] and row['appID'] == prerow['appID']):
            row['click_appID_day_lab'] = 2
            train_tmp.ix[ix,:]=row
            if prerow['click_appID_day_lab'] != 2:
                prerow['click_appID_day_lab'] = 1
                train_tmp.ix[preix, :] = prerow
        elif prerow['click_appID_day_lab'] == 2:
            prerow['click_appID_day_lab'] = 3
            train_tmp.ix[preix, :] = prerow
            # print(prerow)
            # print(row)
        preix = ix
        prerow = row

    train_tmp = train_tmp.sort_index()

    if i == 16:
        TrainFeature_best_score_day_add = train_tmp['click_appID_day_lab']

    else:
        TrainFeature_best_score_day_tmp = train_tmp['click_appID_day_lab']

        TrainFeature_best_score_day_add = TrainFeature_best_score_day_add.append(TrainFeature_best_score_day_tmp)

TrainFeature_best_score_day_add = TrainFeature_best_score_day_add.reset_index(drop=True)
TrainFeature_best_score['click_appID_day_lab'] = TrainFeature_best_score_day_add




test_tmp = TestFeature_best_score.ix[:, ['clickTime', 'appID', 'userID']]

test_tmp = test_tmp.sort_values(by=['userID', 'appID', 'clickTime'])
test_tmp['click_appID_day_lab'] = 0

preix = -1
prerow = {'clickTime': -1,
          'appID ': -1,
          'userID': -1,
          'click_appID_day_lab': -1}

preix = -1

for ix, row in test_tmp.iterrows():
    # print(ix)
    # print(row)
    if (row['userID'] == prerow['userID'] and row['appID'] == prerow['appID']):
        row['click_appID_day_lab'] = 2
        train_tmp.ix[ix, :] = row
        if prerow['click_appID_day_lab'] != 2:
            prerow['click_appID_day_lab'] = 1
            train_tmp.ix[preix, :] = prerow
            print(row)
    elif prerow['click_appID_day_lab'] == 2:
        prerow['click_appID_day_lab'] = 3
        train_tmp.ix[preix, :] = prerow
        # print(prerow)
        # print(row)
    preix = ix
    prerow = row

test_tmp = test_tmp.sort_index()

TestFeature_best_score['click_appID_day_lab'] = test_tmp['click_appID_day_lab']





# 加入一天内user点击同一个appID距离该天第一次点击和最后一次点击时间差

print('加入一天内user点击同一个appID距离该天第一次点击和最后一次点击时间差')

for i in range(27, 30):
    TrainFeature_best_score_day = TrainFeature_best_score[(TrainFeature_best_score.clickTime // 1000000) == i]

    first_dict = {}
    last_dict = {}

    for ix, row in TrainFeature_best_score_day.iterrows():
        # print(ix)
        # print(row)
        tmp = row['click_appID_day_lab']
        tmp_click_appID = row['userID_appID']
        if tmp == 1:
            first_dict[tmp_click_appID] = row['clickTime']
        elif tmp == 3:
            last_dict[tmp_click_appID] = row['clickTime']

    TrainFeature_best_score_day['click_appID_day_min_first'] = 0
    TrainFeature_best_score_day['click_appID_day_min_last'] = 0
    TrainFeature_best_score_day['click_appID_day_second_first'] = 0
    TrainFeature_best_score_day['click_appID_day_second_last'] = 0
    for ix, row in TrainFeature_best_score_day.iterrows():
        # print(ix)
        # print(row)
        tmp = row['click_appID_day_lab']
        tmp_click_appID = row['userID_appID']

        if tmp == 2:
            row['click_appID_day_min_first'], row['click_appID_day_second_first'] = interclick(
                first_dict[tmp_click_appID], row['clickTime'])
            row['click_appID_day_min_last'], row['click_appID_day_second_last'] = interclick(row['clickTime'],
                                                                                             last_dict[tmp_click_appID])
        elif tmp == 1:
            row['click_appID_day_min_first'] = 0
            row['click_appID_day_second_first'] = 0
            row['click_appID_day_min_last'], row['click_appID_day_second_last'] = interclick(row['clickTime'],
                                                                                             last_dict[tmp_click_appID])
        elif tmp == 3:
            row['click_appID_day_min_first'], row['click_appID_day_second_first'] = interclick(
                first_dict[tmp_click_appID], row['clickTime'])
            row['click_appID_day_min_last'] = 0
            row['click_appID_day_second_last'] = 0
        TrainFeature_best_score_day.ix[ix, :] = row

    print(TrainFeature_best_score_day)
    if i == 16:
        TrainFeature_best_score_day_add = TrainFeature_best_score_day.ix[:,
                                          ['click_appID_day_min_first', 'click_appID_day_second_first',
                                           'click_appID_day_min_last', 'click_appID_day_second_last']]

    else:
        TrainFeature_best_score_day_tmp = TrainFeature_best_score_day.ix[:,
                                          ['click_appID_day_min_first', 'click_appID_day_second_first',
                                           'click_appID_day_min_last', 'click_appID_day_second_last']]

        TrainFeature_best_score_day_add = TrainFeature_best_score_day_add.append(TrainFeature_best_score_day_tmp)

TrainFeature_best_score_day_add = TrainFeature_best_score_day_add.reset_index(drop=True)

TrainFeature_best_score = TrainFeature_best_score.join(TrainFeature_best_score_day_add)




first_dict = {}
last_dict = {}

for ix, row in TestFeature_best_score.iterrows():
    # print(ix)
    # print(row)
    tmp = row['click_appID_day_lab']
    tmp_click_appID = row['userID_appID']
    if tmp == 1:
        first_dict[tmp_click_appID] = row['clickTime']
    elif tmp == 3:
        last_dict[tmp_click_appID] = row['clickTime']

TestFeature_best_score['click_appID_day_min_first'] = 0
TestFeature_best_score['click_appID_day_min_last'] = 0
TestFeature_best_score['click_appID_day_second_first'] = 0
TestFeature_best_score['click_appID_day_second_last'] = 0

for ix, row in TestFeature_best_score.iterrows():
    # print(ix)
    # print(row)
    tmp = row['click_appID_day_lab']
    tmp_click_appID = row['userID_appID']

    if tmp == 2:
        row['click_appID_day_min_first'], row['click_appID_day_second_first'] = interclick(first_dict[tmp_click_appID],
                                                                                           row['clickTime'])
        row['click_appID_day_min_last'], row['click_appID_day_second_last'] = interclick(row['clickTime'],
                                                                                         last_dict[tmp_click_appID])
    elif tmp == 1:
        row['click_appID_day_min_first'] = 0
        row['click_appID_day_second_first'] = 0
        row['click_appID_day_min_last'], row['click_appID_day_second_last'] = interclick(row['clickTime'],
                                                                                         last_dict[tmp_click_appID])
    elif tmp == 3:
        row['click_appID_day_min_first'], row['click_appID_day_second_first'] = interclick(first_dict[tmp_click_appID],
                                                                                           row['clickTime'])
        row['click_appID_day_min_last'] = 0
        row['click_appID_day_second_last'] = 0
    TestFeature_best_score.ix[ix, :] = row

# 加入appID和click_crea_lab交叉特征
print('生成clickcrealab_appID_con')

TrainFeature_best_score['clickcrealab_appID_con']=TrainFeature_best_score['appID']/10000+TrainFeature_best_score['click_crea_lab']
TestFeature_best_score['clickcrealab_appID_con']=TestFeature_best_score['appID']/10000+TestFeature_best_score['click_crea_lab']


TrainFeature_best_score.to_csv('train_27-29.csv', index=False)

TestFeature_best_score.to_csv('test.csv', index=False)

print('over')















