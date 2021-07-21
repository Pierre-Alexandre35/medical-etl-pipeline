import json 
import sys
from google.cloud import bigquery
from pipeline.extract import extract_input_files_to_dataframes
from pipeline.validate import validate_dataframes
from pipeline.cleaning import clean_dataframes
from utils.file import save_to_file, remove_file_extension, dataframe_to_dictionary
from settings import SQL_RESULT_FILE_EXTENSION
import click
import pandas as pd


def run_query(input_query: str):
    """Execute a SQL query on GCP BigQuery and save the result of that query on a new .json file"""
    client = bigquery.Client()
    try:
        with open(input_query, "r") as text_file:
            query_reader = text_file.read()
        query_job = client.query(query_reader)
        records = [dict(row) for row in query_job]
        json_obj = json.dumps(str(records))
        result_file_path = remove_file_extension(input_query) + SQL_RESULT_FILE_EXTENSION
        save_to_file(json_obj, result_file_path)
    except FileNotFoundError:
        raise("this file does not exists")


def run_pipeline(input_folder: str, input_schemas_folder: str, result_filename: str) -> None:
    """Execute every steeps on the pipeline and save the result in a new json file"""
    
    ## steep 1: read every input files and convert them into Pandas.Dataframes
    raw_dataframes = extract_input_files_to_dataframes(input_folder)
        
    ## steep 2: check the validity of every row of Pandas.Dataframes by comparing each Dataframe with it's own schema provided by the
    validated_datafrmes = validate_dataframes(raw_dataframes)

    ## steep 3: reformat rows with readable but inconsistent value (ex: different date format)   
    cleaned_dataframes = clean_dataframes(validated_datafrmes)
    
    ## steep 4: save cleaned and formated data into a new folder before to process data
    iterator = 0
    d = {}
    for dataframe in cleaned_dataframes:
        d[dataframe['id']] = dataframe.to_dict()
        print(d)

        
        




    ## steep 5: processing the data to geenrate the graph

      


def run(target: str, input_file_or_folder: str, *args) -> None:
    """ run either the pipeline or SQL aueries based on the user CLI arguments """
    if target not in 'pipeline' and 'custom_queries':
        raise ValueError("The second argument must be either pipeline or sql")
    elif target == 'sql':
        run_query(input_file_or_folder)
    else:
        run_pipeline(input_file_or_folder, args[0], args[1])


        

if __name__ == "__main__":
    args = sys.argv
    globals()[args[1]](*args[2:])



##run_pipeline('data', 'pipeline/schemas', 'result.json')