# Journal des modifications — Ecologic

---

## Version : Profil utilisateur + Leaderboard

---

## 1. Ajout des statistiques par profil

### Fichier modifié : `sources/app.py`

**Nouvelle table SQL `Stats`** créée dans `init_db()` :

```sql
CREATE TABLE IF NOT EXISTS Stats (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id    INTEGER NOT NULL,
    nb_parties INTEGER DEFAULT 0,
    max_loups  INTEGER DEFAULT 0,
    max_cerfs  INTEGER DEFAULT 0,
    max_annees INTEGER DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES Compte(id)
)
```

**Nouvelle fonction `maj_stats(username, annee_fin, historique)`**
- Appelée automatiquement à chaque fin de partie (extinction d'une espèce)
- Récupère le `user_id` depuis la table `Compte`
- Si une ligne existe déjà pour ce joueur : met à jour avec `MAX()` pour ne garder que les records
- Sinon : crée une nouvelle ligne
- Ne fait rien si le joueur n'est pas connecté (username = None)

**Nouvelle fonction `get_stats(username)`**
- Retourne un dict `{nb_parties, max_loups, max_cerfs, max_annees}` pour un joueur
- Retourne des 0 si aucune partie jouée

**`maj_stats` appelée dans les 3 routes de fin de partie :**
- `/game` — fin de partie normale tour par tour
- `/accelerer` — fin de partie en mode accéléré
- `/update_ajouter` — fin de partie après ajout manuel d'individus

---

## 2. Onglet profil avec dropdown (top droite de l'accueil)

### Fichier modifié : `sources/templates/index.html`

**Remplacement de la barre utilisateur** par un bouton profil avec dropdown :

- Avatar circulaire avec l'initiale du pseudo
- Clic sur le bouton → panel animé qui s'ouvre
- Clic en dehors → panel qui se ferme
- **Grille de 4 stats** dans le panel :
  - Parties jouées
  - Max années atteint
  - Max loups atteint
  - Max cerfs atteint
- Bouton "Se déconnecter" en bas du panel

Si l'utilisateur n'est pas connecté : boutons Connexion / S'inscrire à la place.

---

## 3. Leaderboard Top 10 avec onglets

### Fichier modifié : `sources/app.py`

La route `/` passe maintenant 3 listes au template au lieu d'une seule :
- `lb_annees` — top 10 par `max_annees`
- `lb_loups` — top 10 par `max_loups`
- `lb_cerfs` — top 10 par `max_cerfs`

Seuls les joueurs ayant au moins une partie terminée apparaissent (`WHERE score > 0`).

### Fichier modifié : `sources/templates/index.html`

**Nouveau composant leaderboard** avec 3 onglets cliquables :
- `Années` — classement par durée de partie
- `Loups` — classement par max loups simultanés
- `Cerfs` — classement par max cerfs simultanés

**Médailles** pour le podium : 🥇 🥈 🥉, numéro simple ensuite.

**Mise en évidence** du joueur connecté dans le classement (nom en vert + flèche ◀).

Basculement entre onglets via la fonction JS `switchLb(panneau, el)` — aucun rechargement de page.

---

## Résumé des fichiers modifiés

| Fichier | Modification |
|---|---|
| `sources/app.py` | Table `Stats`, fonctions `maj_stats` + `get_stats`, 3 leaderboards dans route `/` |
| `sources/templates/index.html` | Dropdown profil, stats dans le panel, leaderboard avec onglets |

## Aucun fichier créé ou supprimé.
