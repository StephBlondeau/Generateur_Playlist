#!/usr/bin/python3
import logging
import Initialisations.loggingConf
import Initialisations.argument

from Initialisations.argument import argumentsParser
from controles.recuperationDonnees import verificationChoisi


#Liste des arguments du programme
#Attributs = ['g','ar','sg','alb','t','r']

'''
Created on 8 oct. 2014
Verification des arguments saisies par l'utilisateur
@author: kitsune, Fx
'''

def convertionInt (quantity):
    '''
    Verifie si la quantite saisie pour un argument est un entier naturel.
    @param quantity: nombre saisie par l'utilisateur pour un argument.
    @return la valeur en entier naturel.
    '''
    
    #On essais de convertir le format de la saisie en entier
    try:
        goodQte = int(quantity)
        #Convertion de la saisie
        logging.info("Un entier a bien ete saisie.")
            
    except ValueError:
        logging.error("Erreur de conversion,la saisie est une chaine.")
        print("Il y a une erreur, veuillez saisir un entier naturel.")
        exit(1)
        
    #On va verifier que l'entier saisie est correcte  
    try:    
        #Si la quantite saisie est un entier naturel
        if goodQte > 0:
            logging.info("L'entier saisie est bien positif.")
            #On retourne la saisie convertie en entier
            return goodQte

            #Sinon (inferieur ou egale a 0) on regarde s'il est egale a 0
        elif goodQte == 0:
            #Si c'est le cas on renvoie en erreur et le programme s'arrete
            logging.error("0 a ete saisie.")
            print('Veuillez saisir un nombre non nul.')
            exit(2)

            #Dans le dernier cas (strictement inferieur a 0)
        else:
            #On convertie le negatif en positif
            goodQte = abs(goodQte)
            logging.info("L'entier saisie est negatif, la saisie a ete transformer donc en entier positif.")
            return goodQte

    except ValueError:
        #Si le programme n'a pas reussi a convertir la saisie en entier (il s'agit donc de caracteres ou caracteres speciaux
        logging.error("Erreur lors de la verification de l'entier.")
        print("Il y a une erreur, veuillez saisir un entier naturel.")
        exit(3)




def pourcentages (pourcentage):
    '''
    Fonction qui permet de calculer un taux de remise a l'echelle selon la pourcentage total qui lui est transmis
    @param pourcentage : total des quantites voulue pour la playlist
    @return: un decimal qui represente le taux de remise a l'echelle a appliquer a toute les quantites
    '''
    
    #On regarde si le pourcentage est different de 100 donc non correcte
    if pourcentage != 100:

        #S'il est superieur a 100
        if pourcentage > 100:
            
            #On va mettre tout les pourcentages des arguments proportionnellement pour atteindre les 100
            proportion = 100 / pourcentage

            #S'il est inferieur a 100
        else:
            #On va mettre tout les pourcentges des arguments proportionnellement pour atteindre les 100.
            proportion = 100 / pourcentage
            
        logging.info("Le programme a mis les pourcentages proportionnel a leur nombre car le pourcentage total n'etait pas de 100.")
    
    else:
        proportion = 1
        
    
    return proportion

def conversionMinutes(ArgumentEntier):
    '''
    fonction qui permet de convertir un entier (pourcentage d'un argument voulue) en minutes
    @param ArgumentEntier: pourcentage d'un argument en entier naturel (donc deja verifie) 
    @return: un entier , le pourcentage est convertie en minutes.
    '''
    #On convertie le pourcentage en minutes selon la duree de la playlist
    Conversion = int (argumentsParser.duree_playlist*ArgumentEntier/100)
    return Conversion

def remettreEchelle(listTArg, echelle):
   
    '''
    Selon le pourcentage va remettre a l'echelle toute les valeurs des arguments
    @param ListeArg : liste des arguments saisie par l'utilisateur
    @param echelle: proporsition a applique a l'ensemble des entiers de la liste
    @return: la liste avec les entiers remit a la meme echelle 
    '''
    
    #Pour chaque élements de la liste on fait une mise a l'echelle de la quantite
    for arg in listTArg:
        #mise a l'echelle
        arg[1] = round(arg[1] * echelle)
        #conversion en minutes
        arg[1] = conversionMinutes(arg[1])
         
    return listTArg

