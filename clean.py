import pandas as pd
import sqlite3
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
df['Attrition_Flag'] = df['Attrition'].map({'Yes':1,'No':0})

df['AgeGroup'] = pd.cut(df['Age'],
                        bins=[18,25,35,45,60],
                        labels=['18-25','26-35','36-45','46-60'])
df['IncomeGroup'] = pd.cut(df['MonthlyIncome'],
                           bins=[0,5000,10000,20000],
                           labels=['low','medium','high'])
df.drop(columns=['EmployeeCount','EmployeeNumber',
                  'Over18','StandardHours'], inplace=True)
df.to_csv('hr_cleaned.csv', index=False)
print(f"Cleaned data: {df.shape[0]} rows, {df.shape[1]} columns")

#load into sqlite3
conn = sqlite3.connect('hr_analytics.db')
df.to_sql('employees', conn, if_exists='replace', index=False)
print("Loaded into SQLite successfully")

# Overall attrition rate
q1 = pd.read_sql("""
    SELECT
      COUNT(*) AS total_employees,
      SUM(Attrition_Flag) AS total_attrition,
      ROUND(AVG(Attrition_Flag)*100, 2) AS attrition_rate_pct
    FROM employees
""", conn)

# Attrition by Department
q2 = pd.read_sql("""
    SELECT Department,
      COUNT(*) AS headcount,
      ROUND(AVG(Attrition_Flag)*100,2) AS attrition_pct
    FROM employees
    GROUP BY Department
    ORDER BY attrition_pct DESC
""", conn)

# Attrition by JobRole
q3 = pd.read_sql("""
    SELECT JobRole,
      COUNT(*) AS headcount,
      ROUND(AVG(Attrition_Flag)*100,2) AS attrition_pct
    FROM employees
    GROUP BY JobRole
    ORDER BY attrition_pct DESC
    LIMIT 5
""", conn)

# Avg income — stayed vs left
q4 = pd.read_sql("""
    SELECT Attrition,
      ROUND(AVG(MonthlyIncome),0) AS avg_income,
      ROUND(AVG(YearsAtCompany),1) AS avg_tenure
    FROM employees
    GROUP BY Attrition
""", conn)

print(q1, q2, q3, q4, sep='\n\n')
conn.close()