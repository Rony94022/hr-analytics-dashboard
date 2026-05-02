# HR Attrition \& Workforce Analytics Dashboard

An end-to-end HR analytics project analysing employee attrition
across departments, job roles, age groups, and income bands using
Python, SQL, and Power BI.

\---

## Dashboard Preview

!\[HR Dashboard](hr_dashboard.png)

\---

## Tools Used

|Tool|Purpose|
|-|-|
|Python (Pandas)|Data cleaning \& feature engineering|
|SQLite + SQL|Data storage \& querying|
|Power BI + DAX|Dashboard \& visualizations|
|GitHub|Version control|

\---

## Dataset

* Source: IBM HR Analytics Employee Attrition Dataset (Kaggle)
* Size: 1,470 employee records, 35 columns
* Link: https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

\---

## Key Insights

* Overall attrition rate: **16.1%** (237 out of 1,470 employees)
* **Sales department** has the highest attrition rate at 20%+
* **Sales Representatives** are the highest attrition job role at 39%+
* Employees who left earned on average **₹2,000–3,000 less** per month
than those who stayed
* **26–35 age group** has the highest attrition count
* Employees working **OverTime** are significantly more likely to leave

\---

## Project Steps

### 1\. Data Cleaning (Python + Pandas)

* Loaded 1,470 rows from IBM HR dataset
* Created `Attrition\_Flag` column (Yes=1, No=0) for numeric analysis
* Engineered `AgeGroup` and `IncomeGroup` bins for segmentation
* Dropped 4 irrelevant columns (EmployeeCount, EmployeeNumber, etc.)
* Exported cleaned data to `hr\_cleaned.csv`

### 2\. SQL Analysis (SQLite)

* Loaded cleaned data into SQLite database
* Ran GROUP BY queries to find attrition rate by Department and JobRole
* Compared average income and tenure between employees who stayed vs left
* Validated all Python findings independently through SQL

### 3\. Power BI Dashboard

* Built 4 DAX measures: Total Employees, Attrition Count,
Attrition Rate, Avg Monthly Income
* Created 5 visualizations: KPI cards, bar charts, donut chart,
column chart, scatter plot
* Added 3 interactive slicers: Gender, OverTime, AgeGroup

\---

## How to Run

1. Clone this repository
2. Run `clean.py` to clean data and load into SQLite
3. Open `HR Attrition \& Workforce Analytics Dashboard.pbix` in Power BI Desktop to explore dashboard

\---

## Connect

* LinkedIn: linkedin.com/in/rupam-patra-27801224b
* GitHub: github.com/Rony94022

