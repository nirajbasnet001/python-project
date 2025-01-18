import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

file_path = 'C:/Users/neera/OneDrive/Desktop/fifa_ranking_2022-10-06.csv'
data = pd.read_csv(file_path)

x = data['rank'].values.reshape(-1, 1)  
y = data['points'].values  

model = LinearRegression()
model.fit(x, y)


y_pred = model.predict(x)


r_squared = r2_score(y, y_pred)

plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['rank'], y=data['points'], label='Data', color='blue')
plt.plot(data['rank'], y_pred, color='red', label='Regression Line')
plt.title('Linear Regression: Rank vs Points', fontsize=16)
plt.xlabel('Rank', fontsize=14)
plt.ylabel('Points', fontsize=14)
plt.legend()
plt.grid(True)
plt.text(10, min(y), f'R² = {r_squared:.2f}', fontsize=12, color='green')
plt.show()