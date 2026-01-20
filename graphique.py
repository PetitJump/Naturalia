import pandas as pd
import matplotlib.pyplot as plt


def graphique(data: list, historique: dict):
    df = pd.DataFrame(historique)
    plt.plot(df['jour'], df['predateur'], label='Prédateurs')
    plt.plot(df['jour'], df['proie'], label='Proies')
    plt.plot(df['jour'], df['vegetal'], label='Végétaux')
    plt.xlabel('Jour')
    plt.ylabel('Population')
    plt.title('évolution des population')
    plt.grid()
    plt.show()