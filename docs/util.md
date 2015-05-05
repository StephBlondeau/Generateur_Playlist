Documentation Utilisateur
=========================

###Sommaire

* Présentation de l'application
* Arguments de la ligne de commande
* Playlist final
* Erreurs possibles

###Présentation
> L'application permet de généré une playlist selon les choix musicaux voulus. Elle fonctionne à partir d'un terminal.

![GitHub Logo](https://raw.githubusercontent.com/StephBlondeau/Generateur_Playlist/documentation/docs/docs/img/playlist_1.png)


###Saisie Argument(s)
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

###Fichier de sortie
> La playlist sortira en format demandé dans la ligne de commande et se trouvera dans le dossier de l'application.

###Attention

> 
* La durée de la playlist doit être supérieur à 0.
* Le pourcentage d'attribut voulus doit être supérieur à 0.
* La demande d'un attributs doit exister dans le programme (voir avec --help)
* La valeur associé à un attribut doit exister dans la base de données.
* Si le nom de la playlist à déja etait saisie, l'application peut en recréer une du même nom mais qui va écraser la précèdente.

*Il s'agit d'un projet PPE passé sur une base de données de musique avec des chemins fictif. On ne peut donc pas lancer la playlist avec un lecteur media.*
