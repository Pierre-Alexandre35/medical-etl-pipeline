import pandas as pd
from pandas.core.arrays import boolean
from decimal import *
import datetime    


def check_null(non_empty_string: str):
    """ return true if the input value is non empty """
    '''
    if isinstance(string, float):
        return pd.isna(string)
    elif isinstance(string, int):
        return pd.isna(string)
    else:
        return len(string) > 0
    '''
    if isinstance(non_empty_string, float) or isinstance(non_empty_string, int):
        non_empty_string = str(non_empty_string)
    else:
        non_empty_string = non_empty_string.strip()
    return len(non_empty_string) > 0
    


def check_decimal(dec: Decimal) -> boolean:
    """ return true if the input value is a decimal number """
    try:
        Decimal(dec)
    except InvalidOperation:
        return False
    return True


def check_string(string: str) -> boolean:
    """ return true if the input value is a string """
    return isinstance(string, str)


def check_date(date: str) -> boolean:
    """ return true if the input value is a date under '%Y-%m-%d' format """
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False
    return True