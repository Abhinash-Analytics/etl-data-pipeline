# 🚀 ETL Data Pipeline (Python | OOP | Config-Driven)

A scalable, modular **ETL pipeline** built using Python to process data from multiple sources into clean, analysis-ready datasets.

Designed using **object-oriented principles** and a **config-driven architecture**, reflecting real-world data engineering practices.

---

## 📌 Key Features

* Multi-source ingestion (**CSV, JSON, API, Database**)
* Config-driven pipeline using **YAML**
* Modular and reusable architecture (OOP-based)
* Built-in **logging and data validation**
* Easy to extend and scale

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

## 🔄 Pipeline Workflow

1. Extract data from multiple sources (CSV, JSON, API, DB)
2. Transform and clean the data
3. Validate data quality
4. Load processed output for downstream use

---

## 🚀 How to Run

```bash
git clone https://github.com/Abhinash-Analytics/etl-data-pipeline.git
cd etl-data-pipeline
pip install -r requirements.txt
python main.py
```

---

## 💡 Highlights

* End-to-end ETL pipeline implementation
* Demonstrates **production-style architecture**
* Handles real-world data formats and validation
* Built with scalability and reusability in mind

---

## 🎯 Why This Project Matters

This project showcases:

* Strong understanding of ETL pipeline design
* Practical experience with **data ingestion, transformation, and validation**
* Ability to build **scalable, maintainable data systems**

---

## 👨‍💻 Author

**Abhinash Dora (Avi)**
Aspiring Data Engineer | Python | SQL | Azure (Exposure)
