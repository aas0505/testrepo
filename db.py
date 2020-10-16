
import mysql.connector
import pymysql
import sqlite3

con= mysql.connector.connect(
host="localhost",
user="root",
password="",
port=3306,
db='tiers'
)
mycursor= con.cursor()
print("connected")
carte_entry=input("entrez numéro de carte: ")
mycursor.execute("SELECT carte from client")
cartes=mycursor.fetchall()
    # verification de numero de carte

liste_cartes=[]
for i in cartes:
    for k in i:
        liste_cartes.append(k)
print(liste_cartes)
j=0

class Client:
        def __init__(self, nom, num_carte, num_code, solde):
            self.nom=nom
            self.num_carte=num_carte
            self.num_code=num_code
            self.solde=solde


liste_tiers=[]
for i in range(len(liste_cartes)):
    if liste_cartes[i]==int(carte_entry):
        j+=1
        
        mycursor.execute("SELECT nom,carte,pin,solde FROM client WHERE carte=%s;",(int(carte_entry),))
        tiers=mycursor.fetchone()
        
        for i in tiers:
            liste_tiers.append(i)
        print(liste_tiers)
       
        client_systeme=Client(liste_tiers[0], liste_tiers[1], liste_tiers[2], liste_tiers[3])

if j==0:
    print("carte inexistante")

con.commit()
con.close()