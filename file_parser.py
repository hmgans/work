import argparse
import json
import os

if __name__ == '__main__':

    # Parse arguement given in CLI
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--data_path', type=str, help='dataset', required=True)
    arg_parser.add_argument('--table_path', type=str, help='table dataset', required=False) # Changed from True to False
    arg_parser.add_argument('--ner_path', type=str, help='file containing the values extracted by NER (e.g. ner_train.json)', required=False) # Changed from True to False
    args = arg_parser.parse_args()

    with open(args.data_path, 'r', encoding='utf8') as f:
        datas = json.load(f)

    ground_truth_values = []

    # Extract 'ground truth values' from each spider json
    for data in datas:
        
        for i in range(0, len(data['sql']['where']), 2):
            ground_truth_values.append(data['sql']['where'][i][3])

        final_values = []
        for value in ground_truth_values:
            value = str(value).replace('"','') # Clean strings
            final_values.append(str(value))

        # Append ground truth values to the json 
        data['values'] = final_values

    # Modify the file to include ground truth values 
    with open(args.data_path, 'w', encoding='utf8') as f:
        json.dump(datas, f)


