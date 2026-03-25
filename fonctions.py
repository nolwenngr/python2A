from great_tables import GT, html
import matplotlib.pyplot as plt


# Question 3
def beau_tableau(df, titre):
    """
    Transforme une base de données en beau tableau.
    """
    tableau = (
        GT(df)
        .tab_header(title=html(f"<b>{titre}</b>"))
    )

    cols_numeriques = df.select_dtypes(include=['number']).columns.tolist()

    if cols_numeriques:
        tableau = tableau.fmt_number(
            columns=cols_numeriques,
            decimals=2,
            sep_mark=" "
        )

    tableau = (
        tableau.tab_options(
            table_font_size="14px",
            column_labels_font_weight="bold",
            table_border_top_style="solid",
            table_border_top_width="3px",
            table_border_top_color="#444444"
        )
        .cols_align(align="center")
    )
    return tableau


# Question 7
def top_surrepresentation(top_n, nom_candidat, donnees):
    """
    Affiche les principales surreprésentations
    (en valeur absolue) par département

    Parameters
    ----------
    n: int
    Représente les n premières
    surreprésentations

    candidat : str
    Nom du candidat dont on veut
    les surreprésentations

    donnees : dataframe
    Données que l'on souhaite étudier
    """
    # Recherche index du candidat
    index_cand = donnees['candidat'].str.contains(nom_candidat, case=False, na=False)

    # Copie avec seulement le candidat pour ne pas modifier le dataframe
    copie_score = donnees[index_cand].copy()
    # Index du top n
    top_abs = (
        copie_score['surrepresentation (%)'].abs().nlargest(5)
        .index
        )
    # Sélection de ces n lignes et tri (plus haut vers plus bat)
    top_deviations = (
        copie_score
        .loc[top_abs]
        .sort_values(by='surrepresentation (%)', ascending=False)
        )
    # Graphique
    plt.barh("code_departement", "surrepresentation (%)", data=top_deviations)
    plt.axvline(x=0)
    plt.xlabel('Surreprésentation')
    plt.ylabel('Département')
    plt.title(f'Top {top_n} des surreprésentations de {nom_candidat}')
    plt.show()


# Question 8
def score_candidat(candidat, donnees):
    """
    Isole le score du candidat

    Parameters
    ----------
    candidat : str
    Prenom NOM du candidat dont on veut
    les surreprésentations

    donnees : dataframe
    Données que l'on souhaite étudier
    """
    copie_score = donnees.copy()
    return copie_score[copie_score["candidat"] == candidat]
