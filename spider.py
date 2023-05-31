# This file converts json's of the given format into a spider file
#
# Author: Henry Gansert
# Date: 5-31-2023
# 
import json

#Given input
inputJson_example = '[ { "db_id": "db1", "table_name": "head", "column_name": ["age","name","born_state"], "column_type": ["number","string","string"] }, { "db_id": "db1", "table_name": "department", "column_name": ["age","name","born_state"], "column_type": ["number","string","string"] } ]'

json_array = json.loads(inputJson_example)

spider_array = []

# Create a spider object for each json input
for jsn in json_array:
    spider_object = {
            'db_id': jsn['db_id'],
            'query': 'SELECT ' + ', '.join(jsn['column_name']) + ' FROM ' + jsn['table_name'],
            'question': 'Retrieve ' + ', '.join(jsn['column_name'][:-1]) + ' and ' + jsn['column_name'][-1] + ' contact information from the ' + jsn['table_name'] + ' table'
        }
    spider_array.append(spider_object)

print(spider_array)

spider_json_array = json.dumps(spider_array)


# Write spider jsons to a text file 
with open('output.txt', 'w') as file:
    json.dump(spider_json_array, file)

print("Spider array has been written to the file.")
