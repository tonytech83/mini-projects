"""
Rename the files form "wod-day-month-year.txt" to "year-month-day.txt"
"""
import os

os.chdir('./output')
print(os.getcwd())

for idx, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)

    if f_ext != '.zip':
        wod, day, month, year = f_name.split('-')
        new_name = f'{year}-{month}-{day}{f_ext}'
        os.rename(f, new_name)