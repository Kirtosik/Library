import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("+")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


######################################################

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("+")
    except Error as e:
        print(f"The error '{e}' occurred")


#######################################################
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


######################################################
create_users_table = """
CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VAR NOT NULL,
  groupp VAR ,
  orderID INTEGER,
  points INTEGER,
);
"""

create_users = """
INSERT INTO
  students (name, groupp, orderID, points)
VALUES
  ('Dima', 'FP-2', 2, 100),
  ('Lena', 'FP-2', 1, 20),
  ('Victoria', 'FP-2', 3, 110),
  ('Misha', 'FP-2', 4, 10),
  ('Elizabeth', 'FP-2', 5, 70);
"""

connection = create_connection("C:\\sqlite\\sm_app.sqlite")
execute_query(connection, create_users_table)
execute_query(connection, create_users)

select_users = "SELECT name, points from students"
students = execute_read_query(connection, select_users)

for student in students:
    if student[1] <= 30:
        print(student)
