from datetime import date
from num2words import num2words

print('Hello, World!')

day_of_year = date.today().timetuple().tm_yday
ordinal_day_of_year = num2words(day_of_year, to='ordinal_num')

print(f'This is the {ordinal_day_of_year} day of the year.')