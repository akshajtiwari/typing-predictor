<div align="center">

#  MonkeyType Typing Speed Prediction System

### End-to-End Data Engineering + ML Pipeline for Typing Performance Forecasting

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

</div>

---

##  Overview

This project is a **complete end-to-end ML system** that collects MonkeyType typing data, processes it, stores it in PostgreSQL, trains a prediction model per user, and forecasts future typing speed.

It demonstrates real-world engineering skills:

- Data ingestion pipeline  
- Data preprocessing & validation  
- Relational database design  
- ML model training & persistence  
- Backend system architecture  
- Prediction system  

> Designed as a flagship backend + ML portfolio project.

---

#  Why This Project Matters

This project demonstrates:

✔ Data engineering pipeline  
✔ Backend system design  
✔ Database schema design  
✔ ML model lifecycle  
✔ Model persistence  
✔ End-to-end system thinking  
✔ Entire Codebase is handwritten , no LLM/GPT's have been used to write or debug code. 

---

#  System Architecture

##  Invocation Architecture (How components interact)

<div align="center">

```
            ┌──────────────┐
            │   Frontend   │  (CLI / future UI)
            └──────┬───────┘
                   │ HTTP/CLI
                   ▼
            ┌──────────────┐
            │   FastAPI    │
            │  (API Layer) │
            └──────┬───────┘
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
┌──────────────┐      ┌──────────────┐
│ PostgreSQL   │      │ Background   │
│ (Database)   │      │ Worker       │
└──────────────┘      └──────┬───────┘
                               │
                               ▼
                        ┌──────────────┐
                        │   ML Model   │
                        │ Train/Save   │
                        └──────────────┘
```

</div>

### Component Responsibilities

| Component | Responsibility |
|-----------|---------------|
Frontend / CLI | User input, upload CSV, view predictions |
FastAPI | API layer, validation, triggers processing |
Worker | Preprocess → DB insert → Train → Predict |
PostgreSQL | Stores users & typing history |
ML Model | Trains per user & predicts future speed |

---

#  Data Pipeline Architecture

<div align="center">

```
            ┌──────────────────┐
            │      USER        │
            └─────────┬────────┘
                      │
                      ▼
            ┌──────────────────┐
            │     Scraper      │
            │  Downloads CSV   │
            └─────────┬────────┘
                      │
                      ▼
            ┌──────────────────┐
            │  Preprocessing   │
            │ Clean + Transform│
            └─────────┬────────┘
                      │
                      ▼
            ┌──────────────────┐
            │   PostgreSQL     │
            │  users + tests   │
            └─────────┬────────┘
                      │
                      ▼
            ┌──────────────────┐
            │   ML Training    │
            │ per user model   │
            └─────────┬────────┘
                      │
                      ▼
            ┌──────────────────┐
            │   Prediction     │
            │ Future speed     │
            └──────────────────┘
```

</div>

---

#  Database Design

## Users Table
Stores unique users.

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

##  Typing Tests Table
Each row = one typing test.

```sql
CREATE TABLE typing_tests (

 id SERIAL PRIMARY KEY,
 user_id INT REFERENCES users(id),

 test_time TIMESTAMP,

 wpm FLOAT,
 raw_wpm FLOAT,
 accuracy FLOAT,
 consistency FLOAT,

 correct_chars INT,
 incorrect_chars INT,
 extra_chars INT,
 missed_chars INT,

 test_duration FLOAT,
 mode TEXT,
 mode2 INT,
 quote_length INT,
 language TEXT,
 difficulty TEXT,

 is_pb BOOLEAN,
 punctuation BOOLEAN,
 numbers BOOLEAN
);
```



---



#  Project Structure

```
monkeytype-ml/

├── preprocess.py        # preprocessing pipeline
├── scraper.py           # CSV scraper
├── db_insert.py         # database insertion
├── trainer.py           # ML training
├── predictor.py         # prediction logic
│
├── models/              # saved models
├── data/                # raw CSVs
└── README.md
```

---

#  Tech Stack

| Category | Tools |
|----------|------|
Language | Python |
Database | PostgreSQL |
Backend | FastAPI |
ML | Scikit-learn |
Data | Pandas |
Future UI | React |

---



#  Planned Enhancements

- FastAPI endpoints  
- Frontend dashboard  
- Graph visualization  
- Model comparison  
- Docker deployment  
- Async background worker  

---

#  Author

**Akshaj Tiwari**  
Backend • Machine Learning • Full Systems  

---
<div align="center">

### ⭐ If you like this project, consider starring the repo

</div>
