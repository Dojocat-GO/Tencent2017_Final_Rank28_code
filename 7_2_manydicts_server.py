# encoding: utf-8
'''
Created on 2017年6月19日

@author: c
'''
import csv
import numpy as np
import gc
import pandas as pd


# 生成转化率特征：交叉统计

def con_two_dict(dic1,dic2):
    dic=[]
    for item in dic1:
        dic.append(item.copy())
    for i in range(0,len(dic)):
        for k in dic2[i].keys():
            if dic[i].__contains__(k):
                dic[i][k]=np.add(dic[i][k],dic2[i][k])
            else:
                dic[i][k]=dic2[i][k]
    return dic
     
 
def proc(csv_na,con):
    dicts=[]
    for i in range(0,len(con)):
        dicts.append(dict())
    sum=0
    f=csv.DictReader(open(csv_na))
    for rec in f:
        rec['single']='1'
        #print(csv_na,rec['clickTime'])
        label=int(rec['label'])
        for i in range(0,len(con)):
            k=rec[con[i][0]]+'#'+rec[con[i][1]]
            if dicts[i].__contains__(k):
                dicts[i][k]=np.add(dicts[i][k],[label,1])
            else:
                dicts[i][k]=[label,1]
        sum+=1
    return  dicts,sum
  
def merge(csv_na,con,fd,sum,ds):
    f=csv.DictReader(open(csv_na))
    fn=f.fieldnames
    for i in range(0,len(con)):
        k=con[i][0]+'#'+con[i][1]+'cvr'
        fn.append(k)
        k=con[i][0]+'#'+con[i][1]+'clt'
        fn.append(k)
    wrt=csv.DictWriter(open('final'+csv_na,'wb'),fieldnames=fn)
    wrt.writeheader()
    for rec in f:
        time=int(rec['clickTime'])
        if time>=30000000:
            break
        if time<27000000:
            continue
        rec['single']='1'
        for i in range(0,len(con)):
            b=1.0*sum/ds[i]
            k=rec[con[i][0]]+'#'+rec[con[i][1]]
            key=con[i][0]+'#'+con[i][1]+'cvr'
            tup=fd[i].get(k,[0,0])
            if tup[1]==0:
                rec[key]=0.027
            else:
                rec[key]=1.0*(0.027*b+tup[0])/(b+tup[1])
            key=con[i][0]+'#'+con[i][1]+'clt'
            rec[key]=tup[1]
        rec.pop('single')
        wrt.writerow(rec)
     
def mergetest(csv_na,con,fd,sum,ds):
    f=csv.DictReader(open(csv_na))
    fn=f.fieldnames
    for i in range(0,len(con)):
        k=con[i][0]+'#'+con[i][1]+'cvr'
        fn.append(k)
        k=con[i][0]+'#'+con[i][1]+'clt'
        fn.append(k)
    wrt=csv.DictWriter(open('final'+csv_na,'wb'),fieldnames=fn)
    wrt.writeheader()
    for rec in f:
        rec['single']='1'
        for i in range(0,len(con)):
            b=1.0*sum/ds[i]
            k=rec[con[i][0]]+'#'+rec[con[i][1]]
            key=con[i][0]+'#'+con[i][1]+'cvr'
            tup=fd[i].get(k,[0,0])
            if tup[1]==0:
                rec[key]=0.027
            else:
                rec[key]=1.0*(0.027*b+tup[0])/(b+tup[1])
            key=con[i][0]+'#'+con[i][1]+'clt'
            rec[key]=tup[1]
        rec.pop('single')     
        wrt.writerow(rec)
         
 
# content=[['adID','connectionType',0],['camgaignID','connectionType',0],['marriageStatus','residence',0],
#          ['positionID','telecomsOperator',0],['userID','positionID',0],['creativeID','positionID',0],['userID','connectionType',0],['userID','telecomsOperator',0],
#          ['camgaignID','positionID',0],['positionID','single',0],['userID','single',0],['advertiserID','single',0],['appID','positionID',0],
#          ['positionID','connectionType',0],['userID','positionID',1],['userID','appID',1],['appID','positionID',1]]

