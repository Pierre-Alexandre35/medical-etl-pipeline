from google.cloud import bigquery
from utils.file import save_to_file, remove_file_extension
import json


client = bigquery.Client()


def execute_query(query_name: str) -> None:
    sql_file = "sql/" + query_name + ".sql"
    try:
        with open(sql_file, "r") as text_file:
            query_reader = text_file.read()
        query_job = client.query(query_reader)
        records = [dict(row) for row in query_job]
        json_obj = json.dumps(str(records))
        result_file_path = "results/sql/" + remove_file_extension(query_name) + ".json"
        save_to_file(json_obj, result_file_path)
    except FileNotFoundError:
        raise("this sql query does not exists")
