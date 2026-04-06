import json
from src.extractor import extract_all

# load file
with open("data/prescription_raw_text_only.json", "r") as f:
    data = json.load(f)

output = []

for item in data:
    raw = item.get("raw_text")

    if not raw:
        continue

    extracted = extract_all(raw)
    output.append(extracted)

# save output
with open("output.json", "w") as f:
    json.dump(output, f, indent=2)

print("Done")
