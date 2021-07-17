import pandas as pd
import pathlib
import os


def read_input_file(filename):
    file_extension = pathlib.Path(filename).suffix
    if file_extension == '.csv':
        df = pd.read_csv(filename)
        print(df)
    

'''
df = pd.read_csv("./text.txt")
df_to_doct = df.to_dict()


a_json = json.loads(json_string)
print(a_json)

dataframe = pd.DataFrame.from_dict(a_json)
'''


def ingestion(input_folder):
    for filename in os.listdir(input_folder):
        read_input_file(input_folder + '/' + filename)
        
ingestion('input_data')