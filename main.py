import pandas as pd
import math  # Импортируем модуль math для округления

from generator_input_date import generate_unique_random_numbers


# функция - генерато случайных чисел выборки
generate_unique_random_numbers(count=..., range_nums=..., filename='input_date.csv')

# Запрос имени CSV-файла от пользователя
csv_file: str = 'input_date.csv'

# Чтение данных из CSV-файла в DataFrame
df = pd.read_csv(csv_file, names=['x', ])

# Рассчитываем значение k в зависимости от количества значений
N = len(df)
if N <= 20:
    k = 4
else:
    k = 5

# Сортируем данные по столбцу 'x'
df.sort_values(by='x', inplace=True)

# Рассчитываем границы интервалов
x_min = df['x'].min()
x_max = df['x'].max()
interval_width = math.ceil((x_max - x_min) / k)  # Округляем вверх до целого числа

# Создаем список интервалов
intervals = [(x_min + i * interval_width, x_min + (i + 1) * interval_width) for i in range(k)]

# Создаем новую таблицу для интервалов
interval_table = pd.DataFrame({
    'N': range(1, k + 1),
    'Границы интервалов': intervals,
    'Частота': [((df['x'] >= lower) & (df['x'] < upper)).sum() for lower, upper in intervals],
})

# Рассчитываем накопленную частоту
interval_table['Накопленная частота'] = interval_table['Частота'].cumsum()

# Рассчитываем частость и накопленную частость
interval_table['Частость'] = interval_table['Частота'] / N
interval_table['Накопленная частость'] = interval_table['Накопленная частота'] / N

# Рассчитываем среднее значение в каждом интервале
interval_table['Среднее значение'] = [(lower + upper) / 2 for lower, upper in intervals]

# Выводим таблицу интервалов
print("Таблица интервалов:")
print(interval_table)

# Сохраняем результат в новый CSV-файл
output_file = 'обработанные_' + csv_file
interval_table.to_csv(output_file, index=False)

print(f"Результат сохранен в файл: {output_file}")
