import os


## Google Cloud Platform
if "GCP_PROJECT_ID" in os.environ:
    GCP_PROJECT_ID = os.environ['GCP_PROJECT_ID']
else:
    GCP_PROJECT_ID = "sbx-da"


## Queries
QUERY_ONE = "total_sales"
QUERY_TWO = "sales_by_category"
QUERY_RESULT_FOLDER = "results/sql/"

## Pipeline
DATE_FORMAT = "%Y-%m-%d"
PIPELINE_RESULT_FOLDER_NAME = "results/pipeline/"
PIPELINE_STORAGE_FOLDER = "storage/"
PIPELINE_GRAPH_FILE_NAME = "graph.json"
PIPELINE_INPUT_DATA_FOLDER = "data/"
PIPELINE_PUBLICATIONS_FOLDER = "publications/"
PIPELINE_DRUGS_FOLDER = "drugs/"
PIPELINE_DATA_SCHEMA_FILENAME = "schema.yaml"
PIPELINE_PUBLICATIONS_COLUMNS = ["id", "title", "date", "journal"]
PIPELINE_DRUGS_COLUMNS = ["atccode", "drug"]

## to clean
DRUGS_FILENAME = "drugs.json"
CLINICAL_TRIALS_FILENAME = "clinical_trials.json"
PUBMED_FILENAME = "pubmed.json"
GRAPH_NAME = "graph.json"
INPUT_DATE_COLUMN_NAME = "date"
INPUT_DATE_FORMAT = "%Y-%m-%d"
FINAL_RESULT_KEYS = ["type",
                     "drug_id",
                     "drog_name",
                     "title",
                     "journal",
                     "date"
                     ]
