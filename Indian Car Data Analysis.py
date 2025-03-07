
                     #PROJECT ON CAR DATA ANALYSIS


#importing python libraries which will help us in analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#loading data in pandas data frame
carData_df=pd.read_csv(r'C:\Users\DELL\Documents\car_dataset_india.csv')
print(carData_df)

#exploring our data
print(carData_df.columns)
print(carData_df.describe()) 
print(carData_df.info())    
print(carData_df.shape)
print(carData_df.sample(10))

                    #some basic insights
#most used fuel type
fuel_type_count=carData_df['Fuel_Type'].value_counts()
print(fuel_type_count.sort_values(ascending=False,axis=0).head(1))

#most used transmission type
print(carData_df['Transmission'].value_counts().sort_values(ascending=False,axis=0).head(1))

                   #PRICE ANALYSIS

#price variation of brands according to manufacturing year 2022,2023,2024
v1=carData_df[['Brand','Year','Price']]
v2=v1[v1['Year'].isin([2022,2023,2024])][['Brand','Price','Year']]
price_variation=v2.pivot_table(index='Brand',columns='Year',values='Price',aggfunc='mean').round()
print(price_variation)

price_variation.plot(kind='bar',color=['#F7F7F7','#808080','#F8E231'],figsize=(14,7),zorder=2)
plt.grid(axis='y',linestyle='--',alpha=0.9,zorder=1)
plt.legend(title='year',loc='lower center',bbox_to_anchor=(-0.1,0))
plt.ylabel('prices in million')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.tick_params(axis='x',rotation=30)
plt.title('Price Variation Of Car Brands According to Manufactured Years')
plt.gca().set_facecolor('lightgrey')
plt.show()

#top 5 expensive brands  made in 2024
df1=carData_df[['Brand','Model','Year','Price']].sort_values(by='Year',ascending=False)
df2=df1[df1['Year']==2024][['Brand','Model','Price']]
expensive_brands=df2.pivot_table(index=('Brand','Model'),values='Price',aggfunc='mean').round().sort_values(by='Price',ascending=False).head(5)
print(expensive_brands)

expensive_brands.plot(kind='line',legend=False,color='black',marker='o',markersize=4,markerfacecolor='black',zorder=2)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.ylabel('Prices in million')
plt.grid(axis='x',linestyle='--',color='black',alpha=0.5,zorder=1)
plt.grid(axis='y',linestyle='--',color='black',alpha=0.5,zorder=1)
plt.gca().set_facecolor('#F8E231')
plt.title('Top 5 Expensive Brands Made In 2024')
plt.tick_params(axis='x',rotation=10)
plt.show()

#top 5 affordable brands made in 2024 and their price variation

df11=carData_df[['Brand','Model','Year','Price']].sort_values(by='Year',ascending=False)
df22=df11[df11['Year']==2024][['Brand','Model','Price']]
affordable_brands=df22.pivot_table(index=('Brand','Model'),values='Price',aggfunc='mean').round().sort_values(by='Price',ascending=True).head(5)
print(affordable_brands)

affordable_brands.plot(kind='line',legend=False,color='black',marker='o',markersize=4,markerfacecolor='black',zorder=2)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.ylabel('Prices in million')
plt.grid(axis='x',linestyle='--',color='black',alpha=0.5,zorder=1)
plt.grid(axis='y',linestyle='--',color='black',alpha=0.5,zorder=1)
plt.gca().set_facecolor('#F8E231')
plt.title('Top 5 Affordable Brands Made In 2024')
plt.tick_params(axis='x',rotation=10)
plt.show()



#price variation of brands w.r.t transmission type

T1=carData_df[['Brand','Transmission','Year','Price']]
T2=T1[T1['Year']==2024][['Brand','Transmission','Price']]
T3=T2.pivot_table(index='Brand',columns='Transmission',values='Price',aggfunc='mean').round()
print(T3)


T3.plot(kind='bar',color=['#32CD32','#03055B'],figsize=(12,6),zorder=2)
plt.gca().set_facecolor('#FFFFFF')
plt.tick_params(axis='x',rotation=10)
plt.grid(axis='x',linestyle='--',color='black',alpha=0.5,zorder=1)
plt.grid(axis='y',linestyle='--',color='black',alpha=0.5,zorder=1)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.ylabel('Prices in Million')
plt.title('Price Variation Of Brands w.r.t Transmission')
plt.legend(title='Transmission',loc='lower center',bbox_to_anchor=(-0.1,0))
plt.show()


                         #Fuel_Type Analysis
#Brand wise fuel type distribution

f1=carData_df.groupby(['Brand','Fuel_Type']).size().reset_index(name='count')
brandwise_fuel_distribution=f1.pivot_table(index='Brand',columns='Fuel_Type',values='count')
print(brandwise_fuel_distribution)

plt.figure(figsize=(14,6))
sns.heatmap(brandwise_fuel_distribution,annot=True,cmap='cividis',fmt='.2f',cbar_kws={'label':'Fuel Type Count'})
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.title('Brand Wise Fuel Type Distribution')
plt.show()

