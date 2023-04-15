from pathlib import Path
import json
import sqlite3

# Data to write in the db
# movies = json.loads(Path("movies.json").read_text())
# print(movies)

# Create a data base and write data
"""
with sqlite3.connect("db.sqlite3") as connection:
    command = "INSERT INTO Movies VALUES(?,?,?)"
    for movie in movies:
        connection.execute(command, tuple(movie.values()))
    connection.commit() # Only need when write data into db
"""

# Read data from db
with sqlite3.connect("db.sqlite3") as connection:
    command = "SELECT * FROM Movies"
    cursor = connection.execute(command)
    # for row in cursor:
    #    print(row)
    movies_rows = cursor.fetchall()
    print(movies_rows)
