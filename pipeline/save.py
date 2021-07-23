import json
import pandas as pd


def save_data(cleaned_publications, location, format):
    for publication in cleaned_publications:
        file = pd.concat(publication['dataframes'])
        cleaned_dic = file.set_index('id').T.to_dict('dict')
        r = json.dumps(cleaned_dic)
        path = location + publication['name'] + '.' + format
        with open(path, 'w') as f:
            f.write(r)
