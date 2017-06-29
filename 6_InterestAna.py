# encoding: utf-8
'''
Created on 2017年5月9日

@author: c
'''
import csv
import numpy as np
from NAMEDICT import NameDict

# 统计installedapps表，action表统计特征
# 62 : user_actioned_sum 63 : user_actioned_thiscate_sum
# 64 : user_actioned_thisbigcate_sum 65 : user_installed_sum 66 : user_installed_thiscate_sum 67 : user_installed_thisbigcate_sum
install=open('Tencent/user_installedapps.csv')
installreader=csv.DictReader(install)
app=open('Tencent/app_categories.csv')
appreader=csv.DictReader(app)

interest=open('user_installed_NEW.csv','w',newline='')
fieldnames = ["userID",'0', '1','2', '101', '103', '104', '105', '106', '108', '109', '110',  '201', '203', '204', '209', '210', '211', '301', '303', '401', '402', '403', '405', '406', '407', '408', '409', '503','SUM']
interestwriter=csv.DictWriter(interest,fieldnames =fieldnames )
interestwriter.writeheader()
InDict=dict()
AppDict=dict()
for appa in appreader:
    AppDict[appa["appID"]]=appa['appCategory']
print ('appComplete')
for rec in installreader:
#     if int(rec['installTime'])>=24000000:
#         continue
    apID = rec["appID"]
    cate=AppDict[apID]
    if InDict.__contains__(rec['userID']):
        temp=InDict[rec['userID']] 
        temp[NameDict[cate]]+=1
        InDict[rec['userID']] =temp
    else:
        blank=np.zeros(28,dtype=np.int)
        blank[NameDict[cate]]+=1
        InDict[rec['userID']] =blank
print ('record complete')

user_set=InDict.keys()
for user in user_set:
    tup=InDict[user]
    interestwriter.writerow({"userID":user,'0':tup[0], '1':tup[1],'2':tup[2], '101':tup[3], '103':tup[4], '104':tup[5], '105':tup[6], '106':tup[7], '108':tup[8], '109':tup[9], '110':tup[10],  '201':tup[11], '203':tup[12], '204':tup[13], '209':tup[14], '210':tup[15], '211':tup[16], '301':tup[17], '303':tup[18], '401':tup[19], '402':tup[20], '403':tup[21], '405':tup[22], '406':tup[23], '407':tup[24], '408':tup[25], '409':tup[26], '503':tup[27],'SUM':sum(tup)})
print ('complete')