#Average mileage of brands w.r.t different fuel types

a=carData_df[['Brand','Fuel_Type','Mileage']]
avg_mileage=a.pivot_table(index='Brand',columns='Fuel_Type',values='Mileage',aggfunc='mean').round(2)
print(avg_mileage)

avg_mileage.plot(kind='bar',color=['#F7F7F7','#808080','#F8E231','#4169E1'],figsize=(12,6),zorder=2)
plt.xlabel('brands')
plt.ylabel('mileage(km/L')
plt.title('Average Mileage Of Brands w.r.t Different Fuel Type')
plt.grid(axis='y',linestyle='--',color='black',alpha=0.9,zorder=1)
plt.ylim(10.0,None)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.legend(loc='upper right',bbox_to_anchor=(0.2,-0.2))
plt.gca().set_facecolor('lightgrey')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x,loc:"{:.2f}".format(x)))
plt.tight_layout()
plt.show()

#relationship between engine cc and fuel type on mileage

em=carData_df[['Engine_CC','Fuel_Type','Mileage']]
em1=em.pivot_table(index='Engine_CC',columns='Fuel_Type',values='Mileage',aggfunc='mean').round(2)
print(em1)

em1.plot(kind='line',figsize=(13,6),zorder=2,marker='o',markersize=5,markerfacecolor='white')
plt.ylabel('mileage(km/L)')
plt.grid(axis='y',linestyle='--',alpha=0.9,zorder=1)
plt.legend(loc='upper right',bbox_to_anchor=(0.1,-0.1))
plt.gca().set_facecolor('#333333')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.title('Interaction between Engine_CC and Mileage on Fuel type')
plt.tight_layout()
plt.show()


#Model wise transmission distribution

mt1=carData_df.groupby(['Model','Transmission']).size().reset_index(name='count')
modelwise_trans_distribution=mt1.pivot_table(index='Model',columns='Transmission',values='count')
print(modelwise_trans_distribution)

modelwise_trans_distribution.plot(kind='bar',color=['#F8E231','#4169E1'],figsize=(16,8),zorder=2)
plt.grid(axis='y',linestyle='--',color='white',alpha=0.6,zorder=1)
plt.title('Model Wise Transmission Distribution')
plt.gca().set_facecolor('#333333')
plt.ylabel('Transmission Count')
plt.show()


                        #seating Analysis
#Distribution of seating capacity
sc=carData_df[['Brand','Model','Seating_Capacity']]
s1=sc['Seating_Capacity']

print(s1)

plt.hist(s1,bins=10,color='#228B22',edgecolor='black',zorder=2)
plt.grid(axis='y',linestyle='--',alpha=0.9,zorder=1)
plt.xlabel('Seating capacity')
plt.ylabel('Frequency')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.gca().set_facecolor('#F0F0F0')
plt.title('Distribution of seating capacities')
plt.show()

print(s1.describe())   #summary statistics of seating capacity


        #comparison of seating capacity by each brand
#we define a function which will take brand name as input from user and return seating capacities of all
# models of that brand and will also give us its graphical visual

s=carData_df[['Brand','Model','Seating_Capacity']]
def brand_name():
    bn=str(input('enter a brand'))
    r1=s[(s['Brand']==bn)][['Model','Seating_Capacity']]
    required_result=r1.groupby('Model')['Seating_Capacity'].mean().round()
    print(required_result)
    required_result.plot(kind='line',marker='o',markersize=5,markerfacecolor='white',zorder=2)
    plt.grid(axis='y',linestyle='--',alpha=1.0,zorder=1)
    plt.xticks(fontweight='bold')
    plt.yticks(fontweight='bold')
    plt.gca().set_facecolor('#E5E5E5')
    plt.xlabel('models')
    plt.ylabel('seating_capacity')
    plt.show()

print(brand_name())


#defined a function which will gives the model wise seating capacity comparison of all
#brands

ms=carData_df[['Brand','Model','Seating_Capacity']]
def brand_comparison():
    allbrands=['Honda','Hyundai','Kia','Mahindra','Maruti Suzuki','Renault','Skoda','Tata Motors','Toyota','Volkswagen']
    fig,axes=plt.subplots(2,5,figsize=(14,8),facecolor='#8BC34A')
    axes=axes.flatten()
    for i,brand in enumerate(allbrands):
        r2=ms.loc[ms['Brand']==brand,['Model','Seating_Capacity']]
        result=r2.groupby('Model')['Seating_Capacity'].mean().round()
        result.plot(kind='bar',color='#CCCCCC',ax=axes[i],zorder=2)
        axes[i].grid(axis='y',linestyle='--',alpha=0.6,zorder=1)
        axes[i].set_facecolor('#333333')
        axes[i].tick_params(axis='x',rotation=45,labelsize=10)
        axes[i].set_title(f"{brand}")
        axes[i].set_xlabel("")
    plt.suptitle('Car Brands With Their Respective Models Seating Capacities')
    plt.subplots_adjust(hspace=0.4,wspace=0.3) 
    plt.show()

