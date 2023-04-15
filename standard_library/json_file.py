from pathlib import Path
import json

"""
# Create json object
movies = [
    {"id": 1, "title": "Terminator", "yes": 1984},
    {"id": 2, "title": "Kindergarten Cop", "yes": 1990}
]

data = json.dumps(movies)
# print(data)
# Create json file
Path("movies.json").write_text(data)
"""

# Read json file
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
