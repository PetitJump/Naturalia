import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

def creer_graphique(historique):
    """Crée un graphique matplotlib et le retourne en base64 pour l'affichage HTML"""
    if not historique["loup"]:  # Si l'historique est vide
        return None
    
    plt.figure(figsize=(8, 5))
    
    jours = list(range(1, len(historique["loup"]) + 1))
    
    plt.plot(jours, historique["loup"], label='Loups', color='red', linewidth=2, marker='o', markersize=4)
    plt.plot(jours, historique["mouton"], label='Moutons', color='blue', linewidth=2, marker='s', markersize=4)
    plt.plot(jours, historique["herbe"], label='Herbe', color='green', linewidth=2, marker='^', markersize=4)
    
    plt.title('Évolution de l\'écosystème', fontsize=14, fontweight='bold')
    plt.xlabel('Jour', fontsize=12)
    plt.ylabel('Population', fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    
    img = io.BytesIO()
    plt.savefig(img, format='png', dpi=100, bbox_inches='tight')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return f'data:image/png;base64,{graph_url}'
