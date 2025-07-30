import json
import csv
import sys
from pathlib import Path

def flatten_json(y, parent_key='', sep='.'):
    items = []
    if isinstance(y, list):
        for i, v in enumerate(y):
            items.extend(flatten_json(v, f'{parent_key}[{i}]', sep=sep).items())
    elif isinstance(y, dict):
        for k, v in y.items():
            new_key = f'{parent_key}{sep}{k}' if parent_key else k
            items.extend(flatten_json(v, new_key, sep=sep).items())
    else:
        items.append((parent_key, y))
    return dict(items)

def convert_semgrep_json_to_flat_csv(json_path, csv_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    results = data.get("results", [])
    print(f"Processing {len(results)} findings...")

    flattened = [flatten_json(result) for result in results]

    # Get all unique keys from all flattened results
    all_keys = sorted({key for item in flattened for key in item})

    with open(csv_path, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=all_keys)
        writer.writeheader()
        for item in flattened:
            writer.writerow(item)

    print(f"✅ CSV created at: {csv_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python semgrep_json_to_csv_flat.py input.json output.csv")
        sys.exit(1)

    input_json = Path(sys.argv[1])
    output_csv = Path(sys.argv[2])

    if not input_json.exists():
        print(f"Input file does not exist: {input_json}")
        sys.exit(1)

    convert_semgrep_json_to_flat_csv(input_json, output_csv)
