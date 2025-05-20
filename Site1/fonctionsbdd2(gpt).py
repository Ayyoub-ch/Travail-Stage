import mysql.connector

class Connexion:
    def __init__(self, host='localhost', user='root', password='', database='log'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connecter(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            print("✅ Connexion réussie.")
        except mysql.connector.Error as err:
            print("❌ Erreur de connexion :", err)

    def deconnecter(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("🔌 Déconnexion effectuée.")

    def afficher_utilisateurs(self):
        try:
            self.cursor.execute("SELECT * FROM utilisateurs")
            resultats = self.cursor.fetchall()
            for ligne in resultats:
                print(ligne)
        except mysql.connector.Error as err:
            print("❌ Erreur lors de la lecture :", err)

    def inserer_utilisateur(self, username, password):
        try:
            self.cursor.execute(
                "INSERT INTO utilisateurs (username, password) VALUES (%s, %s)",
                (username, password)
            )
            self.conn.commit()
            print(f"✅ Utilisateur '{username}' inséré.")
        except mysql.connector.Error as err:
            print("❌ Erreur lors de l'insertion :", err)

# --- Utilisation ---
if __name__ == "__main__":
    db = Connexion()
    db.connecter()
    db.afficher_utilisateurs()
    db.inserer_utilisateur("nouvel_user", "motdepasse123")
    db.deconnecter()
