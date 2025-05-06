# 🚆 ETL Transport Intercités – Data Engineering Project

Ce projet met en œuvre un pipeline ETL complet pour collecter, transformer et charger des données de régularité des trains Intercités (SNCF), en s'appuyant sur une stack open source professionnelle.

---

## 🛠️ Stack utilisée

* **PostgreSQL** : stockage relationnel des données
* **Apache Airflow** : orchestration des étapes ETL
* **Docker Compose** : environnement de développement reproductible
* **Python (pandas, SQLAlchemy)** : transformation et chargement des données

---

## 📊 Source des données

* Données issues du portail officiel SNCF :
  [https://data.sncf.com/explore/dataset/regularite-mensuelle-intercites](https://data.sncf.com/explore/dataset/regularite-mensuelle-intercites)
* Format : CSV mensuel
* Données depuis janvier 2014

---

## 🗂️ Structure du projet

```
.
├── dags/               # DAG Airflow (etl_transport.py)
├── etl/                # Scripts extract / transform / load
├── db/                 # Schéma SQL
├── data/               # Fichiers CSV et Parquet
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ Lancer le projet en local

### 1. Démarrer l’environnement

```bash
docker-compose up -d
```

### 2. Accéder à Airflow

* Interface : [http://localhost:8080](http://localhost:8080)
* Identifiant : `admin` / Mot de passe : `admin`

### 3. Lancer le pipeline

* Activer le DAG `etl_transport_data`
* Cliquer sur "Trigger DAG"
* Suivre l'exécution dans les logs (extract → transform → load)

---

## 💡 Fonctions principales

* `download_transport_data(url, path)` : télécharge le fichier CSV brut
* `clean_transport_data(csv_path)` : nettoie les données, calcule les ratios
* `load_dataframe_to_postgres(df, db_url, schema_path)` : charge dans PostgreSQL
* Le DAG appelle ces fonctions via Airflow, avec passage des données par fichier `.parquet`

---

## 📌 À venir

* 🔄 Intégration de données météo pour analyse croisée
* 📊 Ajout d’Apache Superset pour visualiser les retards
* 🔁 Déploiement continu avec Airflow + cron

---

## ✍️ Auteur

Marko Macanovic
