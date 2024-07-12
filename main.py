import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['figure.figsize'] = [8, 5]
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use("seaborn-v0_8-whitegrid")

path = './datasets/'
df = pd.read_csv(path+'insurance.csv')
print('\n Data sets rows and columns: ',df.shape)

print("\nSHAPE OF DATA \n")
print(df.head())

print("\nDATA DESCRIPTION \n")
print(df.describe())

sns.lmplot(x='bmi', y='charges', data=df, aspect=2, height=7)
plt.xlabel('BMI $(kg/m^2)$: (Independent varaible)')
plt.title('Charges Vs BMI')


plt.figure(figsize=(12,4))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis',yticklabels=False)
plt.title('Missing values')

corr = df.corr()
sns.heatmap(corr, cmap='Wistia', annot=True)

plt.show()