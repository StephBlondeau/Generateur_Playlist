#!/usr/bin/python3
from controles.verificationsArguments import Veriff
from controles.recuperationDonnees import recuperationDonnees
from Initialisations.argument import argumentsParser
import controles.playlistFormat
from controles.playlistFormat import writeM3U, writeXSPF
import random


Attributs=['g','ar','sg','alb','t']
#Liste des arguments du programme


recupArg = Veriff(Attributs)
#On execute la requete qui va lancer le controle des saisies (argument et entier) de l'utilisateur


playlist = recuperationDonnees(argumentsParser,recupArg)
#On recupere la playlist des morceaux trier selon les arguments demander par l'utilisateur

random.shuffle(playlist)
#On mélange la playlist

if (argumentsParser.type_playlist =='m3u'):
    writeM3U(argumentsParser, playlist)
    print('La playlist a bien ete genere')

if(argumentsParser.type_playlist=='xspf'):
    writeXSPF(argumentsParser, playlist)
    print('La playlist a bien ete genere')

if(argumentsParser.type_playlist=='pls'):
    writeXSPF(argumentsParser, playlist)
    print('La playlist a bien ete genere')
