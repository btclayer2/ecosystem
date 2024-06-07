import json
import sys
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def validate_json(json_data):
    required_fields = ["name", "types", "icon", "description", "link"]
    valid_types = ["Bridge", "Dev Tools", "Infra", "Game", "NFT", "Wallet", 
                   "Social", "Identity", "Defi", "Data Service", "CEX", 
                   "Security", "Funding", "Launchpad", "Entertainment", 
                   "Inscription", "DEX"]

    for section in json_data.values():
        for item in section:
            # Check for all required fields
            if not all(field in item for field in required_fields):
                print(f"Missing one of the required fields in item: {item}")
                return False

            # Check if types is a list and each type is valid
            if not isinstance(item["types"], list) or not all(t in valid_types for t in item["types"]):
                print(f"Invalid type in item: {item}")
                return False

            # Check if URLs are valid
            if not is_valid_url(item["icon"]) or not is_valid_url(item["link"]):
                print(f"Invalid URL in item: {item}")
                return False

    return True

def sort_data(json_data):
    for key in json_data.keys():
        json_data[key] = sorted(json_data[key], key=lambda x: x['name'].lower())

try:
    with open('dapplist.json', 'r') as file:
        data = json.load(file)
        if validate_json(data):
            print("JSON is valid.")
            sort_data(data)  # Sorting the data after validation
            print("Data sorted by name (case-insensitive).")
            # Optionally print the sorted data
            print(json.dumps(data, indent=4, ensure_ascii=False))
        else:
            sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
