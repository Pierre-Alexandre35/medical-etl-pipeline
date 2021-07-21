import json
  
    
# Opening JSON file
with open('results/drugs.json') as json_file:
    drugs = json.load(json_file)

# Opening JSON file
with open('results/clinical_trials.json') as json_file:
    clinical_trials = json.load(json_file)

# Opening JSON file
with open('results/pubmed.json') as json_file:
    pudmed = json.load(json_file)


def generate_mention_drug_item(type, drug_id, drug_name, title, journal, date):
    return {
        'type' : type,
        'drug_id' : drug_id,
        'drug_name' : drug_name,
        'title' : title,
        'journal' : journal,
        'date' : date,
    }
    

def generate_graph(input_dic, drugs_dic):
    mention_drug_items = []
    for id, journal in input_dic.items():
        target_item = journal['title']
        for id, drug in drugs_dic.items():
            keyword = drug['drug']
            if keyword.lower() in target_item.lower():
                new_mention_item = generate_mention_drug_item('pubmed', 
                                      drug['atccode'], 
                                      keyword, 
                                      target_item,
                                      journal['journal'],
                                      journal['date']
                                    )
                mention_drug_items.append(new_mention_item)
    
    json_result = json.dumps(mention_drug_items)
    print(mention_drug_items)
    with open('results/output.json', 'w') as f:
        f.write(json_result)
        


generate_graph(pudmed, drugs)


