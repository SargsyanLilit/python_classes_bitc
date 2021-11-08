import json
import sqlite3
from sqlite3 import Error
import os
import sys


database = os.path.join(os.getcwd(), "film_data.db")

try:
    conn = sqlite3.connect(database)
except Error as e:
    print(e)
    sys.exit()


def query_execute(query):
    curs = conn.cursor()
    with conn:
        curs.execute(query)
    return curs.fetchall()


# movies that starts with B

movies_with_b_query = """SELECT * FROM film_data
                         WHERE title LIKE "B%";"""
print(query_execute(movies_with_b_query))


# movie with the largest duration

largest_duration_query = """SELECT * FROM film_data
                            ORDER BY length DESC
                            LIMIT 1;"""
print(query_execute(largest_duration_query))

# from table into a json file

select_all_query = """SELECT * FROM film_data;"""
result = query_execute(select_all_query)

with open("films_json.json", "w") as json_file:
    json.dump(result, json_file, indent=4)


# extra

create_filtered_table_query = """CREATE TABLE "filtered_films" (
                                 "film_id" INTEGER,
                                 "title" TEXT,
                                 "description" TEXT,
                                 "release_year" INTEGER,
                                 "length" INTEGER,
                                 "rate" TEXT,
                                 "special_features" TEXT );"""

query_execute(create_filtered_table_query)


filtered_movies_query = """SELECT * FROM film_data
                           WHERE release_year > 2005 AND rate IN ('G','R','PG') ;"""

result = query_execute(filtered_movies_query)

string_for_query = ""

for i in result:
    string_for_query += str(i) + ", "
string_for_query = string_for_query[:-2]

insert_query = f"""INSERT INTO filtered_films (film_id,title, description, release_year, length, rate, special_features)
                   VALUES {string_for_query};"""

query_execute(insert_query)
