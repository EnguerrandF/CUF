# CUF
## Présentation du projet
Ce projet a vu le jour en réponse à une problématique liée à ma profession de photographe/vidéaste. Pour éviter toute perte de données, j'avais besoin de stocker mes fichiers sur deux disques distincts. De plus, lors de l'édition de mes photos et vidéos, il était indispensable pour moi de travailler sur l'un de ces disques. Et aucune des solutions classiques telles que le RAID ou les sauvegardes ne répondait parfaitement à mes besoins.

C'est dans ce contexte que j'ai pris l'initiative de développer ce petit programme en Python. Son objectif est de copier les fichiers du dossier source vers le dossier de destination s'ils ne sont pas déjà présents, tout en supprimant les fichiers du dossier de destination qui ne se trouvent plus dans le dossier source. Ainsi, une copie quasiment identique est maintenue entre les deux dossiers. De plus, le programme est conçu pour mettre à jour les fichiers dont la taille a été modifiée, garantissant une copie plus précise mais pas forcement identique. L'avantage est que cela permet de mettre à jour les fichiers dans le dossier de destination sans forcement tout recopier.


## Déploiement en local du projet
#### 1- Sélectionner la commande Git ci-dessous afin de récupérer le projet:
```
     git clone https://github.com/EnguerrandF/cloneDir.git
```
---
#### 2- Accéder au dossier:
```
    cd nom_du_dossier
```
---
#### 3- Créer l'environnement virtuel en exécutant la commande ci-dessous:
```
    python -m venv env
```
---
#### 4- Activer l'environnement:
* Windows:
```
    env/Scripts/activate
```
* Mac et linux:
```
    source venv/bin/activate
```
---
#### 5- Ajoutez-les modules du fichier requirements.txt en executant la commande si dessous:
```
    pip install -r requirements.txt
```
---
#### 7- Lancer le programme:
```
    python .\run.py  
```
#### 8- Utilisation du programme:
Une fenêtre va s'ouvrir et vous allez pouvoir sélectionner le dossier source et le dossier de destination. Puis lancer la mise à jour des fichiers entre les deux dossiers. Vous pouvez vérifier dans le shell les fichiers copiés et supprimés.

