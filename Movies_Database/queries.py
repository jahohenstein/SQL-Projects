from calendar import c
import sqlite3

conn = sqlite3.connect("movies.sqlite")

db = conn.cursor()

def number_of_directors():
    # return the number of directors contained in the database
    query = """
    SELECT
    """


if __name__ == "__main__":
    number_of_directors()
