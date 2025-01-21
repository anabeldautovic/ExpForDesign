import json
import glob

# Directory containing your JSON files
json_folder = "."
output_file = "linked_entities.json"

merged_data = {}

# Iterate through all JSON files in the folder in sorted order
for file_name in sorted(glob.glob(f"{json_folder}/linked_entities_*.json")):
    with open(file_name, "r") as f:
        data = json.load(f)
        # Add all key-value pairs from the file to the merged_data dictionary
        for key, value in data.items():
            key_as_int = int(key)  # Convert key to an integer for proper merging
            merged_data[key_as_int] = value  # Add or overwrite the key-value pair

# Sort the merged data by keys (numerical order) before saving
merged_data = {str(k): v for k, v in sorted(merged_data.items())}

# Save the merged data into a single JSON file
with open(output_file, "w") as f:
    json.dump(merged_data, f, indent=4)

print(f"Merged {len(glob.glob(f'{json_folder}/linked_entities_*.json'))} files into {output_file}")