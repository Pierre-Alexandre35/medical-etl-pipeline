import json 
import sys
from google.cloud import bigquery
from pipeline.extract import extract_input_files_to_dataframes
from pipeline.validate import validate_dataframes
from pipeline.cleaning import clean_dataframes
from utils.file import save_to_file, remove_file_extension, dataframe_to_dictionary
from settings import FINAL_RESULT_KEYS
import argparse
import pandas as pd

parser = argparse.ArgumentParser()


def run_query(input_query: str):
    """Execute a SQL query on GCP BigQuery and save the result of that query on a new .json file"""
    print(input_query)
    if input_query != 'total_sales' and input_query != 'sales_by_category':
        raise ValueError("You must run either the total_sales or sales_by_category query")
    else: 
        client = bigquery.Client()
        sql_file = "sql/"  + input_query + ".sql"
        try:
            with open(sql_file, "r") as text_file:
                query_reader = text_file.read()
            query_job = client.query(query_reader)
            records = [dict(row) for row in query_job]
            json_obj = json.dumps(str(records))
            result_file_path = "results/sql/" + remove_file_extension(input_query) + ".json"
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

      


def run():
    """ run either the pipeline or SQL aueries based on the user CLI arguments """
    parser.add_argument('--pipeline',  nargs='?', const=True, type=bool, default=True,help='run the ETL pipeline')
    parser.add_argument('--query', help='run a query')
    args = parser.parse_args()
    if not any(vars(args).values()):
        print('You must provide some arguments to start the program. Please run main.py --help to know more about our features'
    if args.query:
        run_query(args.query)
    else:
        run_pipeline()



if __name__ == "__main__":
    run()
    
    