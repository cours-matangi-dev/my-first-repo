[![flask-deployment](https://github.com/cours-matangi-dev/my-first-repo/actions/workflows/blank.yml/badge.svg)](https://github.com/cours-matangi-dev/my-first-repo/actions/workflows/blank.yml)  ![test-coverage badge](./app/coverage-badge.svg)

# appli de sondage nginx et flask

Lancer les container avec docker-compose up

# verification manuelle que l'appli fonctionne 

verifier que le serveur nginx tourne sur :

http://localhost/blabla/ pour les "mauvaises" requetes

et 

http://localhost/blabla/?answeryes=1&answerno=0 pour voter oui
http://localhost/blabla/?answeryes=0&answerno=1 pour voter non

et 

http://localhost/blabla/results.png pour les graphiques de résultats

# verification que traefic fonctionne

Vous pouvez en principe remplacer localhost par sondage.localhost dans les adresses précédentes pour vérifier que traefik fonctionne. 
Traefik et nginx proposent tous les deux des fonctions de reverse proxy et on trouve le plus souvent de la literature sur l'utilisation de l'un ou l'autre mais rarement des deux en même temps.
Cette illustration est purement pédagogique
blabla
