import pandas as pd
from pandas.core.arrays import boolean
from decimal import *
import datetime    


def check_null(string):
    '''
    if isinstance(string, float):
        return pd.isna(string)
    elif isinstance(string, int):
        return pd.isna(string)
    else:
        return len(string) > 0
    '''
    if isinstance(string, float) or isinstance(string, int):
        string = str(string)
    else:
        string = string.strip()
    return len(string) > 0
    


def check_decimal(dec) -> boolean:
    try:
        Decimal(dec)
    except InvalidOperation:
        return False
    return True


def check_string(string) -> boolean:
    return isinstance(string, str)


def check_date(date) -> boolean:
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False
    return True