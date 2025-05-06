import pandas as pd
import numpy as np

def clean_transport_data(csv_path: str) -> pd.DataFrame:
    """
    Nettoie et transforme les données de régularité Intercités.

    - Standardise les noms de colonnes
    - Convertit les dates
    - Calcule un ratio de ponctualité à partir des données brutes
    - Conserve la valeur du ratio fournie par la SNCF (source) pour comparaison

    :param csv_path: Chemin vers le fichier CSV brut
    :return: DataFrame nettoyé et enrichi
    """
    # Chargement du fichier CSV
    df = pd.read_csv(csv_path, sep=';')

    # Nettoyage des noms de colonnes
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace("'", '')
        .str.replace('[^a-z0-9_]', '', regex=True)
    )

    # Renommage standard pour les noms de colonnes
    df.rename(columns={
        "date": "jour",
        "depart": "gare_depart",
        "arrivee": "gare_arrivee",
        "nombre_de_trains_programmes": "nb_trains_programmes",
        "nombre_de_trains_ayant_circule": "nb_trains_circules",
        "nombre_de_trains_annules": "nb_trains_annules",
        "nombre_de_trains_en_retard_a_l_arrivee": "nb_trains_en_retard",
        "taux_de_regularite": "taux_regularite",
        "nombre_de_trains_a_l_heure_pour_un_train_en_retard_a_l_arrivee":
            "ratio_source_trains_a_lheure_par_retard"
    }, inplace=True)

    # Conversion de la date
    df["jour"] = pd.to_datetime(df["jour"], errors="coerce")

    # Suppression des lignes invalides
    df.dropna(subset=["jour", "gare_depart", "gare_arrivee"], inplace=True)

    # Calcul de notre propre ratio : (trains à l'heure / trains en retard)
    df["ratio_recalc_trains_a_lheure_par_retard"] = (
        (df["nb_trains_circules"] - df["nb_trains_en_retard"]) / df["nb_trains_en_retard"]
    ).round(3)

    # Nettoyage des valeurs infinies et NaN
    col = "ratio_recalc_trains_a_lheure_par_retard"
    df[col] = df[col].replace([float("inf"), -float("inf")], np.nan)
    df[col] = df[col].astype("float64").fillna(0)
    return df


# Test manuel en local
if __name__ == "__main__":
    path = "data/raw/intercites_ponctualite.csv"
    df_clean = clean_transport_data(path)
    print(df_clean.head())
    print(df_clean.dtypes)