def verifArgument():
    '''
    Fonction qui va vérifié la saisie des arguments de la ligne de commande
    @return une liste de liste 
    '''
    #On va vérifié s"il y a des arguments optionnel utilisés a partir de ceux qui sont possible
    #Liste des arguments du programme
    Attributs = ['g','ar','sg','alb','t']
    
    #on va vérifier que la duree de la playlist est superieur a 0
    if argumentsParser.duree_playlist <= 0:
        logging.error("La duree de la playlist saisie est 0")
        print("Erreur la duree de la playlist ne peut pas être de 0.")
        exit(4) 
    
    #Initialisation des liste
    ListeArg   = list() # liste de depart qui contient tout les tuples d'un argument
    listTArg   = list() # liste final de l'ensemble de tout les tuples de tout les argument
    
    #On initialise le pourcentage total de la playlist
    pourcentageTotal = 0
    
    #Boucle pour parcourir la liste des arguments saisies par l'utilisateur
    for arg in Attributs:       
        i = 0 #On initialise un compteur de tuple par argument

        #On regarde si dans l'argumentParser on trouve un argument qui n'est pas vide (donc ecrit dans la ligne de commande
        if getattr(argumentsParser, arg) is not None:

            #Si le trouve on le range dans une variable de type liste de liste (liste de tuple d'argument)
            ListeArg  = getattr(argumentsParser, arg)
    
            #On enregistre dans le fichier logging l'information
            logging.info("L'option " + arg + " est bien present.")
    
            #Tant qu'il y a plusieurs des tuples pour un argument trouve
            while i < len(ListeArg):
                
                #On controle la saisie qui represente le pourcentage du tuple
                try:
                    #On va donner la saisie a une fonction pour la verifier'''
                    argVerif = convertionInt(ListeArg[i][1]) #Exemple: on prend la valeur 34 de ("Rock", 34)

                    #On rentre la saisie dans une variable qui totalise les pourcentages saisies
                    pourcentageTotal += argVerif
                    
                    #On remplace la saisir de l'utilisateur par un entier correcte s'il ne l'est pas deja
                    if (ListeArg[i][1] != 100):                       
                        ListeArg[i][1] = argVerif
                        
    
                except Exception:
                    logging.error("La fonction de verification d'un entier n'a pas fonctionner")
            
                #On regarde si la saisie est present dans la base de donne'''
                try:
                    #On controle la valeur voulu pour un argument (Ex pour g : (Rock, 34) on recupere Rock)
                    #On verifie que le choisie saisie existe dans la base de donnees grace a une fonction
                    trouveBase = verificationChoisi(ListeArg[i][0], arg) 
    
                    #On regarde si on a trouve l'argument dans la base de donnees
                    if (trouveBase == False):
                        logging.error("La demande "+ ListeArg[i][0] + " pour l'argument "+ arg +" n'ai pas dans la base.")
                        #Si c'est faux on affiche un message d'erreur a l'utilisateur
                        print("Votre demande "+ ListeArg[i][0] + " pour l'argument "+ arg +" n'ai pas dans la base.")
                        #On quitte le programme
                        exit(4)
                            
                except Exception:         
                    logging.error("La verification de la saisie dans la base de donnée n'a pas pu se faire.")

                listTuple = list() # liste qui contient un tuple correcte
                # On range le tuple d'argument (ex: (Rock, 20, g)
                listTuple.append(ListeArg[i][0])
                listTuple.append(ListeArg[i][1])
                
                listTuple.append(arg)
                
                # On range la liste du tuple dans une autre liste
                listTArg .append(listTuple)

                i = i+1 #Incrementation du compteur de tuple
        
        #Si l'argument n'a pas ete trouve dans l'argumentParser
        else:
            logging.info("L'option " + arg + " n'est pas presente.")
     
    #On va faire une remise a l'echelle selon le pourcentage 
    # roud() permet de faire un arrondie
    # pourcentages est une fonction qui va retourner une proportion a appliqué a la remise a l'echelle
    try :
        listTArg = remettreEchelle(listTArg, round(pourcentages(pourcentageTotal),2))
        logging.info("Mise a l'echelle reussie.")
        
    except Exception :
        logging.error("Erreur dans la mise l'echelle")

    return listTArg 

