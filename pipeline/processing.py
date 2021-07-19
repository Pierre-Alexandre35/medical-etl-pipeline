import json


def dictionary_to_json(dictonary, output_file):
    data = {}
    data['key'] = 'value'
    json_data = json.dumps(data)
    with open('data.json', 'w', encoding='utf-8') as f:
        f.write(json_data)


ddd = "Preemptive Infiltration With Betamethasone and Ropivacaine for Postoperative Pain in Laminoplasty or \xc3\xb1 Laminectomy"

if "with" in ddd.casefold():
    print(111)