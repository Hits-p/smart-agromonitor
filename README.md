🌱 Smart AgroMonitor
📌 Project Description

Smart AgroMonitor is a smart agriculture monitoring system that collects, stores, and visualizes environmental sensor data to support data-driven farming decisions. The system uses a hybrid database architecture, combining relational and time-series databases, to efficiently manage real-time and historical agricultural data.

⚙️ System Architecture

The application follows a Flask-based backend architecture with dual data storage:

PostgreSQL → Structured and persistent storage of sensor readings

InfluxDB → Time-series storage for real-time analytics

Flask → REST API for data ingestion and dashboard rendering

Matplotlib → Server-side data visualization

🚜 Features

Real-time sensor data collection via REST APIs

Storage of agricultural data in PostgreSQL for historical analysis

Time-series storage using InfluxDB for trend monitoring

Dynamic server-generated graphs using Matplotlib

Web-based dashboard using Flask templates

🧪 Parameters Monitored

Temperature

Humidity

Soil Moisture

pH Level

Light Intensity

🛠️ Tech Stack

Backend

Python

Flask

Databases

PostgreSQL

InfluxDB

Visualization

Matplotlib

Tools

Git

VS Code
