import pandas as pd
from pandas.core.arrays import boolean
import pandas_schema
from pandas_schema import Column
from pandas_schema.validation import CustomElementValidation
from decimal import *
import datetime
import numpy as np
import bios


def check_null(string):
    if isinstance(string, float):
        return pd.isna(string)
    else:
        return len(string) > 2


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


def dataframe_to_BQ(dataframe) -> None:
    dataframe.to_gbq('test', 
                 Context.default().project_id,
                 chunksize=10000, 
                 if_exists='append',
                 verbose=False
                 )

def do_validation(dataframe, schema) -> pd.DataFrame:
    # apply validation
    errors = schema.validate(dataframe)
    errors_index_rows = [e.row for e in errors]
    data_clean = dataframe.drop(index=errors_index_rows)
    
    return data_clean


def process_input_schema(input_schema):
    input_schema_dict = input_schema[1]
    schemas_columns = []
    for item in input_schema_dict:
        name = item
        type = input_schema_dict[item]['type']
        is_required = input_schema_dict[item]['required']
        column = Column(name, type, is_required)
        print(column)
        schemas_columns.append(column)
    print(schemas_columns)
        
    
    '''
     # define validation elements
    decimal_validation = [CustomElementValidation(lambda i: check_string(i), 'is not a decimal')]
    string_validation = [CustomElementValidation(lambda i: check_string(i), 'is not a string')]
    date_validation = [CustomElementValidation(lambda i: check_string(i), 'is not a valid date')]
    null_validation = [CustomElementValidation(lambda i: check_null(i), 'this field cannot be null')]
    
    # define validation schema
    schema = pandas_schema.Schema([
            Column('id', string_validation + null_validation),
            Column('scientific_title', string_validation + null_validation),
            Column('date', string_validation),
            Column('journal', string_validation)])
    return schema
    '''

def process_dataframes(dataframes):
    input_schema = bios.read("pipeline/schemas/pubmed.yaml")
    process_input_schema(input_schema)
    
    '''
    print(dataframes[0])
    c = do_validation(dataframes[3])
    print(c)
    '''