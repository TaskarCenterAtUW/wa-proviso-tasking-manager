import json
file_path = 'frontend/patch/imagery.min.json'
with open(file_path, 'r') as f:
    data = json.load(f)

# Dump the minified JSON into the same file
with open(file_path, 'w') as f:
    json.dump(data, f, separators=(',', ':'))