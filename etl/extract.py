# etl/extract.py

import os
import requests

def download_transport_data(url: str, save_path: str) -> None:
    """
    Télécharge le fichier CSV depuis l'URL et le sauvegarde localement.

    :param url: URL du fichier à télécharger
    :param save_path: Chemin de sauvegarde local
    """
    response = requests.get(url)
    response.raise_for_status()

    dir_name = os.path.dirname(save_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    with open(save_path, "wb") as f:
        f.write(response.content)

    print(f"✅ Fichier téléchargé et sauvegardé à : {save_path}")


if __name__ == "__main__":
    url = "https://data.sncf.com/explore/dataset/regularite-mensuelle-intercites/download/?format=csv"
    save_path = "data/raw/intercites_ponctualite.csv"
    download_transport_data(url, save_path)
