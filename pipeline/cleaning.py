from datetime import datetime
import dateutil.parser
from settings import INPUT_DATE_FORMAT
import pandas as pd
from settings import INPUT_DATE_COLUMN_NAME


def rename_column(dataframe: pd.DataFrame, input_name: str, output_name: str) -> pd.DataFrame:
    if input_name in dataframe:
        dataframe.rename(columns={input_name: output_name}, inplace=True)
    return dataframe


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
        dataframe = rename_column(dataframe, 'scientific_title', 'title')
    return dataframes


def clean_data(publications):
    for publication in publications:
        publication['dataframes'] = clean_dataframes(publication['dataframes'])
    return publications
