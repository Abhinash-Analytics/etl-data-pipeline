# 🚀 ETL Data Pipeline (Python | OOP | Config-Driven)

A scalable and modular ETL (Extract, Transform, Load) pipeline built using Python.
Designed with object-oriented principles and a config-driven architecture to process data from multiple sources.

---

## 📌 Key Features

* Multi-source ingestion (CSV, JSON, API, Database)
* Config-driven pipeline using YAML
* Modular and reusable architecture
* Built using Object-Oriented Programming (OOP)
* Logging and data validation support

---

## 🏗️ Project Structure

```
ETL_Project/
│
├── data/
├── ingestion/
│   ├── base.py
│   ├── read_csv.py
│   ├── read_json.py
│   ├── read_api.py
│   └── read_db.py
│
├── transformation/
│   ├── base.py
│   └── cleaning.py
│
├── pipeline/
│   └── pipeline.py
│
├── utils/
│   ├── config_loader.py
│   ├── logger.py
│   └── validation.py
│
├── log/
│   └── pipeline.log
│
├── config.yaml
└── main.py
```

---

## 🔄 How It Works

1. Extract data from multiple sources
2. Transform and clean the data
3. Validate data quality
4. Load the processed output

---

## ▶️ Run the Project

```bash
git clone https://github.com/your-username/etl-data-pipeline.git
cd etl-data-pipeline
pip install -r requirements.txt
python main.py
```

---

## 🧠 Why This Project

* Demonstrates end-to-end ETL pipeline design
* Shows modular and scalable architecture
* Reflects real-world data engineering practices

---

## 👨‍💻 Author

Abhinash Dora (Avi)
Aspiring Data Engineer | Python | SQL | AWS
