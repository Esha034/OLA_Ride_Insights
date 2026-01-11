# 🚖 OLA Ride Insights – End-to-End Data Analytics Project

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

---

## 📌 Project Overview
The rapid growth of ride-sharing platforms has generated massive volumes of operational data.  
This project focuses on analyzing **OLA ride-sharing data** to extract **actionable business insights** that can improve operational efficiency, customer satisfaction, and revenue optimization.

The project follows an **end-to-end data analytics workflow**, starting from raw data cleaning and SQL-based analysis to advanced visualization using **Power BI** and deployment of insights through an **interactive Streamlit web application**.

---

##  Business Objectives
1. Identify **ride demand patterns** and booking trends
2. Analyze **revenue distribution and payment behavior**
3.  Understand **cancellation reasons** from customers and drivers.
4.  Evaluate **driver and customer ratings**.
5.  Enable **data-driven decision making** through interactive dashboards

---

##  Tech Stack
- **Python** – Data pre-processing & EDA.
- **PostgreSQL** – Database Connection and analytics.
- **Power BI** – Business intelligence dashboards
- **Streamlit** – Interactive web application
- **Pandas & SQLAlchemy** – Data handling & DB integration segmentation for targeted strategies  

---

## Dataset Description
The dataset contains **103,024 ride records** with features such as:
- Booking details (ID, status, date)
- Vehicle type and locations
- Ride distance and fare value
- Payment methods
- Cancellation reasons
- Driver and customer ratings

---

## Project Workflow

### 1️⃣ Data Understanding & Exploration
- Loaded and examined dataset structure
- Identified key variables (status, payment, ratings)
- Performed initial Exploratory Data Analysis (EDA)

### 2️⃣ Data Cleaning & Preprocessing
- Handled missing and inconsistent values
- Standardized column formats
- Converted data types for accurate analysis

### 3️⃣ SQL Analysis (PostgreSQL)
- Designed database schema
- Wrote optimized SQL queries to answer business questions
- Validated query outputs against the dataset

### 4️⃣ Power BI Dashboard
- Built **multi-page interactive dashboards**
- Implemented KPIs, charts, slicers, and drill-downs
- Designed views for Overall, Vehicle Type, Revenue, Cancellation, and Ratings analysis

### 5️⃣ Streamlit Application
- Developed a **user-friendly analytics web app**
- Connected PostgreSQL using SQLAlchemy
- Implemented KPIs, filters, and interactive tables
- Enabled real-time exploration of SQL insights

---

## Key Analytics Performed (SQL)
- Successful bookings analysis
- Average ride distance by vehicle type
- Customer and driver cancellation counts
- Top customers by rides and revenue
- Revenue analysis by vehicle and payment method
- Driver and customer rating distribution
- Incomplete rides with reasons

---

## Power BI Dashboard Pages
- **Overall** – KPIs, booking status, ride volume trends
- **Vehicle Type** – Distance, revenue, and performance comparison
- **Revenue** – Payment methods, top customers, daily trends
- **Cancellation** – Customer vs driver cancellation reasons
- **Ratings** – Driver and customer satisfaction analysis

---

##  Streamlit Application Features
- Interactive KPI cards
- Dynamic filters (date, vehicle type, booking status)
- SQL-powered analytics
- Clean and intuitive UI for stakeholders

---

## 📁 Project Structure

```bash
OLA_Ride_Insights/
│
├── data/ # Raw & cleaned datasets
├── sql/ # SQL schema & queries
├── powerbi/ # Power BI dashboard file
├── streamlit_app/ # Streamlit application
│ ├── app.py
│ ├── db_connection.py
│ ├── queries.py
│ └── requirements.txt
├── notebooks/ # EDA notebooks
└── README.md

```

---

## ✅ Key Outcomes
- Built a **complete analytics pipeline**
- Delivered **business-ready dashboards**
- Enabled **interactive decision support tools**
- Demonstrated strong skills in **SQL, BI, and Python apps**

---

##  Conclusion
This project showcases the ability to transform raw operational data into **meaningful insights** using a combination of **SQL analytics, data visualization, and web application development**.  
It reflects a real-world, industry-level data analytics workflow.

---

### 👤 Author
**Eshani Banik**  
 Data Analyst




