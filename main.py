import argparse
from pipeline.extract import extract_data
from pipeline.validate import validate_data
from pipeline.cleaning import clean_data
from pipeline.save import save_data
from pipeline.process import process_data
from sql.queries import execute_query
from settings import (PIPELINE_STORAGE_FOLDER,
                      QUERY_ONE, QUERY_TWO,
                      PIPELINE_RESULT_FOLDER_NAME,
                      PIPELINE_GRAPH_FILE_NAME,
                      PIPELINE_PUBLICATIONS_FOLDER,
                      PIPELINE_INPUT_DATA_FOLDER,
                      PIPELINE_DATA_SCHEMA_FILENAME)


LOCAL_DB_STORAGE_PATH = PIPELINE_RESULT_FOLDER_NAME + PIPELINE_STORAGE_FOLDER
FINAL_GRAPH_PATH = PIPELINE_RESULT_FOLDER_NAME + PIPELINE_GRAPH_FILE_NAME
INPUT_PUBLICATIONS_PATH = PIPELINE_INPUT_DATA_FOLDER + PIPELINE_PUBLICATIONS_FOLDER
parser = argparse.ArgumentParser()


def run_query(input_query: str) -> None:
    """Execute a SQL query on GCP BigQuery and save the result of that query on a new .json file"""
    if input_query != QUERY_ONE and input_query != QUERY_TWO:
        raise ValueError(f"You must run either the {QUERY_ONE} or {QUERY_TWO} query")
    else:
        execute_query(input_query)


def run_pipeline() -> None:
    """Execute every steeps on the pipeline and save the result in a new json file"""
    raw_publications = extract_data(INPUT_PUBLICATIONS_PATH, PIPELINE_DATA_SCHEMA_FILENAME)
    validated_publications = validate_data(raw_publications)
    cleaned_publications = clean_data(validated_publications)
    save_data(cleaned_publications, LOCAL_DB_STORAGE_PATH, 'json')
    process_data(LOCAL_DB_STORAGE_PATH, FINAL_GRAPH_PATH)


def run() -> None:
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
