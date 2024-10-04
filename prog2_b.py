import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

google = pd.read_csv('D://datasets//exp2//GOOGL_data.csv')
facebook = pd.read_csv('D://datasets//exp2//FB_data.csv')
apple = pd.read_csv('D://datasets//exp2//AAPL_data.csv')
amazon = pd.read_csv('D://datasets//exp2//AMZN_data.csv')
microsoft = pd.read_csv('D://datasets//exp2//MSFT_data.csv')
plt.figure(figsize=(16,8), dpi = 300)
plt.plot('date', 'close', data = google, label = 'Google')
plt.plot('date', 'close', data = facebook, label = 'Facebook')
plt.plot('date', 'close', data = apple, label = 'Apple')
plt.plot('date', 'close', data = amazon, label = 'Amazon')
plt.plot('date', 'close', data = microsoft, label = 'Microsoft')

plt.xticks(np.arange(0, 1260, 40), rotation = 70)
plt.yticks(np.arange(0, 1450, 100))
plt.title('Stock Trend', fontsize = 16)
plt.ylabel('Closing price in $', fontsize = 14)
plt.grid()
plt.legend()
plt.show()

#---------------------------------------------------------------------------
movie_scores = pd.read_csv('D://datasets//exp2//movie_scores.csv')
plt.figure(figsize=(10, 5), dpi = 300)
pos = np.arange(len(movie_scores['MovieTitle']))
width = 0.3
plt.bar(pos-width/2, movie_scores['Tomatometer'], width, label = 'Tomatometer')
plt.bar(pos+width/2, movie_scores['AudienceScore'], width, label = 'Audience Score')
plt.xticks(pos, rotation = 10)
plt.yticks(np.arange(0, 101, 20))
ax = plt.gca()
ax.set_xticklabels(movie_scores['MovieTitle'])
ax.set_yticks(np.arange(0, 100, 5), minor = True)
ax.yaxis.grid(which = 'major')
ax.yaxis.grid(which = 'minor', linestyle = "--")
plt.title("Movie Comparision")
plt.legend()
plt.show()

#---------------------------------------------------------------------------
bills=sns.load_dataset('tips')
days=['Thur','Fir','Sat','Sun']
days_range=np.arange(len(days))
smoker=['Yes','No']
bills_by_days=[bills[bills['day']==day]for day in days]
bills_by_days_smoker=[[bills_by_days[day][bills_by_days[day]['smoker']==s]for s in smoker ]for day in days_range]
total_by_days_smoker=[[bills_by_days_smoker[day][s]['total_bill'].sum() for s in range(len(smoker))]for day in days_range]
totals=np.asarray(total_by_days_smoker)

plt.figure(figsize=(10,5),dpi=300)
plt.bar(days_range,totals[:,0],label='smoker')
plt.bar(days_range,totals[:,1],bottom=totals[:,0],label='Non-smoker')
plt.legend()
plt.xticks(days_range)
ax=plt.gca()
ax.set_xticklabels(days)
ax.yaxis.grid()
plt.ylabel('Daily total sales in $')
plt.title('Restaurant performance')
plt.show()
#---------------------------------------------------------------------------
scales=pd.read_csv("D://datasets//exp2//smartphone_sales.csv")
plt.figure(figsize=(10, 6), dpi=300)
labels = scales.columns[1:]  
plt.stackplot(scales['Quarter'], scales['Apple'], scales['Samsung'], scales['Huawei'], scales['Xiaomi'], scales['OPPO'], labels=labels)
plt.legend()  
plt.xlabel('Quarter')  
plt.ylabel('Sales units in thousands')
plt.title('Smartphone Sales Units')
plt.show()
#---------------------------------------------------------------------------