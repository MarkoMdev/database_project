# 🚆 Transport Data ETL Project

Ce projet a pour objectif de mettre en place une pipeline ETL (Extract - Transform - Load) pour analyser les données de ponctualité des trains en France à l'aide d'outils de data engineering open source.

---

## 🧰 Stack technique

- **PostgreSQL** : stockage relationnel des données
- **Apache Airflow** : orchestration des pipelines ETL
- **Apache Superset** : exploration et visualisation des données
- **Python (pandas)** : transformation des données

---

## 📊 Dataset utilisé

Données publiques issues de [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/ponctualite-des-trains-voyageurs-ter-intercites-et-transilien/)

- Format : CSV
- Données mensuelles de ponctualité des trains (TER, Intercités, Transilien)
- Contient : nombre de trains, taux de ponctualité, causes de retard...

---

## 🔁 Étapes du pipeline

1. **Extraction** : Téléchargement des données depuis data.gouv.fr
2. **Transformation** : Nettoyage et formatage avec pandas
3. **Chargement** : Insertion dans une base PostgreSQL
4. **Visualisation** : Dashboard interactif via Apache Superset

---

## 🚀 À venir

- Ajout de données météo (OpenWeatherMap)
- Intégration avec dbt pour modélisation analytique
- Déploiement complet avec Docker Compose

---

## 📁 Structure du projet

transport-data-etl/ 
├── dags/ # Pipelines Airflow 
├── data/ # Données brutes / clean 
├── db/ # Schéma PostgreSQL 
├── superset/ # Dashboards 
├── docker-compose.yml 
├── README.md 
└── requirements.txt