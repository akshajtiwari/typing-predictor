<div align="center">

# ⌨ MonkeyType Typing Speed Prediction System

### End-to-End Data Engineering + ML Pipeline for Typing Performance Forecasting

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Completed%20(Core%20Pipeline)-brightgreen)

</div>

---

##  Overview

This project is a complete **end-to-end machine learning pipeline** that:

- Collects MonkeyType typing history  
- Cleans and preprocesses raw CSV data  
- Stores structured data in PostgreSQL  
- Trains a per-user prediction model  
- Forecasts future typing speed  

The system is designed as a **realistic backend + ML engineering project**, focusing on learning tools like **Selenium** and **PostgreSQL** and  creating a basic end to end ML system.

> This repository represents the completed core pipeline.  
> Future enhancements are listed below but are not required for functionality.

---

#  Why This Project Matters

This project demonstrates:

✔ End-to-end data pipeline design  
✔ Real database schema & relations  
✔ Automated ingestion + preprocessing  
✔ Model training & persistence  
✔ Prediction system design  
✔ Modular codebase structure  
✔ System-level engineering thinking  

> Entire codebase written manually without LLM-generated code for implementation or debugging.

---

#  System Architecture

## Invocation Structure (Current Implementation)

<div align="center">

```
            ┌──────────────┐
            │    CLI App   │
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │   Scraper    │
            │ (Selenium)   │
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │ Preprocessing│
            │   Pipeline   │
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │ PostgreSQL   │
            │ users/tests  │
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │ ML Training  │
            │ Polynomial   │
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │ Prediction   │
            │ (Future WPM) │
            └──────────────┘
```

</div>

---

# Data Pipeline

<div align="center">

```
User → Scraper → CSV → Preprocessing → PostgreSQL → Model Training → Prediction
```

</div>

### Pipeline Stages

1. Scrape MonkeyType typing history  
2. Clean and normalize dataset  
3. Store structured data in PostgreSQL  
4. Train polynomial regression model  
5. Predict future typing performance  

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

## Typing Tests Table
Each row represents one typing test.

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

**Relationship:**  
One user → Many typing tests  
`users.id → typing_tests.user_id`

---

#  Model Approach

Model: Polynomial Regression (Time-based)

The model learns:

```
typing_speed = f(time)
```

It captures:
- improvement trends  
- plateau behavior  
- long-term typing growth  

Prediction:
- future WPM after X months  
- based purely on historical trend  

---

#  Project Structure

```
typing-predictor/

├── main.py              # main pipeline controller
├── login.py             # monkeytype scraper
├── preprocess.py        # data cleaning pipeline
├── insert_db.py         # database insertion
├── model.py             # training + prediction
│
├── raw_data/
├── downloaded_files/
├── models/
└── README.md
```

---

# 🛠️Tech Stack

| Category | Tools |
|----------|------|
Language | Python |
Database | PostgreSQL |
ML | Scikit-learn |
Automation | Selenium |
Data | Pandas |

---

#  Future Enhancements (Optional)

These are **ideas for future expansion**, not required for current functionality:

- FastAPI backend for API-based predictions  
- Frontend dashboard with graphs  
- Multi-user prediction comparison  
- Model comparison (Linear vs Poly vs ARIMA)  
- Dockerized deployment  
- Cloud hosting  

---

# Author

**Akshaj Tiwari**  
Backend • Machine Learning • Systems Engineering  

---

<div align="center">

### ⭐ If you found this project interesting, consider starring the repository

</div>