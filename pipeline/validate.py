import pandas as pd
from pandas.core.arrays import boolean
import pandas_schema
from pandas_schema import Column
from pandas_schema.validation import CustomElementValidation
from decimal import *
import datetime
import numpy as np


def check_decimal(dec) -> boolean:
    try:
        Decimal(dec)
    except InvalidOperation:
        return False
    return True


def check_string(string) -> boolean:
    return  isinstance(string, str)


def check_date(date) -> boolean:
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False
    return True


def 

def do_validation(dataframe) -> pd.DataFrame:

    # define validation elements
    decimal_validation = [CustomElementValidation(lambda i: check_decimal(i), 'is not a decimal')]
    string_validation = [CustomElementValidation(lambda i: check_string(i), 'is not a string')]
    date_validation = [CustomElementValidation(lambda i: check_date(i), 'is not a valid date')]
    null_validation = [CustomElementValidation(lambda i: i is not np.nan, 'this field cannot be null')]

    # define validation schema
    schema = pandas_schema.Schema([
            Column('id', decimal_validation + null_validation),
            Column('title', string_validation + null_validation),
            Column('date', date_validation),
            Column('journal', string_validation)])

    # apply validation
    errors = schema.validate(dataframe)
    errors_index_rows = [e.row for e in errors]
    data_clean = dataframe.drop(index=errors_index_rows)
    return dataframe



if __name__ == '__main__':
    do_validation()