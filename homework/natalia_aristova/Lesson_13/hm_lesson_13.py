import os
from datetime import datetime, timedelta

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
eugene_path = os.path.join(homework_path, 'eugene_okulik')
hw13_path = os.path.join(eugene_path, 'hw_13', 'data.txt')

with open(hw13_path, 'r', encoding='utf-8') as data_file:
    for line in data_file.readlines():
        data = datetime.strptime(line[3:29], '%Y-%m-%d %H:%M:%S.%f')
        if 'дату' in line:
            print(f'Через неделю будет {data + timedelta(days=7)}')
        elif 'день' in line:
            print(f"{data} - это {data.strftime('%A')}")
        elif 'дней' in line:
            print(f'{(datetime.now() - data).days} дней назад была дата {data}')
