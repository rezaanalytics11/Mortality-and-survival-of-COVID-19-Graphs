import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df=pd.read_csv(r'C:\Users\Ariya Rayaneh\Desktop\covid_19_clean_complete.csv')


a=df.groupby(['Date','Country/Region'])['Deaths'].agg(['sum']).reset_index()


k0=[]

for i in a.Date:
 k0.append(int(i.split('/')[0]))

a['month']=k0

b=a.groupby(['month','Country/Region'])['sum'].agg(['sum']).reset_index()
b=b[b['month']==7].sort_values('sum').tail(8)

print(b)


plt.figure(figsize=(20,10))
sns.barplot(data=b,x='Country/Region',y='sum')
plt.title('Eight_Countries_Had_the_Most_of_Corona_Death_in_July.2020')
plt.xlabel('Country',fontsize=14)
plt.ylabel('Number_of_Deaths(x 10e6)',fontsize=14)
plt.show()

# df.Sex=df.Sex.replace(['Female',"Male"],[0,1])
# print(df)
# x=df.drop('Sex',axis=1)
# y=df.iloc[:,-1]
# print(y)
# a=[]
# b=[]
# c=[]
# for k in range(3,30):
#  model=KNeighborsClassifier(k)
#  x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
#  model.fit(x_train,y_train)
#  y_predict=model.predict(x_test)
#  c.append(k)
#  a.append(model.score(x_train,y_train))
#  b.append(model.score(x_test,y_test))
#
# plt.plot(c,a,c='g')
# plt.plot(c,b,c='b')
# plt.xlabel('K',fontsize=14,c='r')
# w=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
# plt.xticks(w)
# plt.ylabel('Score',fontsize=14,c='r')
# plt.legend(['train_data_score','test_data_score'])
#
# plt.show()

