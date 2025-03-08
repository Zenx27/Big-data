import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


np.random.seed(42)
data = {
    'Дата': pd.date_range(start='2024-01-01', periods=30, freq='D'),
    'Продажи': np.random.randint(50, 200, size=30),
    'Цена': np.random.uniform(10, 50, size=30)
}
df = pd.DataFrame(data)
df['Выручка'] = df['Продажи'] * df['Цена']


mean_sales = df['Продажи'].mean()
median_sales = df['Продажи'].median()
max_sales = df['Продажи'].max()
min_sales = df['Продажи'].min()
std_sales = df['Продажи'].std()


print("Средние продажи:", mean_sales)
print("Медиана продаж:", median_sales)
print("Максимальные продажи:", max_sales)
print("Минимальные продажи:", min_sales)
print("Стандартное отклонение продаж:", std_sales)


plt.figure(figsize=(10, 5))
plt.plot(df['Дата'], df['Продажи'], marker='o', linestyle='-', label='Продажи')
plt.axhline(mean_sales, color='r', linestyle='--', label='Средние продажи')
plt.xlabel('Дата')
plt.ylabel('Количество продаж')
plt.title('Анализ продаж товаров')
plt.legend()
plt.grid()
plt.show()
