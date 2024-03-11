import json
import random

json_file_path = r"C:\Users\JackT\CodeLancs\Python\Python projects\Command_Line\Headlines.json"

with open(json_file_path, 'r') as f:
   json_data = json.load(f)

headlines_list = json_data["Headlines"]

samples = random.sample(headlines_list, 5)

for item in samples:
    print(item["name"])