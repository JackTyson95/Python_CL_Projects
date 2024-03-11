import json
import random

# specify the path to your json file
json_file_path = r"C:\Users\JackT\CodeLancs\Python\Python projects\Command_Line\Headlines.json"

with open(json_file_path, 'r') as f:
   json_data = json.load(f)

# Now `json_data` contains the data from your JSON file
headlines_list = json_data["Headlines"]

# get 5 random samples
samples = random.sample(headlines_list, 5)

for item in samples:
    # Print the 'name' from each sampled headline
    print(item["name"])