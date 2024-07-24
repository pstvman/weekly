"""功能说明
按月生成daily.md的工作模板
"""
year = 2022
for month in range(1, 13):
    filename = str(year) + '-' + str(month).rjust(2, '0') + '工作(事务型).md'

    with open(filename, mode='a') as f:
        f.write('|日期(2021.' + str(month).rjust(2, '0') + ')|事务|\n')
        f.write('|:----:|:----|\n')
        if month in [1, 3, 5, 7, 8, 10, 12]:
            days = 31 + 1
        elif month in [4, 6, 9, 11]:
            days = 30 + 1
        else:
            days = 28 + 1
        for day in range(1, days):
            date = '|2021.' + str(month).rjust(2, '0') + '.' + str(day).rjust(2, '0') + '|'

            f.write(date + '\n')
    f.close()
