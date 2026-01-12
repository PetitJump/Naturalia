# Naturalia v1

## Fonctionnement du programme:
Ce programme simule l’évolution d’un écosystème simple composé de loups, de moutons et d'herbes au fil des jours. À partir de règles définies dans un fichier JSON (et modifiable dans plus tard), il gère les naissances selon des cycles de reproduction et un nombre de nouveau-nés partiellement aléatoire, puis les morts liées à l’alimentation et à la disponibilité des ressources. La fonction principale met à jour les populations à chaque jour de simulation en appliquant successivement la reproduction et la mortalité, ce qui permet de modéliser de manière réaliste les interactions entre les différentes formes de vie.

## Differents fichiers :
- terminal.py : Fichier du programme qui fonctionne sur le terminal. Il suffit de le lancer
- app.py : fichier où flask est implementer. Il suffit de lancer le programme et aller sur : [Ici](http://127.0.0.1:5000) 
- algo.py : Tout les algos utiliser. Seul l'algo update() est utiliser dans Flask
- data.json : Loi du monde modifiable via le menus 'règles'
