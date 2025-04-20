import pandas as pd
from sqlalchemy import create_engine, text

def create_table_if_not_exists(engine, schema_path: str):
    """
    Crée la table dans PostgreSQL si elle n'existe pas encore.
    """
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()
    with engine.begin() as conn:
        conn.execute(text(schema_sql))


def load_dataframe_to_postgres(df: pd.DataFrame, db_url: str, schema_path: str):
    """
    Charge un DataFrame dans la base PostgreSQL.

    :param df: DataFrame prêt à insérer
    :param db_url: URL de connexion PostgreSQL
    :param schema_path: Chemin vers le fichier SQL (création de la table)
    """
    engine = create_engine(db_url)
    create_table_if_not_exists(engine, schema_path)

    # Insertion dans la table
    with engine.begin() as conn:
        df.to_sql("intercites_regularite", con=conn, if_exists="append", index=False)

    print("✅ Données chargées dans la base PostgreSQL.")

# Exemple de test (optionnel)
if __name__ == "__main__":
    from transform import clean_transport_data

    csv_path = "data/raw/intercites_ponctualite.csv"
    df = clean_transport_data(csv_path)

    db_url = "postgresql://airflow:airflow@localhost:5432/airflow"
    schema_path = "db/schema.sql"

    load_dataframe_to_postgres(df, db_url, schema_path)
