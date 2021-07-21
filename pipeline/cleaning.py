from datetime import datetime
import dateutil.parser
from settings import INPUT_DATE_FORMAT
import pandas as pd 
from settings import INPUT_DATE_COLUMN_NAME

def format_date(dataframe: pd.DataFrame) -> pd.DataFrame:
    """ convert the column date in the correct format """
    if 'date' in dataframe:
        for row in dataframe[INPUT_DATE_COLUMN_NAME]:
            dataframe[INPUT_DATE_COLUMN_NAME][0] = dateutil.parser.parse(row).strftime(INPUT_DATE_FORMAT)
        return dataframe

    
def clean_dataframes(dataframes: list) -> list:
    """ format a list of dataframes for data consistency """
    for dataframe in dataframes:
        dataframe = format_date(dataframe)
    return dataframes

