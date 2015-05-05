Documentation Technique
=======================

###Sommaire

* Contexte de l'application
* Environnement du projet
* Arguments de la ligne de commande
* Modules python
* Régles de gestion

### Contexte de l'application

> La section BTS SIO du Lycée André Malraux gère, maintient et anime la Radio Libre de
l’établissement. La nature des morceaux qui sont écoutés par les auditeurs provient du travail du programmateur radio dont la responsabilité est de concevoir l’enchaînement musical diffusé.

> Pour cela, le programmateur radio doit créer des playlist en plusieurs formats. Nous avons
donc créé un outil de génération de playlist musicale pour lui faciliter le travail. L’insertion des morceaux est donc rendu plus rapide dans la playlist puisqu’ils étaient à l’origine ajoutés à la main. 

### Environnement de developpement
>
####Système d'exploitation : 
> GNU/Linux 
####Langage : 
> Python et interprété avec Python3
####Méthode de conception :
> Programmation Orientée Objet.
####Langage de requêtage : 
> SQL.
####SGBD/Stockage des données :
> PostgreSql
####Bibliothèques : 
> lxml pour la sortie en XSPF, sqlAlchemy pour l’accès au stockage de données avec PgSql, argparse  pour la gestion des arguments de la ligne de commande,
####Documentation technique : 
> 
* Intégrée en PyDoc pour Python et rédigé sur un document PDF.
* une page de manuel rédigée en Markdown et convertie en manpage à l’aide de readTheDocs , contenant alors la documentation détaillée de l’utilisation du programme,
####Documentation utilisateur :
> 
* l’affichage d’une documentation succinte rappelant les différentes options disponibles pour le programme, appelée à l’aide de l’option --help en paramètre de la ligne de commande,
* une page de manuel rédigée en Markdown et convertie en manpage à l’aide de readTheDocs , contenant alors la documentation détaillée de l’utilisation du programme,
* une version HTML de la documentation issue de la page de manuel ,
* une version PDF de la documentation issue de la page de manuel .

### Arguments de la ligne de Commande
>
#### Obligatoires :
| Nom           |  Utilité    | Exemple   |
| ------------- |-------------| ----------|
| durre_playlist| Indique la durée en minutes voulu pourla playlist | 120|
| type_playlist | Indique le type de sortie de la playlist |m3u, xspf ou pls|
| nom_playlist  | Le nom du fichier de sortie créé |nom_playlist|

#### Optionnels :
Chacun de ses arguments attends 2 parametres 

| Raccourcie    |  Nom   | Utilité | Exemple   |
| ------------- |--------|---------| ----------|
| __--help__ | Help | Affichage d'un message d'aide||
| __--g__    | Genre | Indique le genre de musique voulue | --g Rock 120 |
| __--ar__    | Artiste | Indique le nom d'un artiste | --ar Indochine 25 |
| __--alb__  | Album | Indique le titre d'un album | --alb Matin 25 |
| __--t__    | Titre | Indique le titre d'un morceau | --t Debut 124 |
| __--sg__   | Sous-genre | Indique le sous-genre de musique voulue | --sg Rap 76 |

>*Les arguments sont donc composés d'une chaîne et ensuite d'une quantité (en pourcentage).*

###Règles de gestion des arguments de la ligne de commande
>
#### Pour les arguments optionnels :
> 
* Si on ne saisie aucun paramètre optionnel
>> Ex: --g --ar --t etc ... La playlist sera généré avec des morceaux de musique de tout les genres, sélectionnés aléatoirement.
* Si on saisie un paramètre optionnel mais sanq la quantité ou le nom de l'argument voulue
>> Ex: --g Rock --g 34 La playlist ne sera pas généré et un message d'erreur sera affiché à l'utilisateur.
* Si on saisie un paramètre optionnel avec un quantité et un argument qui n'existe pas dans la base
>> Ex: --g Rack 34 La playlist ne sera pas généré et un message d'erreur sera affiché à l'utilisateur.

#### Pour la durée de la playlist :

> 
* Si la durée de la playlist est supérieur à l'ensemble des quantités des arguments optionnels
>> Ex: Durée Playlist = 450 et --g Rock 80 --g Rap 80 (=160) On remet le tout en base 100 en gardant la proportion des arguments voulus.
* Si la durée de la playlist est inférieur à l'ensemble des quantités des arguments optionnels
>> Ex: Durée Playlist = 100 et --g Roc  20 --g Rap 10 (=30) On remet le tout en base 100 en gardant la proportion des arguments voulus.
* Si la durée de la playlist est de 0
>> Ex : Durée Playlist = 0 alors le programme envoie un message d'erreur

#### La saisie du pourcentage d'argument

>
* Si on saisie un nombre décimal
>> L'application va le convertir en entier
* Si on saisie un nombre négatif
>> L'application va le convertir en entier naturel 
* Si on saisie 0 pour un argument
>> L'application envoie un message d'erreur

### Etapes du programmes


