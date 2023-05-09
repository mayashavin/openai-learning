import csv
import json
from types import SimpleNamespace

# Replace 'input_file.csv' with your actual CSV file path
csv_file_path = '../storefrontui-demo/listing.csv'
csv_array = []

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        csv_array.append(row)

# Get a sub-array of the first 3 elements (rows)
sub_array = csv_array[:3]

# Stringify the sub-array
sub_array_string = '\n'.join([','.join(row) for row in sub_array])

from chatGPT import get_completion

prompt = f"""
Your task is to generate a short summary of each product based on the technical specifications and stock status in the CSV file below. \ 
Each row in the text below represents a product. \ 
You need to put the data into a JSON list with the following properties: title with a most 15 words focusing only on the main product's details, summary of at most 100 words focusing on any technical aspects that are relevant to the product's details, stock_status, price, tags, images, variants, materials. \ 

Text:
```{sub_array_string}```
"""

response = get_completion(prompt)
print(response)

data = json.loads(response)

json_file_path="listing.json"
with open(json_file_path, 'w') as file:
    json.dump(data, file)
