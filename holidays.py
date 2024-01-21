import pandas as pd
from datetime import date
import holidays
from workalendar.europe import finland

us_holidays = holidays.US()
us_holidays = holidays.country_holidays('US')  # this is a dict

from holidays import country_holidays
us_holidays = country_holidays('US')


for holiday in holidays.Finland(years=[2020, 2021]).items():
    print(holiday)