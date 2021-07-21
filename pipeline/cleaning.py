from datetime import datetime
import dateutil.parser

def format_date(dataframe):
    if 'date' in dataframe:
        for row in dataframe['date']:
            dataframe['date'][0] = dateutil.parser.parse(row).strftime(date_format)
        return dataframe

date_format = "%Y-%m-%d"    
    
def clean_dataframes(dataframes):
    for dataframe in dataframes:
        dataframe = format_date(dataframe)
    return dataframes

