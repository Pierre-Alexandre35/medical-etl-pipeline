# entrypoint (il prend des arguments avec la CLI, ex ENVvariables, projectID, )
import json 
from google.cloud import bigquery
from pipeline.extract import extract_input_files_to_dataframes
from pipeline.validate import process_dataframes
from utils.file import save_to_file, remove_file_extension

def run_query(input_query: str):
    """Execute a SQL query on GCP BigQuery and save the result of that query on a new .json file"""
    client = bigquery.Client()
    try:
        with open(input_query, "r") as text_file:
            query_reader = text_file.read()
        query_job = client.query(query_reader)
        records = [dict(row) for row in query_job]
        json_obj = json.dumps(str(records))
        result_file_path = remove_file_extension(input_query) + '.json'
        save_to_file(json_obj, result_file_path)
    except FileNotFoundError:
        raise("this file does not exists")


def run_pipeline(input_query: str):
    """Execute every steeps on the pipeline and save the result in a new json file"""
    raw_dataframes = extract_input_files_to_dataframes('data')
    print(res_list = [x[0] for x in raw_dataframes])
    cleaned_dataframes = process_dataframes(raw_dataframes)

