import pandas as pd
from pandas import json_normalize
import pathlib
import os
import json
from pandas.core.frame import DataFrame
import yaml
from utils.file import remove_file_extension

def read_json_file(filename: str) -> DataFrame:
    #Another option is to parse it as YAML; YAML accepts valid JSON but also accepts all sorts of variations.
    yaml_data = yaml.safe_load(open(filename))
    json_data = json.dumps(yaml_data)
    dictionnary_data = json.loads(json_data)
    dataframe = pd.DataFrame.from_dict(dictionnary_data)
    return dataframe


def read_csv_file(filename: str) -> DataFrame:
    dataframe = pd.read_csv(filename)
    return dataframe
        
        
def read_input_file(filename: str) -> function:
    file_extension = pathlib.Path(filename).suffix
    if file_extension != ".csv" and file_extension != ".json":
        raise ValueError(f"{filename} is not supported.")
    if file_extension == '.csv':
        return read_csv_file(filename)
    else:
        return read_json_file(filename)


def extract_input_files_to_dataframes(input_folder: str) -> tuple:
    dataframes = []
    for filename in os.listdir(input_folder):
        file_relative_path = input_folder + '/' + filename
        dataframe = read_input_file(file_relative_path)
        extracted_file = (remove_file_extension(file_relative_path), dataframe)
        dataframes.append(extracted_file)
    return dataframes
        




