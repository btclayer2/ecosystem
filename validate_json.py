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
                   "Inscription"]

    for key in json_data:
        for item in json_data[key]:
            # Check for all required fields
            if not all(field in item for field in required_fields):
                return False

            # Check if types is a list and each type is valid
            if not isinstance(item["types"], list) or not all(t in valid_types for t in item["types"]):
                return False

            # Check if URLs are valid
            if not is_valid_url(item["icon"]) or not is_valid_url(item["link"]):
                return False

    return True

try:
    with open('dapplist.json', 'r') as file:
        data = json.load(file)
        if validate_json(data):
            print("JSON is valid.")
        else:
            print("JSON is invalid.")
            sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
