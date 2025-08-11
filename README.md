# ☁️ Weather Data Pipeline with Apache Airflow | Nowa Analytics

This project demonstrates how to build and orchestrate a data pipeline using **Apache Airflow** to extract and store 7-day weather forecast data for Boston. The pipeline enables a tourism company to better plan its tours based on accurate weather predictions.

---

## 🚀 Project Overview

Our client, a tourism company based in Boston, requires a data pipeline that:

* Extracts weather forecast data for Boston for the next 7 days from the **Visualcrossing** API.
* Orchestrates the extraction, processing, and storage using **Apache Airflow**.
* Provides reliable and automated weather data for operational decision making.

---

## 📌 Key Learning Outcomes

* Learn what **Apache Airflow** is and its role in modern data engineering.
* Understand the concepts of **DAGs (Directed Acyclic Graphs)**, **Tasks**, and **Operators**.
* Explore the architecture components of Airflow.
* Get familiar with the Airflow web interface and its main features.
* Develop and deploy your first Airflow DAG to automate data extraction.

---

## ⚙️ Technologies Used

* Python 3.9+
* Apache Airflow
* Visualcrossing Weather API
* REST API requests
* JSON data processing

---

## 📁 Project Structure

```
📦 weather-data-pipeline
├── dags/                  # Airflow DAGs and task definitions
├── scripts/               # Python scripts for data extraction and processing
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── airflow.cfg            # Airflow configuration (if applicable)
```

---

## 📊 Pipeline Description

1. **Extract**: Query the Visualcrossing API for Boston’s 7-day weather forecast.
2. **Transform**: Process and clean the extracted JSON data as needed.
3. **Load**: Save the processed data into a preferred storage system (e.g., CSV file, database).
4. **Orchestration**: Automate the above steps with Airflow DAGs scheduled as per requirements.

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/weather-data-pipeline.git
cd weather-data-pipeline
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Initialize Airflow and start the scheduler and webserver:

```bash
airflow db init
airflow scheduler
airflow webserver
```

4. Access the Airflow UI at `http://localhost:8080` and trigger the DAG.

---

## 🧠 Insights

* Apache Airflow enables reliable orchestration of complex data pipelines.
* Scheduling and dependency management are simplified with DAGs.
* Automating data extraction helps businesses leverage real-time data effectively.

---

## 🏢 About Nowa Analytics

Nowa Analytics is a data consulting company specializing in scalable data architectures, orchestration, and AI-driven insights.

📍 Offices in São Paulo, Madrid, and London
🌐 [nowaanalytics.com](http://nowaanalytics.com)

---

## 📬 Contact

* 📧 [contact@nowaanalytics.com](mailto:contact@nowaanalytics.com)
* 💼 [LinkedIn – Nowa Analytics](https://linkedin.com/company/nowaanalytics)
