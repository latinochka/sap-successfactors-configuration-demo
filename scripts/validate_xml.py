from pathlib import Path
import sys
import xml.etree.ElementTree as ET

EXPECTED_ROOTS = {
    "candidate-profile-template-demo.xml": "candidate-profile-data-model",
    "succession-data-model-demo.xml": "succession-data-model",
}


def collect_ids(root):
    values = []
    for element in root.iter():
        value = element.attrib.get("id")
        if value:
            values.append(value)
    return values


def main():
    base = Path(__file__).resolve().parents[1]
    failed = False

    for filename, expected_root in EXPECTED_ROOTS.items():
        path = base / "xml" / filename
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError as exc:
            print(f"FAIL {filename}: {exc}")
            failed = True
            continue

        if root.tag != expected_root:
            print(f"FAIL {filename}: expected root {expected_root}, got {root.tag}")
            failed = True
            continue

        ids = collect_ids(root)
        duplicates = sorted({value for value in ids if ids.count(value) > 1})
        if duplicates:
            print(f"FAIL {filename}: duplicate ids {duplicates}")
            failed = True
            continue

        print(f"OK   {filename}: {len(ids)} unique ids")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
