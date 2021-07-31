# lamp_state_service
Ce package contient 2 dossiers : src et srv, les fichiers: CMakeLists.txt, package.xml et le readme

Le dossier src contient le fichier que vous devez executez, et le dossier srv contient le fichier necessaire pour que le fichier lamp_state_service_server.py s'execute correctement.

Le but de ce projet est d'afficher les états de chaque lampes en temps réel et les états sont affichés de type json

Vous pouvez aussi changer les états de ces lampadaires et les faire affichés.

Ce projet consiste de 2 types de lampadaires:
- Lampadaires intelligents
- Lampadaires non-intelligents

## A noté!
- Les lampadaires intelligents ont les `lamp_id` de `1 à 4` et les états `0 , 1 et 2`
  - L'état 0 signifie éteint
  - L'état 1 signifie allumé à moyenne puissance
  - L'état 2 signifie allumé à grande intensité

- Les lampadaires non-intelligents ont les `lamp_id` de `5 à 8` et les états `0 et 1`
  - L'état 0 signifie éteint
  - L'état 1 signifie allumé à moyenne puissance

# Installation
Pour installer ce package, il faut cloner ce projet dans le dossier src de votre catkin workspace
```
cd catkin_ws/src
git clone https://github.com/diksha002/lamp_state_service.git
catkin build
cd ..
source devel/setup.bash
```
# Execution
Pour executer ce projet, vous allez executer le fichier lamp_state_service_server.py sur un terminal et simultanément executer des lignes de commandes dans chaque terminal comme décrit dessous. En tous vous aurez 4 terminal qui seront servi en même temps lors de l'execution de ce noeud

## roscore
Ouvrez un terminal et lancer le roscore.

Dans un terminal, typez:
```
roscore
```

## rosrun
Ouvrez un terminal, et executer tous les codes suivant dans le même ordre
```
source devel/setup.bash
cd catkin_ws
cd src/lamp_state_service
cd src
rosrun lamp_state_service lamp_state_service_server.py

```
En même temps, ouvrez un autre terminal et executez les codes suivants:

## rosservice
Dessous TAB signifie le touche Tab sur votre clavier
```
source devel/setup.bash
rosservice call /lamp_state_service_server TAB TAB
```
Puis naviguez votre cursor(La ligne vertical clignotant) jusqu'à data du lamp_id:
- Choisissez un lamp_id entre 1 à 8 , et naviguez votre cursor jusqu'à le data du state et modifiez la valeur de l'état du lampadaire que vous voulez (Veuillez vous referencer sur les chiffres à inséré correctement dans la section précédente nommée `A noté`)
- Puis tapez la touche ENTER
- Si la sortie 'res' est `True`, cela veut dire que l'état du lampadaire est affiché avec succès
- Si la sortie 'res' est `False`, cela veut dire que l'état du lampadaire ne va pas etre afficher et que vous avez fait un erreur en insérant les données 

Executez nombre de fois cette ligne de commande pour manipuler les valeurs et états des lampadaires.

## rostopic
En simultané du rosservice, sur un nouveau terminal, executez ces codes:
```
source devel/setup.bash
rostopic echo /lamp_state
```
Ici vous allez voir les états des lampadaires en temps réel.
