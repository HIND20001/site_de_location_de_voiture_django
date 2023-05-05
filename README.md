# 1-Application de location de voitures avec Django:
        Cette application web permet aux utilisateurs de rechercher, louer et gérer des réservations de voitures en ligne. Elle a été développée avec Django
        
# 2-Fonctionnalités :
      ## Fonctionnalités  de client :
                    Recherche de voitures disponibles par catégories
                    Réservation de voitures avec un formulaire en ligne facile à utiliser
                    Affichage des réservation   de client connecté
                     Suppression des réservation de client connecté
     ## Fonctionnalités  d admin:
                    la gestion des voitures
                    la gestion des réservations 
                    la gestion des utilisateurs
                    la gestion des catégories
# 3-Installation :
      ##Clonez le dépôt Github :
                    git clone https://github.com/username/location-voitures-django.git
      ## Installez les dépendances :
                     cd location-voitures-django
                     pip install -r requirements.txt
      ## Créez la base de données :
                      python manage.py migrate
      ## Ouvrez l'application dans votre navigateur à l'adresse http://localhost:8000/.



# 4-Utilisation :
       ## Utilisateurs clients :
                      Créez un compte client en cliquant sur le lien "S'inscrire" en haut à droite de la page d'accueil.
                      Connectez-vous avec vos identifiants de connexion.
                      Recherchez une voiture disponible en entrant la categorie
                      Choisissez la voiture que vous souhaitez louer et remplissez le formulaire de réservation.
                      Consultez vos réservations actuelles et passées dans la section "Mes réservations" de votre compte.
       ## Utilisateurs administrateurs :
                       Connectez-vous avec vos identifiants de connexion à la page d'administration de Django, accessible à l'adresse http://localhost:8000/admin/.
                       Gérez les voitures en ajoutant, modifiant ou supprimant des modèles de voitures.
                       Gérez les réservations en visualisant les réservations actuelles et passées, en les modifiant ou en les supprimant.
                       Gérez les utilisateurs en ajoutant, modifiant ou supprimant
#5-Configuration :
              SECRET_KEY: clé secrète utilisée par Django pour les fonctions de sécurité, telle que la gestion des sessions et des cookies. Vous pouvez générer une                           nouvelle clé avec la commande python -c "import secrets; print(secrets.token_hex(24))".
              DEBUG: spécifie si le mode de débogage est activé ou non. Si vous déployez cette application en production, vous devriez désactiver le mode de débogage                        en définissant cette variable sur False.
             DATABASE_URL: URL de la base de données. Vous pouvez utiliser une base de données SQLite pour les tests et le développement, mais vous devriez utiliser                           une base de données plus robuste, telle que PostgreSQL ou MySQL, pour la production.


