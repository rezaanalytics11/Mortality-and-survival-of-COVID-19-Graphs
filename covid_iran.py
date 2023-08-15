import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df=pd.read_csv(r'C:\Users\Ariya Rayaneh\Desktop\covid_19_clean_complete.csv')

df_iran=df[df['Country/Region']=='Iran']

a=df_iran.groupby('Date')['Deaths'].agg('max').reset_index()
aa=df_iran.groupby('Date')['Confirmed'].agg('max').reset_index()

k=[]

for i in a.Date:
    k.append(i.split('/')[0])

a['month']=k
aa['month']=k

b=a.groupby('month')['Deaths'].agg('sum').reset_index()
bb=aa.groupby('month')['Confirmed'].agg('sum').reset_index()

c=b.merge(bb)


ax = c.plot.area(x='month')


print(c)
# plt.figure(figsize=(20,10))
# sns.lineplot(data=b,x='month',y='Deaths',c='r',label='Death')
# sns.lineplot(data=bb,x='month',y='Confirmed',label='Confirmed')
plt.ylabel('Number_of_People',fontsize=14)
plt.xlabel('Month(2020)',fontsize=14)
plt.title('Corona_Confirmed_VS_Death_in_Iran_2020')

plt.show()