import os
import sqlite3

client_id = [1, 2, 3, 4]
client_name = ['Danny',
               'Frank',
			   'Rusty',
			   'Basher']
client_address = ['a', 'b', 'c', 'd']
client_postal_code = ['abc', 'def', 'abc', 'xyz']

# TODO Q2b Inserer enregistrements
# DEBUT DU CODE ->
#Connexion à la bd
db_path = os.path.normpath("./db_exam")
c = sqlite3.connect(db_path)

for i in range(4):
	c.execute('''INSERT INTO CLIENTS(id_client, nom, adresse, codepostal) VALUES(?, ?, ?, ?)''',
			  (client_id[i], client_name[i], client_address[i], client_postal_code[i]))
	c.commit()
# <- FIN DU CODE


