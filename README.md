# NLP drug pipeline 🏥


## Contents
- [Description](#Description)
- [Repository](#Repository)
- [Installation](#Installation)


## Description
Part 1 - Python ETL (Extract, Transform and Load) pipeline to analyze drugs frequency counts on different input sources (medical publication, pudmed, ...). 
- data ingestion: ingestion of input files of anny kind of formats (.csv. .json)
- data validation: validate data inside ingested files. If some data can't be used for later analysis, the data is going to be deleted (ex: missing ID)
- data formating: enforce consistency such as every files should ahve the same date format
- data storage: store cleaned data before perform data processing and geenrate the graph 
- data processing: read data from the data storage and generate a graph according to the business requirement 

Part 2 - SQL Queries for sales analysis

## Installation 
```git clone```
<br>

```virtualenv dev-env```
<br>

```pip3 install -r requirements.txt```
<br>

### To run the pipeline 
```python main.py run pipeline INPUT_FOLDER_PATH YAML_SCHEMA_FOLDER_PATH OUTPOUT_FILE```
<br>

### To run the queries
```python main.py run sql OUTPOUT_FILE```


## Repository
```     
├── .github/                                          # Github Actions
├── data/                                             # pipeline input folder
├── devops/                                           # Docker image  
├── pipeline/                                         # Configuration
│   ├── extract.py                                    # pipeline steep 1
│   ├── validate.py                                   # pipeline steep 2
│   ├── clean.py                                      # pipeline steep 3
│   ├── process.py                                    # pipeline steep 4
│   └── schemas/                                      # validation schemas
├── results/  
│   ├── output.json                                   # default location 
│   └── ...                                           # cleaned data files 
├── sql/                                              # SQL queries 
├── tests/                                            # test folder
├── utils/                                            # utils functions
├── main.py                                           # launch the pipeline
└── settings.py
```     


## Roadmap
- Fix file saving path (priority)
- Add the crinimal_trials in the data processing process (priority)
- Add unit tests (priority) 
- Fix CLI to launch the pipeline (priority)
- Removed hard-coded variables and moved them to the settings.py (priority)
- Linter modifications following pip8 convention
