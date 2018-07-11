from crate import client
from crate.client.cursor import Cursor

connection = client.connect("http://localhost:4200", username="crate")

cursor = connection.cursor()  # type: Cursor

try:
    cursor.execute("CREATE TABLE IF NOT EXISTS strings (str STRING, num INTEGER)")
except:
    print("could not create table")

cursor.execute("INSERT INTO strings (str, num) VALUES (?, ?)", ("Hello world!", 42))

cursor.execute("INSERT INTO strings (str, num) VALUES (?, ?)", ("hi there", 99))

cursor.execute("REFRESH TABLE strings")

cursor.execute("SELECT str FROM strings")

try:
    print(cursor.fetchall())
except:
    print("no results there :(")

cursor.execute("SELECT str FROM strings WHERE num > 50")

try:
    print(cursor.fetchall())
except:
    print("no results there :(")

cursor.execute("UPDATE strings SET str = ?, num = ? WHERE num > 50", ("some different string", 102))

cursor.execute("REFRESH TABLE strings")

cursor.execute("SELECT str FROM strings WHERE str LIKE ?", ["some different string"])

try:
    print(cursor.fetchall())
except:
    print("no results there :(")

cursor.execute("DROP TABLE strings")