# Nature du code et usage de l'IA

## Degré de création originale

Le projet Ecologic est un projet original. L'idée de simuler un écosystème proie-prédateur, la conception du modèle biologique, l'architecture Flask et le système de succès ont été conçus et réalisés par l'équipe.

Les modèles mathématiques utilisés — croissance logistique de Verhulst (1838) et dynamique prédateur-proie inspirée de Lotka-Volterra — sont des concepts académiques classiques, librement documentés, que nous avons adaptés à une simulation discrète avançant année par année.

Aucune bibliothèque externe de simulation ou de visualisation n'a été utilisée. Le graphique d'évolution et le diagramme en anneau sont codés entièrement en JavaScript avec l'API Canvas native.

## Sources externes

- **Flask** — framework web Python (https://flask.palletsprojects.com/)
- **Press Start 2P** — police pixel art (Google Fonts)
- **Modèle logistique** — cours de mathématiques / Wikipédia

## Utilisation de l'intelligence artificielle

Nous avons utilisé **Claude (Anthropic)** comme assistant technique tout au long du développement. Son rôle a principalement porté sur :

- **Débogage** : corriger des erreurs de logique dans les calculs biologiques (broutage, famine, reproduction conditionnelle) et des bugs d'affichage (z-index des modals, persistance des données lors des swaps AJAX)
- **Interface graphique** : aide à la mise en forme CSS, refonte visuelle en pixel art, création du système de thèmes (Game Boy, Parchemin, Workbench, Naturalia)
- **Structuration du code** : organisation des templates Jinja2, gestion des sessions Flask, requêtes SQL pour le classement

Tous les choix de conception — modèle biologique, paramètres de simulation, fonctionnalités de jeu, architecture — ont été décidés par l'équipe. L'IA a été un outil d'exécution et de débogage, pas de conception. Nous sommes en mesure d'expliquer et de justifier chaque partie du code.
