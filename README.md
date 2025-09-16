# Churn-Retention-Pipeline
📝 Project Overview

This project demonstrates a complete ETL pipeline for analyzing Telco Customer Churn.
The pipeline covers data generation, orchestration, processing, storage, and visualization, showcasing a full Data Engineering workflow from raw data to actionable insights.

Pipeline Summary:

Data Source: Original Telco Customer Churn dataset from Hugging Face
.

Synthetic Data Generation: Extended the dataset using Faker library to simulate additional customer records.

Orchestration: Managed the workflow using Apache Airflow.

Data Storage: Raw and processed data stored in HDFS.

Data Transformation: Performed transformations using Apache Spark.

Data Warehouse: Transformed data loaded into SQL Server (SSMS) for analytics.

Visualization: Built interactive dashboards using Power BI to track churn metrics and customer retention.

⚙️ Tools & Technologies

Data Source: Hugging Face Datasets (aai510-group1/telco-customer-churn)

Synthetic Data Generation: Python Faker

Workflow Orchestration: Apache Airflow

Big Data Storage: HDFS (Hadoop Distributed File System)

Data Processing & Transformation: Apache Spark

Data Warehouse: Microsoft SQL Server (SSMS)

Visualization & Reporting: Power BI

📊 Pipeline Flow Diagram
Hugging Face Dataset  -->  Faker (synthetic data generation)
           │
           ▼
       Airflow (Orchestration)
           │
           ▼
         HDFS (Raw & Processed Data)
           │
           ▼
      Apache Spark (Transformations)
           │
           ▼
        SQL Server (DWH)
           │
           ▼
       Power BI Dashboard

🔹 Key Features

Automated ETL pipeline with Airflow DAGs.

Scalable and fault-tolerant HDFS storage.

Distributed data transformations using Spark.

Integration with SQL Server for analytics and reporting.

Interactive Power BI dashboard for churn & retention insights.

📥 How to Run

Clone the repo

git clone <your-repo-link>
cd telco-churn-etl


Install dependencies

pip install datasets faker pyspark


Start Airflow

airflow db init
airflow webserver -p 8080
airflow scheduler


Run ETL pipeline via Airflow DAG.

Access processed data in HDFS, Spark, or SQL Server.

Open Power BI and connect to SQL Server to visualize metrics.

🔹 Optional Enhancements

Add Kafka as streaming source for real-time churn analysis.

Implement data quality checks using Great Expectations or similar.

Extend dashboard with predictive churn models using ML.
