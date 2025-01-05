# Utilisation d'une image de base python
FROM python:3.9-slim

# Créer le répertoire /data où ton fichier CSV sera monté
VOLUME ["/data"]

# Copier ton fichier CSV dans le conteneur
# Remplace "your_file.csv" par le nom du fichier que tu veux ajouter
COPY poster.parquet /data/poster.parquet

# Installer les dépendances nécessaires si nécessaire (ex: pandas, mysql-connector, etc.)
RUN pip install mysql-connector-python pandas
