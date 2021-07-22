import json
import sys
import os
from google.cloud import bigquery
from pipeline.extract import extract_data
from pipeline.validate import validate_data
from pipeline.cleaning import clean_data
from pipeline.process import process_data
from utils.file import save_to_file, remove_file_extension, dataframe_to_dictionary
from settings import FINAL_RESULT_KEYS
import argparse
import pandas as pd
from pathlib import Path
from functools import reduce
from collections import defaultdict

parser = argparse.ArgumentParser()


def save_data(cleaned_publications, location, format):
    for publication in cleaned_publications:
        file = pd.concat(publication['dataframes'])
        cleaned_dic =  file.set_index('id').T.to_dict('dict')
        print(cleaned_dic)
        r = json.dumps(cleaned_dic)
        path = location + publication['name'] + '.' + format
        with open(path, 'w') as f:
            f.write(r)
            
            
def run_query(input_query: str):
    """Execute a SQL query on GCP BigQuery and save the result of that query on a new .json file"""
    print(input_query)
    if input_query != 'total_sales' and input_query != 'sales_by_category':
        raise ValueError("You must run either the total_sales or sales_by_category query")
    else:
        client = bigquery.Client()
        sql_file = "sql/" + input_query + ".sql"
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


def run_pipeline() -> None:
    """Execute every steeps on the pipeline and save the result in a new json file"""
    
    
    ##raw_publications = extract_data('data/publications/', 'schema.yaml')
    ##validated_publications = validate_data(raw_publications)
    ##cleaned_publications = clean_data(validated_publications)
    ##save_data(cleaned_publications, 'results/pipeline/', 'json')
    process_data('results/pipeline/')

    
    '''

        

    for publication in all_publications:
        file = pd.concat(publication['dataframes'])
        cleaned_dic =  file.set_index('id').T.to_dict('dict')
        r = json.dumps(cleaned_dic)
        path = 'results/pipeline' + publication['name'] + '.json'
        with open(path, 'w') as f:
            f.write(r)
    '''
            
    



        
    
    
    


   
    '''

    for publication in all_publications:
        publication['dataframes'] = clean_dataframes(publication['dataframes'], publication['schema'])


    ## steep 4: save cleaned and formated data into a new folder before to process data
    
    iterator = 0
    d = {}
    for dataframe in cleaned_dataframes:
        d[dataframe['id']] = dataframe.to_dict()
        print(d)

    '''

# steep 5: processing the data to geenrate the graph


def run():
    """ run either the pipeline or SQL aueries based on the user CLI arguments """
    parser.add_argument('--pipeline', nargs='?', const=True, type=bool, default=True, help='run the ETL pipeline')
    parser.add_argument('--query', help='run a query')
    args = parser.parse_args()
    if not any(vars(args).values()):
        print('You must provide some arguments to start the program. Please run main.py --help to know more about our features')
    if args.query:
        run_query(args.query)
    else:
        run_pipeline()


if __name__ == "__main__":
    run()
