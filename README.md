# Drug ETL pipeline 🏥


## Contents
- [Description](#Description)
- [Architecture](#Architecture)
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


## Roadmap
- Fix file saving path (priority)
- Add the crinimal_trials in the data processing process (priority)
- Add unit tests (priority) 
- Fix CLI to launch the pipeline (priority)
- Removed hard-coded variables and moved them to the settings.py (priority)
- Linter modifications following pip8 convention
- Create a Dockerfile


## Q&A 

Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ? Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de telles volumétries ?
Pour gérer une pipeline d'ingestion de grosses volumétries, il est préférable d'utiliser une solution Cloud afin de stocker nos données mais également de pouvoir mettre en place une pipeline avec un mécanisme de parallelisme pour augmenter la vitesse de traitement global entre l'ingestion de la data et l'output.

Pour l'ingestion il est possible d'utiliser BigQuery qui est une solution GCP de Data Warehouse. BigQuery est optimal lorsque les transformations qu'on effectue sur les données sont facile à traduire en sql.
Pour le processing d'extraction, de transformation et de loading, si les transformations que l'on effectue sur les données sont assez complexes, je pense opté pour GCP Dataflow voir un framework de calcul distribué tel que Dataproc (avec pyspark).


## Architecture
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


