Dossier ISN

- Projet PatricK -
Environnement de programmation visuel et simplifié



Membres de l'équipe :
Matteo LUCAS
Kilian MARCELIN
SOMMAIRE

1 - Introduction

2 - Notice d’utilisation

3 - Outils utilisés

4 - Planning

5 - Rôles

6 - Conclusion


INTRODUCTION

Nous avons décidez de nous lancer dans le développement de ce projet avec l’objectif de simplifier la programmation en python en la rendant plus visuelle. L’idée était de nous inspirer de Scratch ou d’autres VPL (Visual Programming Language). Le fonctionnement est simple: plutôt que de taper au clavier le code, on déplace des blocs correspondant à certaines instructions. Les grands avantages de ce type de programmation sont la simplicité d’utilisation et par conséquent de son apprentissage mais également les erreurs de syntaxes ne pouvant êtres présentes, évitant ainsi ce type d’erreur courant.

	

NOTICE D’UTILISATION

Le programme se présente sous la forme d’un fichier python et de quelques images. Lorsqu’on l'exécute un fenêtre apparaît. Il faut alors constituer son programme à la suite du bloc “Début”. 

Le fonctionnement des boucles 
Il est bien évidemment possible de faire des boucles ou utiliser des condition cependant à la fin d’un instruction conditionnelle il faut placer un bloc “fin de boucle”. comme dans l'exemple ci-dessous :

Ajouter une valeur
Certain blocs comme “Afficher” nécessitent qu’on leur ajoute une valeur (dans ce cas là, ce qu’il faut afficher). Pour se faire il faut, après avoir cliquer sur le bloc pour le sélectionner,  cliquer sur le bouton “Ajouter une valeur” et entrer la valeur.

Exécution du programme
Après avoir mit les blocs dans l’ordre souhaité, il est possible d’exécuter le programme afin de se rendre compte du résultat. Pour cela, il suffit d’aller dans Actions, puis Exécuter. Si le projet a été lancé depuis PyCharm, le résultat du programme s'affiche dans la console du logiciel. S’il a été lancé avec l’exécutable, alors le résultat d’affiche dans la console. Le bouton Exécuter sauvegarde le programme dans un fichier nommé: “monFichierPatricK.py” mais il est également possible de sauvegarder sans exécuter avec le bouton Sauvegarder.

Les différents blocs

Afficher
Affiche une variable ou une string si la valeur a été mise entre guillemets. Correspond à print.


Aléatoire
Stocke un nombre  entier aléatoire dans une variable. Il y a trois valeurs à donner: la variable dans laquelle stocker le nombre, le plus petit nombre possible ainsi que le plus grand.

Attendre
Fait attendre x secondes avant de lire la suite du programme, x étant le nombre précisé en valeur.

Fin de boucle
Précise la fin d’une boucle. Si non précisée, les blocs suivants un bloc tel que Si seront compris dans la boucle.

Répéter
Boucle pour répéter une série d’actions. Une valeur à donner, le nombre de répétition. Correspond à for.

Saisir
Demande à l’utilisateur de saisir une chaîne de caractère qui est stocké dans la variable spécifiée en valeur.

Si
Boucle si. La valeur à préciser correspond à la condition qui doit être remplie pour que la boucle soit lue, exemple de valeur à donner: a == true. Correspond à if.

Sinon
Boucle sinon. Aucunes valeurs à spécifier. Correspond à else.

Tant que
Boucle tant que. La valeur à préciser correspond à la condition qui doit être remplie pour que la boucle soit lue, exemple de valeur à spécifier: i <= nb. Correspond à while

Variable
Bloc de variable, la valeur donnée sera transcrite tel quelle dans le fichier “monFichierPatricK.py”.

OUTILS UTILISÉS

PyCharm
PyCharm est un environnement de développement intégré utilisé pour programmer en Python. C’est le logiciel que nous avons utilisé en cours et avec lequel nous avons appris le python, nous avons décider de l’utiliser afin de ne pas avoir à apprendre l’utilisation d’un nouveau logiciel.

Bibliothèques utilisées:
Tkinter afin de réaliser l’interface.
Threading pour utiliser les threads.
Os pour exécuter le programme finit.
ImageTk pour importer les images des différents blocs.

Gimp
Gimp a permit de créer les images représentant les différents. Nous l’avons utilisé car il est une alternative gratuite à Photoshop.

GitHub
GitHub nous a permit de partager le projet simplement. Dès que nous modifions le projet de notre côté nous pouvions envoyé notre version sur gitHub et l’autre membre du groupe pouvait alors avoir accès au nouveau(x) fichier(s)

Discord
Discord nous a permit de communiquer simplement et rapidement. Il nous a permit de discuter par écrit mais également par oral. Discord permet également de faire des partages d’écrans et de transmettre des fichiers. Nous l'utilisons déjà auparavant il nous était donc évident d’utiliser cet outil.

Monday
Monday est une application web et mobile facilitant la gestion de projet. Nous l’avons utilisé pour se répartir les tâches ainsi que pour voir l’avancement de chacunes d’elles.

