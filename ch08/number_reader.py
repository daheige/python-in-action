import json
from pathlib import Path

path = Path("number.json")
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)
