#!/usr/bin/python3

import os

#Fonction qui permet de generer une playlist au format m3u
def writeM3U(argumentsParser, playlist):
    '''
    Fonction qui permet de generer une playlist au format m3u.
    @param argumentsParser:contient les informations principales de la playlist (duree, type et nom de la playlist).
    @param playlist: contient un ensemble de morceaux qui correspond a la demande de l'utilisateur. 
    '''

    #On applique le nom de la playlist pour le nom du fichier de la playlist
    #On creer le fichier et on lui donne les droits d'ecriture
    playlistFileName = argumentsParser.nom_playlist +"."+ argumentsParser.type_playlist
    playlistFile = open(playlistFileName, 'w')
    
    #On parcours l'ensemble de la liste de l'ensemble des morceaux trouves
    for musique in playlist:
            #On ecrit le chemin de la musique trouver
            playlistFile.write(musique[8] + "\n")
    #On ferme le fichier de playlist
    playlistFile.close()

#Fonction qui permet de generer une playlist au format xspf
def writeXSPF(argumentsParser, playlist):

    '''
    Fonction qui permet de generer une playlist au format xspf.
    @param argumentsParser:contient les informations principales de la playlist (duree, type et nom de la playlist).
    @param playlist: contient un ensemble de morceaux qui correspond a la demande de l'utilisateur. 
    '''
    
    #Creation d'un fichier
    playlistFileName = argumentsParser.nom_playlist +"."+ argumentsParser.type_playlist
    playlistFile = open(playlistFileName, 'w')

    playlistFile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"+
                       "<playlist version=\"1\" xmlns=\"http://xspf.org/ns/0/\">\n"+
                       "\t<title>"+ playlistFileName +"</title>\n"+
                       "\t<trackList>\n")
    for musique in playlist:
        playlistFile.write("\t\t<track>\n\t\t\t<location>"+ musique[8] +"</location>\n"+
                           "\t\t\t<title>"+ musique[0] +"</title>\n"+
                           "\t\t\t<creator>"+ musique[2] +"</creator>\n"+
                           "\t\t\t<album>"+ musique[1] +"</album>\n"+
                           "\t\t\t<duration>"+ str(musique[5] * 1000) +"</duration>\n"+
                           "\t\t</track>\n")

    playlistFile.write("\t</trackList>\n</playlist>")
    playlistFile.close()

#Fonction qui permet de generer une playliste au format pls
def writePLS(argumentsParser, playlist):
    '''
    Fonction qui permet de generer une playlist au format pls.
    @param argumentsParser:contient les informations principales de la playlist (duree, type et nom de la playlist).
    @param playlist: contient un ensemble de morceaux qui correspond a la demande de l'utilisateur. 
    '''

    #On initialise un compteur
    i=1
    #Creation d'un fichier
    playlistFileName = argumentsParser.nom_playlist +"."+ argumentsParser.type_playlist
    playlistFile = open(playlistFileName, 'w')
    playlistFile.write("[playlist]\n")

    for musique in playlist:
        playlistFile.write("File"+ str(i) +"="+ musique[4] +"\nTitle" + str(i) +"="+ musique[0] +"\nLength"+ str(i) +"="+ str(musique[5]) +"\n")
        i+=1
        playlistFile.write("NumberOfEntries="+ str(len(playlist)) +"\nVersion=2")

    #On ferme le fichier de la playlist
    playlistFile.close()
