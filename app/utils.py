import re

def normalize_marks(marks):
    if isinstance(marks, int):
        return marks

    if isinstance(marks, str):
        marks = marks.strip()

        # Case: "68/100"
        if "/" in marks:
            try:
                parts = marks.split("/")
                return (float(parts[0]) / float(parts[1])) * 100
            except:
                pass

        # Case: "+52 -12"
        if "+" in marks and "-" in marks:
            try:
                plus = int(re.search(r"\+(\d+)", marks).group(1))
                minus = int(re.search(r"-(\d+)", marks).group(1))
                return plus - minus
            except:
                pass

        # Case: "34/75 (45.3%)"
        if "%" in marks:
            try:
                percent = re.search(r"\((.*?)%\)", marks).group(1)
                return float(percent)
            except:
                pass

        # Case: "28"
        if marks.isdigit():
            return float(marks)

    return 0

import json

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)