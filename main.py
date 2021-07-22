import argparse
from pipeline.extract import extract_data
from pipeline.validate import validate_data
from pipeline.cleaning import clean_data
from pipeline.save import save_data
from pipeline.process import process_data
from sql.queries import execute_query


parser = argparse.ArgumentParser()


def run_query(input_query: str):
    """Execute a SQL query on GCP BigQuery and save the result of that query on a new .json file"""
    if input_query != 'total_sales' and input_query != 'sales_by_category':
        raise ValueError("You must run either the total_sales or sales_by_category query")
    else:
        execute_query(input_query)


def run_pipeline() -> None:
    """Execute every steeps on the pipeline and save the result in a new json file"""

    raw_publications = extract_data('data/publications/', 'schema.yaml')
    validated_publications = validate_data(raw_publications)
    cleaned_publications = clean_data(validated_publications)
    save_data(cleaned_publications, 'results/pipeline/storage/', 'json')
    process_data('results/pipeline/storage/', 'results/pipeline/graph.json')


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
