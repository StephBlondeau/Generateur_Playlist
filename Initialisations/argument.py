import argparse
'''
Created on 8 oct. 2014

Liste des arguments obligatoires ou optionnels sur la ligne de commande du programme afin de pouvoir generer une playliste selon 3 format
@author: kitsune, FX
'''

#Arguments positionnels, obligatoires pour generer une playliste
parser = argparse.ArgumentParser()

#Duree_playlist est la duree de la playlist en minutes
parser.add_argument("duree_playlist", help="Duree de la playlist en minutes", type=int)

#Type_playlsit est le format de sortie de la playlist
parser.add_argument("type_playlist", help="Format de sortie de la playlist", choices=["m3u","xspf","pls"])

#Nom_playlist est le nom de la playlist
parser.add_argument("nom_playlist", help="Nom du fichier de la playlist")


#Arguments optionnels pour generation d'une playlist
#--g permettera de specifie un genre de musique 
parser.add_argument("--g", action='append', help="genre de musique voulue '", nargs=2)

#--ar permettre de specifie un artiste voulue
parser.add_argument("--ar", action='append', help="artiste voulu ", nargs=2)

#--alb permettera de specifie un album voulue
parser.add_argument("--alb",action='append', help="album voulue", nargs=2)

#--t permettera de specifie un titre voulue
parser.add_argument("--t", action='append', help="titre voulue", nargs=2)

#--sg permettera de specifie un sous genre
parser.add_argument("--sg", action='append', help="sous genre possible", nargs=2)

#--r permettera de rentre une recherche
#parser.add_argument("--r", help="recherche selon une expression")

argumentsParser = parser.parse_args()