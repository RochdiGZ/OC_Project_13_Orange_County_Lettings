## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

Le site web en production est accessible [ici](https://lettings-174e900c72bd.herokuapp.com/)

### Fonctionnement

- Le déploiement est déclenché à chaque mise à jour de la branche `main` sur [GitHub](https://github.com)
`Le site web est déployé à condition que :`
- le [linting](https://flake8.pycqa.org/en/latest/)
- les [tests](https://docs.pytest.org)
- la construction de l'image [Docker](https://docs.docker.com/) réussissent
`La mise en oeuvre du pipeline CI/CD repose sur la plateforme :`
- [GitHub Actions](https://docs.github.com/fr/actions)
`Le site web de production est hébergé sur la plateforme :`
- [Heroku](https://devcenter.heroku.com/) permettant d'exécuter une image Docker déjà construite 

`Remarque : A chaque déploiement, une nouvelle image Docker est générée et sauvegardée sur la plateforme :`
- [Docker Hub](https://hub.docker.com/) pour tag le `hash` du `commit` de Git correspondant

### Configuration requise

- Le code de l'application doit être hébergé sur un dépôt GitHub sur lequel vous avez tous les droits
- L'accès à un compte [Docker Hub](https://hub.docker.com) pour le dépôt des images Docker
- L'accès à un compte [Heroku](https://id.heroku.com) pour la mise en production du site web
- L'accès à un compte [Sentry](https://sentry.io/signup/) pour la surveillance de l'application

### Etapes à suivre

`Préambule : ` Pour créer les secrets et les variables nécessaires à l'exécution du pipeline CI/CD sur GutHub Actions : 
- Accéder à `settings` de l'onglet Actions GitHub, menu `Security / Secrets and variables / Actions`
- Accéder à l'onglet `Secrets`
- Cliquer sur le bouton `New repository secret`
- Taper le nom `DOCKERHUB_TOKEN`
- Ajouter la valeur du jeton d'accès à Docker Hub et valider
- Ajouter chacune des repository variables en accédant à l'onglet `Variables`
- Cliquer sur le bouton `New repository variable`
- Taper le nom 
- Ajouter la valeur de chaque variable et valider

`Depuis le compte DockerHub : `
  - Créer un `repository` dont le nom doit être enregistré sur GitHub dans la variable nommée `DOCKERHUB_REPO`
  - Générer un `Access token` (menu `Account Settings / Security`) à enregistrer immédiatement dans un fichier texte.
    `Access token` correspond à la valeur du secret `DOCKERHUB_TOKEN` à créer depuis GitHub Actions
    `DOCKERHUB_USERNAME` correspond à votre nom d'utilisateur sur DockerHub 
`Depuis le compte Heroku : `
  - Créer une nouvelle application dont le nom doit être enregistrée dans la variable GitHub nommée `HEROKU_APP_NAME`. 
    Ce nom sera le préfixe de l'URL du site web en production
`Dans le fichier settings.py de l'application : `
  - Ajouter `secret key` en créant une `Config var` nommée `SECRET_KEY` ayant pour valeur le résultat de la commande :
    `python -c "import secrets; print(secrets.token_urlsafe(64))"`
Vous pouvez regénérer `API KEY` (menu `Account settings` onglet `Account`) comme valeur de la variable `HEROKU_API_KEY`
- Sur GitHub, créer la variable `HEROKU_EMAIL` ayant pour valeur l'adresse email utilisée pour se connecter à Heroku
- Après ces étapes de paramétrage, le pipeline CI/CD avec mise en production automatique du site web s'exécutera à chaque nouvelle mise à jour de la branche `main`. Le déroulement et le résultat de l'exécution du `workflow` correspondant est accessible via l'onglet `Actions` du dépôt GitHUb de l'application

- Le site web en production est alors accessible à l'adresse `https://lettings-174e900c72bd.herokuapp.com`

### Surveillance et suivi des erreurs avec [Sentry](https://docs.sentry.io/platforms/python/)

`Depuis le compte Sentry : `
  - Créer un projet en sélectionnant comme plateforme `DJANGO`
  - Copier la valeur du champ `DSN` accessible dans la rubrique `SDK SETUP / Client Keys (DSN)` des paramètres du projet nouvellement créé
- Sur Heroku, Créer une `Config var` nommée `SENTRY_DSN` en lui affectant la valeur du `DSN` ci-dessus

- Tester le bon fonctionnement de la surveillance :
  - Accéder à l'URL `https://lettings-174e900c72bd.herokuapp.com/sentry-debug` qui génère une exception dans l'app.
  - Visualiser l'exception levée dans la section `Issues` du compte Sentry
