from bs4 import BeautifulSoup
import json
import os

# Directory containing HTML files
html_dir = 'WE ASSIGNMENT\we-assignment'

output_file = 'output.json'
all_data = {}

for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
        with open(os.path.join(html_dir, filename), 'r') as file:
            html_content = file.read()

        # Parse the HTML using Beautiful Soup
        soup = BeautifulSoup(html_content, 'html.parser')
        data = {}

        #execpt images
        for element in soup.find_all():
            if element.name == 'img':
                continue  # Skip images

        
            data[element.name] = element.get_text()

      
        all_data[filename] = data

# to json format
json_data = json.dumps(all_data, indent=4)

# Save the JSON data 
with open(output_file, 'w') as file:
    file.write(json_data)