content=[]
A=['userID', 'age', 'gender', 'education','connectionType', 'telecomsOperator','marriageStatus', 'haveBaby', 'hometown', 'residence'] #10
B=['creativeID', 'adID', 'camgaignID', 'advertiserID', 'appID', 'appPlatform', 'appCategory']                                                                        #7
C=['positionID', 'sitesetID', 'positionType']                                                                                                                                                           #3  
D=['age', 'gender', 'education','marriageStatus', 'haveBaby']

for a in A:
    item=[a,'single']
    content.append(item)
    
for b in B:
    item=[b,'single']
    content.append(item)
    
for c in C:
    item=[c,'single']
    content.append(item)

for a in A:
    for b in B:
        item=[a,b]
        content.append(item)

for a in A:
    for c in C:
        item=[a,c]
        content.append(item)
        
for b in B:
    for c in C:
        item=[b,c]
        content.append(item)

for ix,d in enumerate(D):
    for iy,dd in enumerate(D):
        if ix<iy:
            item=[d,dd]
            content.append(item)

print (content)
print (len(content))

dicts1,sum1=proc('ttr0.csv',content)
print(11)
dicts2,sum2=proc('ttr1.csv',content)
print(12)
dicts3,sum3=proc('ttr2.csv',content)
print(13)
dicts4,sum4=proc('ttr3.csv',content)
print(14)
dicts5,sum5=proc('ttr4.csv',content)
print(15)
  
# findict5=con_two_dict(con_two_dict(con_two_dict(dicts1,dicts2),dicts3),dicts4)
# dicsum5=[len(dc.keys()) for dc in findict5]
# print (dicsum5)
# merge('ttr4.csv',content,findict5,sum1+sum2+sum3+sum4,dicsum5)
# print(25)
# del findict5
# gc.collect()
# findict4=con_two_dict(con_two_dict(con_two_dict(dicts1,dicts2),dicts3),dicts5)
# dicsum4=[len(dc.keys()) for dc in findict4]
# print (dicsum4)
# merge('ttr3.csv',content,findict4,sum1+sum2+sum3+sum5,dicsum4)
# print(24)
# del findict4
# gc.collect()
# findict3=con_two_dict(con_two_dict(con_two_dict(dicts1,dicts2),dicts4),dicts5)
# dicsum3=[len(dc.keys()) for dc in findict3]
# merge('ttr2.csv',content,findict3,sum1+sum2+sum5+sum4,dicsum3)
# print(23)
# del findict3
# gc.collect()
# findict2=con_two_dict(con_two_dict(con_two_dict(dicts1,dicts3),dicts4),dicts5)
# dicsum2=[len(dc.keys()) for dc in findict2]
# merge('ttr1.csv',content,findict2,sum1+sum5+sum3+sum4,dicsum2)
# print(22)
# del findict2
# gc.collect()
findict1=con_two_dict(con_two_dict(con_two_dict(dicts5,dicts2),dicts3),dicts4)
# dicsum1=[len(dc.keys()) for dc in findict1]
# merge('ttr0.csv',content,findict1,sum5+sum2+sum3+sum4,dicsum1)
print(21)
del dicts2
del dicts3
del dicts4
del dicts5
gc.collect()

totaldicts=con_two_dict(findict1,dicts1)
dicsum0=[len(dc.keys()) for dc in totaldicts]
del findict1
del dicts1
gc.collect()
mergetest('test.csv',content,totaldicts,sum1+sum2+sum3+sum4+sum5,dicsum0)
print('f')

"""
def proc1(csv_na,wr):
    f=csv.DictReader(open(csv_na))
    for rec in f:
        t=int(rec['clickTime'])
        wr.writerow(rec)
     
fn=csv.DictReader(open('finalttr0.csv'))
fn=fn.fieldnames
writer=csv.DictWriter(open('finalttr_all.csv','wb'),fieldnames=fn)
writer.writeheader()
proc1('finalttr0.csv', writer)
proc1('finalttr1.csv', writer)
proc1('finalttr2.csv', writer)
proc1('finalttr3.csv', writer)
proc1('finalttr4.csv', writer)


f=pd.read_csv('finalttr_all.csv')

f=f.sort_values('ins')
   
print (f.head(5))
   
f.to_csv('finalttr_all_sort.csv',index=False)
"""




