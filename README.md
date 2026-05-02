# 🚀 Real-Time Data Engineering Pipeline

A scalable real-time data pipeline built with modern data engineering tools, designed to simulate event-driven architectures and streaming workflows.

---

## 🧠 Overview

This project demonstrates how to build a complete streaming pipeline:

**JSONPlaceholder API → Apache Airflow → Apache Kafka → Apache Spark → Cassandra**

It simulates real-time ingestion, transformation, and storage of structured data.

---

## 🏗 Architecture

```
        ┌──────────────┐
        │ JSONPlaceholder API │
        └───────┬──────┘
                │
                ▼
        ┌──────────────┐
        │  Airflow DAG │
        │ (Producer)   │
        └───────┬──────┘
                │
                ▼
        ┌──────────────┐
        │   Kafka      │
        │ posts_stream │
        └───────┬──────┘
                │
                ▼
        ┌──────────────┐
        │    Spark     │
        │ (Streaming)  │
        └───────┬──────┘
                │
                ▼
        ┌──────────────┐
        │  Cassandra   │
        │ created_posts│
        └──────────────┘
```

---

## ⚙️ Tech Stack

* 🐍 Python
* 🔄 Apache Airflow
* 📡 Apache Kafka
* ⚡ Apache Spark (Structured Streaming)
* 🗄 Cassandra
* 🐳 Docker & Docker Compose

---

## 📊 Data Source

* API: https://jsonplaceholder.typicode.com/posts
* Simulated streaming via Airflow

---

## 🔧 Features

* Real-time data ingestion from REST API
* Kafka-based event streaming
* Spark Structured Streaming processing
* Cassandra sink for scalable storage
* Fully containerized setup with Docker

---

## ▶️ Getting Started

### 1. Start services

```bash
docker-compose up --build
```

---

### 2. Access UIs

* Airflow: http://localhost:8080
* Kafka Control Center: http://localhost:9021
* Spark UI: http://localhost:4040

---

### 3. Run Pipeline

* Trigger DAG: `jsonplaceholder_posts_pipeline`
* Data will stream automatically into Kafka and Cassandra

---

## 🗄 Cassandra Schema

```sql
CREATE TABLE spark_streams.created_posts (
    id UUID PRIMARY KEY,
    post_id INT,
    user_id INT,
    title TEXT,
    body TEXT
);
```

---

## 📁 Project Structure

```
.
├── dags/
├── spark/
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🚀 Future Improvements

* Add Kafka Consumer monitoring
* Integrate ML / NLP pipeline (e.g. sentiment analysis)
* Implement schema validation (Avro / Schema Registry)
* Add data quality checks
* Deploy to cloud (AWS / GCP)

---

## 💡 Motivation

This project showcases a modern data engineering workflow combining:

* Streaming systems
* Distributed processing
* Scalable storage
* Event-driven architecture

---

## 👨‍💻 Author

Patrick Amann 

MSc in Artificial Intelligence & IT Security

Focus: AI, Data Engineering, Privacy-Preserving Systems

---
