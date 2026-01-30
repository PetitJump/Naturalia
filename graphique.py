import matplotlib
matplotlib.use('Agg')  # Backend non-interactif pour Flask
import matplotlib.pyplot as plt
import io
import base64

def creer_graphique(historique):
    """Crée un histogramme empilé avec l'herbe en ligne et le retourne en base64 pour l'affichage HTML"""
    if not historique["loup"]:  # Si l'historique est vide
        return None
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    nb_jours = min(10000, len(historique["loup"]))
    jours = list(range(len(historique["loup"]) - nb_jours + 1, len(historique["loup"]) + 1))
    
    loups =[ math.log10(x) for x in historique["loup"][-nb_jours:]]
    moutons =[ math.log10(x) for x in historique["mouton"][-nb_jours:]]
    herbes = [ math.log10(x) for x in historique["herbe"][-nb_jours:]]
    
    # Créer l'histogramme empilé pour loups et moutons
    x = range(len(jours))
    
    ax.bar(x, loups, label='Loups', color='red', alpha=0.7, edgecolor='black')
    ax.bar(x, moutons, bottom=loups, label='Moutons', color='blue', alpha=0.7, edgecolor='black')
    
    ax.plot(x, herbes, label='Herbe', color='green', linewidth=3, marker='o', markersize=6)
    
    ax.set_xticks(x)
    ax.set_xticklabels([f'Jour {j}' for j in jours], rotation=45)
    ax.set_title('Répartition des populations par jour', fontsize=14, fontweight='bold')
    ax.set_xlabel('Jour', fontsize=12)
    ax.set_ylabel('Population', fontsize=12)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    
    img = io.BytesIO()
    plt.savefig(img, format='png', dpi=100, bbox_inches='tight')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return f'data:image/png;base64,{graph_url}'

def creer_histogramme(predateur, proie):
    """Crée un histogramme des âges des animaux"""
    if not predateur.get("age") and not proie.get("age"):
        return None
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    if predateur.get("age"):
        ax1.hist(predateur["age"], bins=20, color='red', alpha=0.7, edgecolor='black')
        ax1.set_title('Distribution des âges - Loups', fontsize=12, fontweight='bold')
        ax1.set_xlabel('Âge', fontsize=10)
        ax1.set_ylabel('Nombre', fontsize=10)
        ax1.grid(True, alpha=0.3)
    
    if proie.get("age"):
        ax2.hist(proie["age"], bins=20, color='blue', alpha=0.7, edgecolor='black')
        ax2.set_title('Distribution des âges - Moutons', fontsize=12, fontweight='bold')
        ax2.set_xlabel('Âge', fontsize=10)
        ax2.set_ylabel('Nombre', fontsize=10)
        ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Convertir en base64
    img = io.BytesIO()
    plt.savefig(img, format='png', dpi=100, bbox_inches='tight')
    img.seek(0)
    hist_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return f'data:image/png;base64,{hist_url}'


