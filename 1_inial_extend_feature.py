# encoding: utf-8

import csv
import numpy as np

# 生成初始拼接特征test.csv

def getprov(code):
    #if len(code)==4:
        #return code[0:2]
    #if len(code)==3:
        #return code[0]
    return  code

train=open('Tencent/test.csv')
trainreader=csv.DictReader(train)
ad=open('Tencent/ad.csv')
adreader=csv.DictReader(ad)
user=open('Tencent/user.csv')
userreader=csv.DictReader(user)
postion=open('Tencent/position.csv')
postionreader=csv.DictReader(postion)
cate=open('Tencent/app_categories.csv')
appreader=csv.DictReader(cate)
AdDict=dict()
UserDict=dict()
PosDict=dict()
AppDict=dict()
for appa in appreader:
    AppDict[appa["appID"]]=appa['appCategory']
print ('AppComplete')
for item in adreader:
    AdDict[item['creativeID']]=[item['adID'],item['camgaignID'],item['advertiserID'],item['appID'],item['appPlatform']]
print ('AdComplete')
for item in userreader:
    UserDict[item['userID']]=[item['age'],item['gender' ],item['education' ],item['marriageStatus'],item['haveBaby'],getprov(item['hometown']),getprov(item['residence'])]
print ('UserComplete')
for item in postionreader:
    PosDict[item['positionID']]=[item['sitesetID'],item['positionType']]
print ('PosComplete')
trainfeature=open('test.csv','w',newline='')
fieldnames=['label','clickTime','connectionType','telecomsOperator','creativeID','adID','camgaignID','advertiserID','appID','appPlatform','userID','age', 'gender' ,'education' ,'marriageStatus', 'haveBaby' ,'hometown' ,'residence','positionID','sitesetID','positionType','appCategory']
TFwriter=csv.DictWriter(trainfeature,fieldnames=fieldnames)
TFwriter.writeheader()
for rec in trainreader:
    #if int(rec['clickTime'])>=300000:
     #   break
    print (rec['clickTime'])
    clickTime=rec['clickTime']
    label=rec['label']
    creativeID=rec['creativeID']
    userID=rec['userID']
    positionID=rec['positionID']
    connectionType=rec['connectionType']
    telecomsOperator=rec['telecomsOperator']
    adreader=csv.DictReader(open('Tencent/ad.csv'))
    tup=AdDict[creativeID]
    adID=tup[0]
    camgaignID=tup[1]
    advertiserID=tup[2]
    appID=tup[3]
    appPlatform=tup[4]
    tup=UserDict[userID]
    age=tup[0]
    gender=tup[1]
    education=tup[2]
    marriageStatus=tup[3]
    haveBaby= tup[4]
    hometown=tup[5]
    residence=tup[6]
    tup=PosDict[positionID]
    sitesetID=tup[0]
    postionType=tup[1]
    tup=AppDict[appID]
    appCategory=tup
    TFwriter.writerow({'label':label,'clickTime':clickTime,'connectionType':connectionType,'telecomsOperator':telecomsOperator,'creativeID':creativeID,'adID':adID,'camgaignID':camgaignID,'advertiserID':advertiserID,'appID':appID,'appPlatform':appPlatform,'userID':userID,'age':age, 'gender':gender,'education':education,'marriageStatus':marriageStatus, 'haveBaby':haveBaby ,'hometown':hometown,'residence':residence,'positionID':positionID,'sitesetID':sitesetID,'positionType':postionType,'appCategory':appCategory})


# 生成初始拼接特征train_27-29.csv

def getprov(code):
    # if len(code)==4:
    # return code[0:2]
    # if len(code)==3:
    # return code[0]
    return code


train = open('Tencent/train.csv')
trainreader = csv.DictReader(train)
ad = open('Tencent/ad.csv')
adreader = csv.DictReader(ad)
user = open('Tencent/user.csv')
userreader = csv.DictReader(user)
postion = open('Tencent/position.csv')
postionreader = csv.DictReader(postion)
cate = open('Tencent/app_categories.csv')
appreader = csv.DictReader(cate)
AdDict = dict()
UserDict = dict()
PosDict = dict()
AppDict = dict()
for appa in appreader:
    AppDict[appa["appID"]] = appa['appCategory']
print('AppComplete')
for item in adreader:
    AdDict[item['creativeID']] = [item['adID'], item['camgaignID'], item['advertiserID'], item['appID'],
                                  item['appPlatform']]
print('AdComplete')
for item in userreader:
    UserDict[item['userID']] = [item['age'], item['gender'], item['education'], item['marriageStatus'],
                                item['haveBaby'], getprov(item['hometown']), getprov(item['residence'])]
print('UserComplete')
for item in postionreader:
    PosDict[item['positionID']] = [item['sitesetID'], item['positionType']]
print('PosComplete')
trainfeature = open('train_27-29.csv', 'w', newline='')
fieldnames = ['label', 'clickTime', 'connectionType', 'telecomsOperator', 'creativeID', 'adID', 'camgaignID',
              'advertiserID', 'appID', 'appPlatform', 'userID', 'age', 'gender', 'education', 'marriageStatus',
              'haveBaby', 'hometown', 'residence', 'positionID', 'sitesetID', 'positionType', 'appCategory']
TFwriter = csv.DictWriter(trainfeature, fieldnames=fieldnames)
TFwriter.writeheader()
for rec in trainreader:
    if int(rec['clickTime'])>=30000000 or int(rec['clickTime'])<28000000:
      continue
    print(rec['clickTime'])
    clickTime = rec['clickTime']
    label = rec['label']
    creativeID = rec['creativeID']
    userID = rec['userID']
    positionID = rec['positionID']
    connectionType = rec['connectionType']
    telecomsOperator = rec['telecomsOperator']
    adreader = csv.DictReader(open('Tencent/ad.csv'))
    tup = AdDict[creativeID]
    adID = tup[0]
    camgaignID = tup[1]
    advertiserID = tup[2]
    appID = tup[3]
    appPlatform = tup[4]
    tup = UserDict[userID]
    age = tup[0]
    gender = tup[1]
    education = tup[2]
    marriageStatus = tup[3]
    haveBaby = tup[4]
    hometown = tup[5]
    residence = tup[6]
    tup = PosDict[positionID]
    sitesetID = tup[0]
    postionType = tup[1]
    tup = AppDict[appID]
    appCategory = tup
    TFwriter.writerow({'label': label, 'clickTime': clickTime, 'connectionType': connectionType,
                       'telecomsOperator': telecomsOperator, 'creativeID': creativeID, 'adID': adID,
                       'camgaignID': camgaignID, 'advertiserID': advertiserID, 'appID': appID,
                       'appPlatform': appPlatform, 'userID': userID, 'age': age, 'gender': gender,
                       'education': education, 'marriageStatus': marriageStatus, 'haveBaby': haveBaby,
                       'hometown': hometown, 'residence': residence, 'positionID': positionID,
                       'sitesetID': sitesetID, 'positionType': postionType, 'appCategory': appCategory})