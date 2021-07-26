# Servier Test - ETL Pipeline and SQL Queries 🏥


## Contents
- [Description](#Description)
- [Repository Structure](#Repository_Structure)
- [Installation](#Installation)
- [Q&A](#Q&A)
- [Roadmap](#Roadmap)


## Description

#### Part 1 - Python ETL (Extract, Transform and Load) pipeline to analyze drugs frequency counts on different input sources. 

![A test image](docs/pipeline.png)


- data ingestion: data is extracted from data sources that are not optimized for analytics(.csv, .json) are converted into a Pandas Dataframe format

- data validation: ensure that collected data from different sources meets data quality requirements

- data formating: convert to the various formats and types to adhere to one consistent data structure such as date format

- data storage: load data in a data storage system

- data processing: retrieve data from data storage to generate the graph


#### Part 2 - SQL Queries for sales analysis

- Query 1: total sales
```
SELECT date, sum(prod_price * prod_qty) as total_sales 
FROM `medical.sales`
GROUP BY date
ORDER BY date DESC  
```  

- Query 2: sales by category and by customer ID in 2019
```
SELECT s.client_id,
       sum(case when product_type = 'DECO' then s.prod_price * s.prod_qty else 0 end) deco_sales,
       sum(case when product_type = 'MEUBLE' then s.prod_price * s.prod_qty else 0 end) meuble_sales
FROM  `medical.sales` s join
     `medical.categories` p
     on s.prop_id = p.product_id
WHERE s.date between '2019-01-01' and '2019-12-31'
GROUP by s.client_id ;
```  

## Installation 
<br>

**clone the Github repository**

```git clone https://github.com/Pierre-Alexandre35/servier-test```
<br>

**create your own virtual environment**

```virtualenv dev```
<br>

**activate your virtual environment**

```source dev/bin/activate```
<br>

**install required Python packages**

```pip3 install -r requirements.txt```
<br>

**run the ETL pipeline**

```python main.py --pipeline```
<br>

**run the SQL queries**

```python main.py --query=<QUERY_NAME> ```
```## where QUERY_NAME is total_sales or sales_by_category ```


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
Pour gérer une pipeline d'ingestion de grosses volumétries, il est préférable d'utiliser une solution Cloud afin de stocker nos données mais également de pouvoir mettre en place une pipeline avec un mécanisme de parallélisme pour augmenter la vitesse de traitement global entre l'ingestion de la data et l'output.

Pour l'ingestion il est possible d'utiliser BigQuery qui est une solution GCP de Data Warehouse. BigQuery est optimal lorsque les transformations qu'on effectue sur les données sont faciles à traduire en sql.
Pour le processing d'extraction, de transformation et de loading, si les transformations que l'on effectue sur les données sont assez complexes, je pense opté pour GCP Dataflow voir un framework de calcul distribué tel que Dataproc (avec pyspark).



## Repository_Structure
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


