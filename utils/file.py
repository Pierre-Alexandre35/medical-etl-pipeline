import json
from pathlib import Path


def remove_file_extension(filepath: str) -> str:
    pth = Path(filepath)
    fn = pth.with_suffix('').stem
    return fn 


def save_to_file(input_data: str, filepath: str) -> None:
    with open(filepath, 'w') as the_file:
        the_file.write(input_data)
        
def dataframe_to_dictionary(dataframe):
    first_column = dataframe.columns[0]
    dic = dataframe.set_index(first_column).T.to_dict('list')
    return dic


def dictionary_to_json(dictonary, output_file):
    data = {}
    data['key'] = 'value'
    json_data = json.dumps(data)
    with open('data.json', 'w', encoding='utf-8') as f:
        f.write(json_data)