print(brand_comparison())


                                #service cost analysis
                            #service cost analysis car models made in year 2024
t=carData_df[['Brand','Model','Year','Service_Cost']]

def geometric_mean(x): #this will help us to find geometric mean bcz we can't use mean here as service cost is skewed
    return np.exp(np.mean(np.log(x)))

allbrands=['Honda','Hyundai','Kia','Mahindra','Maruti Suzuki','Renault','Skoda','Tata Motors','Toyota','Volkswagen']
fig,axes=plt.subplots(2,5,figsize=(18,8),facecolor='#F7F7F7')
axes=axes.flatten()
for i,brand in enumerate(allbrands):
    t1=t[t['Year']==2024][['Brand','Model','Service_Cost']].groupby(['Brand','Model'])['Service_Cost'].apply(geometric_mean).reset_index().round(2)
    for j,brand in enumerate(allbrands):
        t11=t1[t1['Brand']==brand][['Model','Service_Cost']].set_index('Model')
        t11.plot(kind='line',legend=False,color='#03A9F4',marker='o',markersize=4,markerfacecolor='black',ax=axes[j],zorder=2)
        axes[j].grid(axis='y',linestyle='--',alpha=0.6,zorder=1)
        axes[j].set_facecolor('#C9E4CA')
        axes[j].tick_params(axis='x',rotation=45,labelsize=10)
        axes[j].set_title(f"{brand}")
        axes[j].set_xlabel("")
plt.suptitle('2024 Car Models and their Service Cost')
plt.subplots_adjust(hspace=0.4,wspace=0.3)
plt.tight_layout(pad=2)
plt.show()


                    #service cost analysis car models made in year 2023

t=carData_df[['Brand','Model','Year','Service_Cost']]

def geometric_mean(x): #this will help us to find geometric mean bcz we can't use mean here as service cost is skewed
    return np.exp(np.mean(np.log(x)))

allbrands=['Honda','Hyundai','Kia','Mahindra','Maruti Suzuki','Renault','Skoda','Tata Motors','Toyota','Volkswagen']
fig,axes=plt.subplots(2,5,figsize=(18,8),facecolor='#F7F7F7')
axes=axes.flatten()
for i,brand in enumerate(allbrands):
    t2=t[t['Year']==2023][['Brand','Model','Service_Cost']].groupby(['Brand','Model'])['Service_Cost'].apply(geometric_mean).reset_index().round(2)
    for j,brand in enumerate(allbrands):
        t22=t2[t2['Brand']==brand][['Model','Service_Cost']].set_index('Model')
        t22.plot(kind='line',legend=False,color='#03A9F4',marker='o',markersize=4,markerfacecolor='black',ax=axes[j],zorder=2)
        axes[j].grid(axis='y',linestyle='--',alpha=0.6,zorder=1)
        axes[j].set_facecolor('#C9E4CA')
        axes[j].tick_params(axis='x',rotation=45,labelsize=10)
        axes[j].set_title(f"{brand}")
        axes[j].set_xlabel("")
plt.suptitle('2023 Car Models and their Service Cost')
plt.subplots_adjust(hspace=0.4,wspace=0.3)
plt.tight_layout(pad=2)
plt.show()



                #service cost analysis car models made in year 2022


t=carData_df[['Brand','Model','Year','Service_Cost']]

def geometric_mean(x): #this will help us to find geometric mean bcz we can't use mean here as service cost is skewed
    return np.exp(np.mean(np.log(x)))

allbrands=['Honda','Hyundai','Kia','Mahindra','Maruti Suzuki','Renault','Skoda','Tata Motors','Toyota','Volkswagen']
fig,axes=plt.subplots(2,5,figsize=(18,8),facecolor='#F7F7F7')
axes=axes.flatten()
for i,brand in enumerate(allbrands):
    t3=t[t['Year']==2022][['Brand','Model','Service_Cost']].groupby(['Brand','Model'])['Service_Cost'].apply(geometric_mean).reset_index().round(2)
    for j,brand in enumerate(allbrands):
        t33=t3[t3['Brand']==brand][['Model','Service_Cost']].set_index('Model')
        t33.plot(kind='line',legend=False,color='#03A9F4',marker='o',markersize=4,markerfacecolor='black',ax=axes[j],zorder=2)
        axes[j].grid(axis='y',linestyle='--',alpha=0.6,zorder=1)
        axes[j].set_facecolor('#C9E4CA')
        axes[j].tick_params(axis='x',rotation=45,labelsize=10)
        axes[j].set_title(f"{brand}")
        axes[j].set_xlabel("")
plt.suptitle('2022 Car Models and their Service Cost')
plt.subplots_adjust(hspace=0.4,wspace=0.3)
plt.tight_layout(pad=2)
plt.show()






