import os
from datetime import datetime, timedelta

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
eugene_path = os.path.join(homework_path, 'eugene_okulik')
hw13_path = os.path.join(eugene_path, 'hw_13', 'data.txt')

with open(hw13_path, 'r', encoding='utf-8') as data_file:
    for line in data_file.readlines():
        if 'дату' in line[32:]:
            print(f"На неделю позже будет  {(datetime.strptime(line[3:29], '%Y-%m-%d %H:%M:%S.%f') +
                                             timedelta(days=7))}")
        elif 'день' in line[32:]:
            print(f"{datetime.strptime(line[3:29], '%Y-%m-%d %H:%M:%S.%f' )}  - "
                  f" это {datetime.strptime(line[3:29],'%Y-%m-%d %H:%M:%S.%f' ).strftime('%A')}")
        elif 'дней' in line[32:]:
            print(f'{(datetime.now() - (datetime.strptime(line[3:29], '%Y-%m-%d %H:%M:%S.%f'))).days} '
                  f'дней назад была дата {datetime.strptime(line[3:29], '%Y-%m-%d %H:%M:%S.%f')}')
