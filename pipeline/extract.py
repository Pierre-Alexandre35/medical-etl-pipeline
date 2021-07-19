import pandas as pd
from pandas import json_normalize
import pathlib
import os
import json
import yaml


def read_json_file(filename):
    #Another option is to parse it as YAML; YAML accepts valid JSON but also accepts all sorts of variations.
    yaml_data = yaml.safe_load(open(filename))
    json_data = json.dumps(yaml_data)
    dictionnary_data = json.loads(json_data)
    dataframe = pd.DataFrame.from_dict(dictionnary_data)
    return dataframe


def read_csv_file(filename):
    dataframe = pd.read_csv(filename)
    return dataframe
        
        
def read_input_file(filename):
    file_extension = pathlib.Path(filename).suffix
    if file_extension != ".csv" and file_extension != ".json":
        raise ValueError(f"{filename} is not supported.")
    if file_extension == '.csv':
        return read_csv_file(filename)
    else:
        return read_json_file(filename)


def extract_input_files_to_dataframes(input_folder):
    dataframes = []
    for filename in os.listdir(input_folder):
        dataframe = read_input_file(input_folder + '/' + filename)
        dataframes.append(dataframe)
    return dataframes
        




