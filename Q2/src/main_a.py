import os
import sqlite3

# TODO Q2a Creer la BD
# DEBUT DU CODE ->
#Ouverture db vide
db_path = os.path.normpath("./db_exam")
c = sqlite3.connect(db_path)

#Créer la table
c.execute('''CREATE TABLE CLIENTS
            (id_client INTEGER,
             nom TEXT,
             adresse TEXT,
             codepostal TEXT,
             PRIMARY KEY (id_client))''')

c.execute('''CREATE TABLE COMMANDES
            (id_comm INTEGER,
             id_client INTEGER,
             date TEXT,
             PRIMARY KEY (id_comm),
             FOREIGN KEY (id_client) REFERENCES CLIENTS(id_client))''')

c.execute('''CREATE TABLE PRODUITS
            (id_prod INTEGER,
             cout NUMERIC,
             PRIMARY KEY (id_prod))''')

c.execute('''CREATE TABLE LIGNES
            (id_comm INTEGER,
             quantite INTEGER,
             id_prod TEXT,
             PRIMARY KEY (id_comm, id_prod),
             FOREIGN KEY (id_comm) REFERENCES COMMANDES(id_comm),
             FOREIGN KEY (id_prod) REFERENCES PRODUITS(id_prod))''')
# <- FIN DU CODE

