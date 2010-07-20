#!/usr/bin/python

import sqlite3 as dbapi

con = dbapi.connect('webDB.db')
con.text_factory = str
cur = con.cursor()
f = open("settings.properties","r")
values = f.readlines()
f.close()
if "create" in values[0]:
	cur.execute('CREATE TABLE webpages(URL TEXT, TITLE TEXT, DESCRIPTION TEXT)')
	f = open("settings.properties","w")
	f.writelines("read")
	f.close()

#Aceasta metoda insereaza in baza de date o noua pagina web gasita
def insertpage(url="none", title="none", description="none"):
	#print("S-a inceput introducerea in baza de date")
	query = 'INSERT INTO webpages VALUES(\"'+url+'\",\"'+title+'\",\"'+description+'\")'
	cur.execute(query)
	con.commit()
	#print("S-a facut o inserare in baza de date")

#Aceasta metoda stocheaza toata baza de date ca un sir de caractere pentru a fi afisat la consola sau ca sa fie scris intr-un fisier
def viewall():
	cur.execute('SELECT * FROM webpages')
	data = cur.fetchone()
	result = ""
	while data is not None:
		result += str(data)+"\n"
		data = cur.fetchone()
	return result

#Metoda permite stergerea unei intrari din baza de date
def deletepage(url):
	query = 'DELETE FROM webpages WHERE URL = \"' + url + '\"'
	con.execute(query)
	con.commit()
		