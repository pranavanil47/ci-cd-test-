import json
import csv
import sys
from pathlib import Path

def extract_value(meta, keys):
    """Safely navigate nested dictionaries and lists."""
    val = meta
    for key in keys:
        if isinstance(val, dict):
            val = val.get(key, "")
        elif isinstance(val, list):
            idx = int(key.split("__")[-1]) - 1
            val = val[idx] if idx < len(val) else ""
        else:
            return ""
    return val

def convert_semgrep_json_to_csv(json_path, csv_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    results = data.get("results", [])
    print(f"Processing {len(results)} findings...")

    with open(csv_path, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "File Path",
            "Severity",
            "Start Line",
            "End Line",
            "Message",
            "Fix Recommendation",
            "Likelihood",
            "Impact",
            "Confidence",
            "Category",
            "CWE(s)",
            "OWASP (1st)",
            "OWASP (2nd)",
            "Reference (1st)",
            "Subcategory",
            "Technology (1st)"
        ])

        for r in results:
            extra = r.get("extra", {})
            metadata = extra.get("metadata", {})

            writer.writerow([
                r.get("path", ""),
                extra.get("severity", ""),
                r.get("start", {}).get("line", ""),
                r.get("end", {}).get("line", ""),
                extra.get("message", ""),
                extra.get("fix", ""),
                metadata.get("likelihood", ""),
                metadata.get("impact", ""),
                metadata.get("confidence", ""),
                metadata.get("category", ""),
                "; ".join(metadata.get("cwe", [])),
                metadata.get("owasp", ["", ""])[0] if isinstance(metadata.get("owasp"), list) else "",
                metadata.get("owasp", ["", ""])[1] if isinstance(metadata.get("owasp"), list) and len(metadata["owasp"]) > 1 else "",
                metadata.get("references", [""])[0] if isinstance(metadata.get("references"), list) else "",
                metadata.get("subcategory", [""])[0] if isinstance(metadata.get("subcategory"), list) else "",
                metadata.get("technology", [""])[0] if isinstance(metadata.get("technology"), list) else ""
            ])

    print(f"✅ CSV successfully created at: {csv_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python semgrep_json_to_readable_csv.py input.json output.csv")
        sys.exit(1)

    input_json = Path(sys.argv[1])
    output_csv = Path(sys.argv[2])

    if not input_json.exists():
        print(f"Input file does not exist: {input_json}")
        sys.exit(1)

    convert_semgrep_json_to_csv(input_json, output_csv)