def Veriff (Attributs):
    '''
    Fonction qui permet la verification de tout les quantites de chaque arguments saisies
    @param Attributs: la liste des arguments possibles de la ligne de commande 
    @return: un boolean trouveArg qui permet de savoir si on a trouve au moin un argument optionnel saisie par l'utilisateur
    '''

    #On initialise le pourcentage total de la playlist
    pourcentage = 0

    #On initialise une variable intialiser a false mais qui passe a true si on trouve au moin un argument optionnel dans la ligne de commande
    trouveArg   = False

    #Boucle pour parcourir la liste des arguments saisies par l'utilisateur
    for arg in Attributs:
        #On initialise un compteur de tuple par argument
        i = 0

        #On regarde si dans l'argumentParser on trouve un argument qui n'est pas vide (donc ecrit dans la ligne de commande
        if getattr(argumentsParser, arg) is not None:

            #On a trouve au moin un argument dans la ligne de commande
            trouveArg = True

            #Si le trouve on le range dans une variable de type liste de liste (liste de tuple d'argument)
            ListeArg  = getattr(argumentsParser, arg)
            #On enregistre dans le fichier logging l'information
            logging.info("L'option "+arg+" est bien present.")

            #Tant qu'il y a plusieurs des tuples pour un argument trouve
            while i < len(ListeArg):
                #On range dans une variable le premier tuple de l'argument
                Argument       = ListeArg[i]

                #On recupere le pourcentage du tuple (ex:Pour g : (Rock, 34) on recupere 34
                ArgumentEntier = Argument[1]

                #On controle la saisie qui represente le pourcentage du tuple
                try:
                    #On va donner la saisie a une fonction pour la verifier'''
                    argVerif = convertionInt(ArgumentEntier)

                    #On rentre la saisie dans une variable qui totalise les pourcentages saisies
                    pourcentage += argVerif

                    #On remplace la saisir de l'utilisateur par un entier
                    ListeArg[i][1] = argVerif

                    #Incrementation du compteur de tuple
                    i=i+1

                except Exception:
                    logging.error("La fonction de verification d'un entier n'a pas fonctionner")

                #On controle la valeur voulu pour un argument (Ex pour g : (Rock, 34) on recupere Rock)
                #On regarde si la saisie est present dans la base de donne'''
                try:
                    #On verifie que le choisie saisie existe dans la base de donnée grace a une fonction
                    trouveBase = verificationChoisi(Argument[0], arg)

                    #On regarde si la valeur retourner
                    if (trouveBase == False):
                        logging.error("La demande "+ Argument[0]+ " pour l'argument "+arg+" n'ai pas dans la base.")
                        #Si c'est faux on affiche un message d'erreur a l'utilisateur
                        print("Votre demande "+ Argument[0]+ " pour l'argument "+arg+" n'ai pas dans la base.")
                        #On quitte le programme
                        exit(3)
                        
                except Exception:
                    logging.error("La verification de la saisie dans la base de donnée n'a pas pu se faire.")

        #Si l'argument n'a pas ete trouve dans l'argumentParser
        else:
            logging.info("L'option "+arg+" n'est pas presente.")


    #On regarde si on a trouver au moin un argument optionnel dans la ligne de commande pour continuer la verification
    if trouveArg == True:

        #On donne le total des pourcentages a un fonction
        valeurPourcentage = round(pourcentages(pourcentage),2)

        #On regarde si on doit faire une mise à l'echelle ou non
        if valeurPourcentage != 0:
            #On regarde pour chaque argument possible
            for args in Attributs:

                #On regarde si dans l'argumentParser on trouve un argument qui n'est pas vide (donc ecrit dans la ligne de commande
                if getattr(argumentsParser, args) is not None:
                    #Et on le range dans une variable
                    ListeArg = getattr(argumentsParser, args)

                    #On initialise un compteur d'argument par option
                    i = 0
                    #Tant qu'il y a plusieurs tuples dans un argument
                    while i < len(ListeArg):
                        #On recupere le premier tuple
                        Argument = ListeArg[i]
                        #On recupere l'entier du tuple
                        ArgumentEntier = Argument[1]

                        #Si la valeur est differente de 0 on fais une mise à l'echelle
                        argPourcent = round(ArgumentEntier*round(valeurPourcentage,2))

                        #On essais de convertire les saisies entieres (pourcentage) en minutes
                        try:

                            #Maintenant on convertie la saisie correcte est remis e l'echelle
                            tempsArg = conversionMinutes(int(argPourcent))

                            #On remplace la saisir de l'utilisateur par un entier
                            ListeArg[i][1] = tempsArg

                        except Exception:
                            logging.error("Le remplacement de la valeur entier n'a pas pu se faire.")
                            exit(4)
                        #On incremente le i
                        i = i+1
    return trouveArg             