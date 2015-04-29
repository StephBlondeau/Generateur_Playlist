#!/usr/bin/python3
import controles.playlistFormat
import random
from controles.verificationsArguments import Veriff
from controles.verificationsArguments import verifArgument
from controles.recuperationDonnees import recuperationDonnees
from Initialisations.argument import argumentsParser
from controles.playlistFormat import writeM3U, writeXSPF, writePLS

Attributs=['g','ar','sg','alb','t']
#Liste des arguments du programme

#on va recupere la liste des arguments correcte
ListeArg = verifArgument()

recupArg = Veriff(Attributs)
#On execute la requete qui va lancer le controle des saisies (argument et entier) de l'utilisateur


playlist = recuperationDonnees(argumentsParser,recupArg)
#On recupere la playlist des morceaux trier selon les arguments demander par l'utilisateur

random.shuffle(playlist)
#On melange la playlist

if (argumentsParser.type_playlist =='m3u'):
    writeM3U(argumentsParser, playlist)
    print('La playlist a bien ete genere')

if(argumentsParser.type_playlist=='xspf'):
    writeXSPF(argumentsParser, playlist)
    print('La playlist a bien ete genere')

if(argumentsParser.type_playlist=='pls'):
    writePLS(argumentsParser, playlist)
    print('La playlist a bien ete genere')
