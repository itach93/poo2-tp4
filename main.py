import sqlite3

# Connexion à la base de données
connexion = sqlite3.connect("ma_bd.db")

curseur = connexion.cursor()

# Création d'une table
curseur.execute('''
    CREATE TABLE IF NOT EXISTS utilisateurs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
''')

print("Table utilisateur crée avec succès!")

nom = "Tchassi"
age = 19
email = "test@test.com"
curseur.execute('''
    INSERT INTO utilisateurs (nom, age, email)
    VALUES (?, ?, ?) 
''', (nom, age, email))
print("Données insérées avec succès!")

# curseur.execute('''
#     UPDATE utilisateurs
#     SET email = 'elie@gmail.com'
#     WHERE id = 1
# ''')
# print("Données mises à jour avec succès!")

curseur.execute('SELECT * FROM utilisateurs')
resultats = curseur.fetchall()

# print(resultats)

for ligne in resultats:
    print(ligne)

connexion.commit()

connexion.close()
