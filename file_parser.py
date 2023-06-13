import argparse
import json
import os

# from preprocessing.sql2SemQL import Parser
# from preprocessing.utils import load_dataSets


def validate_values_contained_in_ner(ner_entities, values_ground_truth):
    for value_gt in values_ground_truth:
        if not any(ner_entity['name'].lower() == value_gt.lower() for ner_entity in ner_entities):
            print(f'NER could not find value {value_gt} we were looking for. We might be able to find it later based on heuristics (see pre_processing.py).')


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--data_path', type=str, help='dataset', required=True)
    arg_parser.add_argument('--table_path', type=str, help='table dataset', required=False) # Changed from True to False
    arg_parser.add_argument('--ner_path', type=str, help='file containing the values extracted by NER (e.g. ner_train.json)', required=False) # Changed from True to False
    args = arg_parser.parse_args()

    with open(args.data_path, 'r', encoding='utf8') as f:
        datas = json.load(f)

    ground_truth_values = []

    # Planning to extract 'ground truth values'
    for data in datas:
        
        ground_truth_values.append(data['sql']['where'][2])
        # for values in data['sql']['where']:
        #     print(values)
            #ground_truth_values.append(values[3])
 

print(ground_truth_values)