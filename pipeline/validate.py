import pandas as pd
from pandas.core.arrays import boolean
from pandas.core.frame import DataFrame
import pandas_schema
from pandas_schema import Column
from pandas_schema.validation import CustomElementValidation
import bios
from utils.validators import check_null, check_string, check_date, check_decimal
import json

decimal_validation = [CustomElementValidation(lambda i: check_decimal(i), 'is not a decimal')]
string_validation = [CustomElementValidation(lambda i: check_string(i), 'is not a string')]
date_validation = [CustomElementValidation(lambda i: check_string(i), 'is not a valid date')]
null_validation = [CustomElementValidation(lambda i: check_null(i), 'this field cannot be null')]


def apply_validation(dataframe, schema) -> pd.DataFrame:
    """ apply validation schemas and drop unvalid columns """
    errors = schema.validate(dataframe)
    errors_index_rows = [e.row for e in errors]
    data_clean = dataframe.drop(index=errors_index_rows)
    return data_clean


def generate_column(name: str, type: str, is_required: boolean, regex=None) -> Column:
    """ generate a list of Columns based on the schema provided by the user """
    if type != 'string' and type != 'float' and type != 'int' :
        raise TypeError("{{type}} is not supported yet") 
    if type == 'string':
        if is_required:
            return Column(name, string_validation + null_validation)
        return Column(name, string_validation)
    elif type == 'int':
        if is_required:
            return Column(name, decimal_validation + null_validation)
        return Column(name, decimal_validation)        
    else:
        if is_required:
            return Column(name, decimal_validation + null_validation)
        return Column(name, decimal_validation)
        
        
def process_input_schema(input_schema) -> pandas_schema.Schema:
    """ check with functions need to be called based on the schema patterm """
    input_schema_dict = input_schema[1]
    schemas_columns = []
    for item in input_schema_dict:
        name = item
        type = input_schema_dict[item]['type']
        is_required = input_schema_dict[item]['required']
        if 'regex' in input_schema_dict[item]:
            regex = input_schema_dict[item]['regex']
            column = generate_column(name, type, is_required, regex)
        else:
            column = generate_column(name, type, is_required)
        schemas_columns.append(column)
    schema = pandas_schema.Schema(schemas_columns)
    return schema


def validate_dataframes(dataframes: list, schema: str) -> None:
    """ loop over a list of daatframes to apply validation schemas """
    validate_dataframes = []
    input_schema = bios.read(schema)
    for dataframe in dataframes:
        output_schema = process_input_schema(input_schema)
        cleaned_dataframe = apply_validation(dataframe, output_schema)
        validate_dataframes.append(cleaned_dataframe)
    return validate_dataframes
        

        





