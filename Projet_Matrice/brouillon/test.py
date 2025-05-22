import os
import pandas as pd

# 🔁 Modifier ce chemin selon ton cas : absolu ou relatif
dossier = "./excels"  # Exemple de chemin relatif

# Vérifie que le dossier existe
if not os.path.exists(dossier):
    print(f"❌ Le dossier '{dossier}' n'existe pas.")
else:
    fichiers_excel = [f for f in os.listdir(dossier) if f.endswith((".xlsx", ".xls"))]

    if not fichiers_excel:
        print("⚠️ Aucun fichier Excel trouvé dans le dossier.")
    else:
        print("📁 Fichiers Excel trouvés :")
        for fichier in fichiers_excel:
            print(f" - {fichier}")

        print("\n🔍 Aperçu de chaque fichier :")
        for fichier in fichiers_excel:
            chemin_fichier = os.path.join(dossier, fichier)
            try:
                df = pd.read_excel(chemin_fichier)
                print(f"\n===== {fichier} =====")
                print(df.head())
            except Exception as e:
                print(f"❌ Erreur avec le fichier '{fichier}' : {e}")
