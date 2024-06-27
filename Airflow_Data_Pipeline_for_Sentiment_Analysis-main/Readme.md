# Automated Data Pipeline for Financial News Sentiment Analysis

## Overview
This project aims to build an automated data pipeline that efficiently collects, analyzes, and stores financial news data to provide real-time market insights. The pipeline integrates various technologies, including Finnhub API for data collection, MongoDB for data storage, sentiment analysis for data processing, and PostgreSQL for storing analysis results. Apache Airflow is used to automate the entire workflow

## Step-by-Step Guide
1. Clone the Repository 'https://github.com/fahru-razi/Airflow_Data_Pipeline_for_Sentiment_Analysis.git'
1. Run Airflow with Docker Compose 'docker-compose up'
2. Create Plugins and Scripts:
    - Mongo loader: Fetch data from Finnhub API and load into MongoDB.
    - Finnhub loader: Scripts to interact with MongoDB.
    - Sentiment Analysis: Analyze sentiment from the collected news data.
    - Postgres loader:  Load analysis results into PostgreSQL.
3. Create python code to extract from Finnhub and load to MongoDB
4. Create python code that Get data from MongoDB, Perform Sentiment Analysis, and Load Results to PostgreSQL
5. Run Docker Commands 
    - Enter Airflow webserver container 'docker exec -it airflow_webserver bash'
    - Run Finnhub to MongoDB Loader 'python /opt/airflow/plugins/finnhub_mongodb_loader.py'
    - Run Sentiment Analysis Loader 'python /opt/airflow/plugins/sentiment_analysis_loader.py'
    - Validate Data Load in PostgreSQL 'psql -h postgres -U airflow -d data_warehouse'

