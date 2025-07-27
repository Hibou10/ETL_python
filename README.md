# ETL_python

# 🌐 ETL-Pipeline: Universities in California (USA)

Dieses Projekt zeigt eine vollständige ETL-Pipeline mit Python: von der Datenextraktion über Transformation bis zum Laden in eine SQLite-Datenbank.

## 🧠 Projektbeschreibung

Die Pipeline lädt Universitätsdaten aus einer öffentlichen API, filtert gezielt nach Universitäten mit dem Begriff **"California"** im Namen und speichert die bereinigten Daten strukturiert in eine lokale SQLite-Datenbank.

## 📊 ETL-Schritte

### 1. 🟦 Extract
- Datenquelle: [http://universities.hipolabs.com](http://universities.hipolabs.com)
- Abgerufen wird eine Liste aller Universitäten in den **USA**
- Die Daten werden als JSON geladen

### 2. 🟨 Transform
- Umwandlung in ein `pandas.DataFrame`
- Filter: Nur Universitäten mit `"California"` im Namen
- Spalten `domains` und `web_pages` werden von Listen zu Strings konvertiert
- Index wird zurückgesetzt und relevante Spalten ausgewählt

### 3. 🟩 Load
- Die transformierten Daten werden mit `SQLAlchemy` in eine **SQLite-Datenbank** (`my_lite_store.db`) geladen
- Tabelle: `cal_uni`

## 🛠️ Verwendete Technologien

- Python 3
- pandas
- requests
- SQLAlchemy
- SQLite
- Jupyter Notebook (optional)

## 📁 Dateien

| Datei             | Beschreibung                                     |
|-------------------|--------------------------------------------------|
| `etl.py`          | Das Hauptskript mit allen drei ETL-Schritten     |
| `etl.ipynb`       | Jupyter-Version der ETL-Pipeline   |
| `my_lite_store.db`| SQLite-Datenbank mit der Tabelle `cal_uni`       |


