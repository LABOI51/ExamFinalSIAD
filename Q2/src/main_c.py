import os
import sqlite3

# TODO Q2c Requete
# DEBUT DU CODE ->
db_path = os.path.normpath("./db_exam")
c = sqlite3.connect(db_path)

sol = c.execute('''SELECT nom FROM CLIENTS WHERE codepostal="abc"''')
rows = sol.fetchall()
for row in rows:
    print(row[0])
# <- FIN DU CODE


