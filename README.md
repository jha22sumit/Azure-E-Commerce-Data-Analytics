# 🛒 Azure E-Commerce Data Analytics

<p align="center">
  <img src="https://img.shields.io/badge/Azure-Cloud-0078D4?logo=microsoftazure&logoColor=white" />
  <img src="https://img.shields.io/badge/ADF-Data%20Ingestion-0078D4?logo=microsoftazure&logoColor=white" />
  <img src="https://img.shields.io/badge/ADLS%20Gen2-Data%20Lake-0078D4?logo=microsoftazure&logoColor=white" />
  <img src="https://img.shields.io/badge/Databricks-PySpark-FF3621?logo=databricks&logoColor=white" />
  <img src="https://img.shields.io/badge/Synapse-SQL-0078D4?logo=microsoftazure&logoColor=white" />
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black" />
</p>

---

# 📌 Project Overview

This project demonstrates an **end-to-end E-Commerce Data Analytics solution** built using Microsoft Azure.

The project processes five major E-Commerce datasets:

- 👥 Customers
- 📦 Products
- 🛒 Orders
- 🧾 Order Items
- 💳 Payments

The project follows an end-to-end cloud data analytics architecture where raw E-Commerce data is ingested, stored, cleaned, transformed, analyzed, and visualized using Azure services.

## 🔄 End-to-End Flow

```text
Source Data
    ↓
Azure Data Factory
    ↓
ADLS Gen2 - RAW Layer
    ↓
Azure Databricks - Data Quality & Cleaning
    ↓
ADLS Gen2 - CLEAN Layer
    ↓
Azure Databricks - Transformation & Business Logic
    ↓
ADLS Gen2 - CURATED Layer
    ↓
Azure Synapse Analytics
    ↓
Power BI Dashboard
    ↓
Business Insights
```

---

# ⭐ Project Highlights

- ☁️ Built an end-to-end Azure Data Analytics pipeline
- 🔷 Used Azure Data Factory for data ingestion
- 🗄️ Implemented a layered Data Lake architecture
- 🥉 RAW Layer for ingested source data
- 🥈 CLEAN Layer for validated and cleaned data
- 🥇 CURATED Layer for business-ready analytical data
- ⚡ Performed data quality checks using Azure Databricks and PySpark
- 🧹 Removed duplicates and validated data
- 🔗 Joined multiple E-Commerce datasets
- 🧮 Created business metrics including Gross Sales, Net Sales, Profit, and Profit Margin
- 🔵 Used Azure Synapse Analytics as the SQL analytics layer
- 📊 Built an interactive Power BI dashboard
- 💡 Generated business insights from E-Commerce data

---

# 🏗️ End-to-End Architecture

![E-Commerce Architecture](https://github.com/jha22sumit/Azure-E-Commerce-Data-Analytics/blob/main/01.%20ARCHITECTURE/architecture%20flow%20of%20e-commerce%20project.png)

---

# ☁️ Azure Services Used

| Service | Purpose |
|---|---|
| 🔷 Azure Data Factory | Data ingestion and orchestration |
| 🗄️ Azure Data Lake Storage Gen2 | Centralized data storage |
| ⚡ Azure Databricks | Data quality, cleaning and transformation |
| 🔵 Azure Synapse Analytics | SQL analytics |
| 📊 Power BI | Data visualization and reporting |

---

# 📂 Source Datasets

The project uses five E-Commerce datasets.

| Dataset | Description | Key Columns |
|---|---|---|
| 👥 Customers | Customer information | customer_id, customer_name, city, state, customer_segment |
| 📦 Products | Product information | product_id, product_name, category, brand, unit_price, cost_price |
| 🛒 Orders | Order-level information | order_id, customer_id, order_date, order_status |
| 🧾 Order Items | Product-level order details | order_item_id, order_id, product_id, quantity, discount |
| 💳 Payments | Payment information | payment_id, order_id, payment_date, payment_status, payment_amount |

---

# 🚀 STEP 1 — Create Azure Storage Account

The first step was to create an Azure Storage Account with **Hierarchical Namespace enabled** to use Azure Data Lake Storage Gen2.

## 🗄️ Storage Account

```text
stecommercedatalake2026
```

Azure Data Lake Storage Gen2 was used as the centralized storage platform for the project.

The project follows a layered data architecture.

```text
SOURCE
   ↓
RAW
   ↓
CLEAN
   ↓
CURATED
```

---

## 📁 Storage Containers

The following containers were created:

```text
source
raw
clean
curated
```

---

## 📂 SOURCE Layer

The original E-Commerce datasets were stored in the Source layer.

```text
source/
│
├── customers/
├── products/
├── orders/
├── order-items/
└── payments/
```

### 📌 Purpose

- Store original source data
- Maintain source datasets
- Provide input for data ingestion

---

## 🥉 RAW Layer

The RAW layer stores the ingested data without major transformation.

```text
raw/
│
├── customers/
├── products/
├── orders/
├── order-items/
└── payments/
```

### 📌 Purpose

- Preserve ingested data
- Maintain original records
- Provide input for data processing

---

## 🥈 CLEAN Layer

The CLEAN layer stores validated and cleaned datasets.

```text
clean/
│
├── customers/
├── products/
├── orders/
├── order-items/
└── payments/
```

### 📌 Purpose

- Remove duplicate records
- Check NULL values
- Validate data types
- Clean text fields
- Validate important business columns

---

## 🥇 CURATED Layer

The CURATED layer contains business-ready datasets created after transformation.

```text
curated/
│
├── sales/
├── sales_summary/
├── monthly_sales/
├── product_summary/
├── customer_summary/
└── category_summary/
```

The curated datasets are used for analytics and reporting.

---

# 🚀 STEP 2 — Upload E-Commerce Source Data

The five E-Commerce datasets were uploaded to the Azure Data Lake Storage Gen2 Source layer.

```text
source/
│
├── customers/
│   └── customers.csv
│
├── products/
│   └── products.csv
│
├── orders/
│   └── orders.csv
│
├── order-items/
│   └── order_items.csv
│
└── payments/
    └── payments.csv
```

The source data was maintained as the original input data.

---

# 🚀 STEP 3 — Azure Data Factory

Azure Data Factory was used for data ingestion and orchestration.

Five pipelines were created to ingest the five E-Commerce datasets.

## 🔷 ADF Pipelines

```text
pl_ingest_customers
pl_ingest_products
pl_ingest_orders
pl_ingest_order_items
pl_ingest_payments
```

Each pipeline uses a **Copy Data activity**.

## 🔄 Pipeline Flow

```text
SOURCE Layer
     ↓
Copy Data Activity
     ↓
RAW Layer
```

The Copy Data activity was configured to preserve the folder structure during ingestion.

---

## 📸 Azure Data Factory Pipeline Run Success

![ADF Pipeline Run Success](https://github.com/jha22sumit/Azure-E-Commerce-Data-Analytics/blob/main/03.Azure%20Data%20Factory/ADF_Pipline_Run_Success_screenshot.PNG)

---

# 🚀 STEP 4 — Azure Databricks Setup

Azure Databricks was used for:

- ⚡ Data Quality Checks
- 🧹 Data Cleaning
- 🔄 Data Transformation
- 🔗 Dataset Joins
- 🧮 Business Calculations
- 💎 Curated Dataset Creation

## ⚡ Databricks Workspace

```text
dbw-ecommerce-analytics
```

PySpark was used for data processing and transformation.

---

# 📓 Databricks Notebooks

Two main notebooks were used.

```text
01_Data_Quality_Cleaning

02_ECommerce_Transformation
```

---

# 🚀 STEP 5 — Data Quality and Cleaning

The RAW datasets were loaded into Azure Databricks.

Data quality checks and cleaning operations were performed using PySpark before storing the cleaned datasets in the CLEAN layer.

## 🔍 Data Quality Checks

| Data Quality Check | Purpose |
|---|---|
| 🔍 Duplicate Check | Identify and remove duplicate records |
| ❌ NULL Check | Identify missing values in important columns |
| 📅 Date Validation | Validate and convert date columns |
| 🔢 Numeric Validation | Validate quantity, prices, discount and payment values |
| ✂️ Text Cleaning | Remove unnecessary spaces and clean text fields |

---

## 🔄 Data Cleaning Flow

```text
RAW DATA
    ↓
Duplicate Check
    ↓
NULL Value Check
    ↓
Data Type Validation
    ↓
Date Validation
    ↓
Text Cleaning
    ↓
CLEAN DATA
```

---

## 🧹 Customers Data Cleaning

The following checks were performed:

- Remove duplicate records
- Validate customer_id
- Check NULL values
- Clean customer-related text fields

Output:

```text
clean/customers/
```

---

## 🧹 Products Data Cleaning

The following checks were performed:

- Remove duplicate records
- Validate product_id
- Validate unit_price
- Validate cost_price
- Check NULL values
- Clean product-related text fields

Output:

```text
clean/products/
```

---

## 🧹 Orders Data Cleaning

The following checks were performed:

- Remove duplicate records
- Validate order_id
- Validate customer_id
- Validate order_date
- Clean order_status
- Clean payment_method
- Clean shipping_city
- Clean shipping_state

Output:

```text
clean/orders/
```

---

## 🧹 Order Items Data Cleaning

The following checks were performed:

- Remove duplicate records
- Validate order_item_id
- Validate order_id
- Validate product_id
- Validate quantity
- Validate discount

The Order Items dataset contains:

```text
order_item_id
order_id
product_id
quantity
discount
```

Output:

```text
clean/order-items/
```

---

## 🧹 Payments Data Cleaning

The following checks were performed:

- Remove duplicate records
- Validate payment_id
- Validate order_id
- Validate payment_date
- Validate payment_amount
- Clean payment_status

The Payments dataset contains:

```text
payment_id
order_id
payment_date
payment_status
payment_amount
```

Output:

```text
clean/payments/
```

---

# 🚀 STEP 6 — Data Transformation and Business Logic

After data cleaning, the datasets were loaded from the CLEAN layer.

Multiple datasets were joined to create a unified E-Commerce analytical dataset.

## 🔗 Dataset Join Flow

```text
👥 Customers
       │
       │ customer_id
       ▼
🛒 Orders
       │
       │ order_id
       ▼
🧾 Order Items
       │
       │ product_id
       ▼
📦 Products
```

### 🔗 Join Keys

Customer information was connected using:

```text
customer_id
```

Orders and Order Items were connected using:

```text
order_id
```

Products were connected using:

```text
product_id
```

---

# 🧮 Business Calculations

The following business metrics were created during the transformation process.

## 💰 Gross Sales

```text
Gross Sales = Quantity × Unit Price
```

---

## 🏷️ Discount Amount

```text
Discount Amount = Gross Sales × Discount
```

The discount values were stored as decimals.

```text
0
0.05
0.10
0.15
0.20
```

---

## 💵 Net Sales

```text
Net Sales = Gross Sales - Discount Amount
```

---

## 💸 Total Cost

```text
Total Cost = Quantity × Cost Price
```

---

## 📈 Profit

```text
Profit = Net Sales - Total Cost
```

---

## 📊 Profit Margin

```text
Profit Margin = Profit / Net Sales
```

---

# 📊 Final Analytical Dataset

The transformation process created a business-ready E-Commerce dataset containing information such as:

```text
customer_id
product_id
order_id
order_date
order_status
payment_method
shipping_city
shipping_state

order_item_id
quantity
discount

product_name
category
subcategory
brand
unit_price
cost_price

gross_sales
discount_amount
net_sales
total_cost
profit
profit_margin

customer_name
email
city
state
signup_date
customer_segment
```

---

# 💎 Curated Analytical Datasets

Business-ready datasets were created in the CURATED layer for analytics and reporting.

```text
curated/
│
├── sales/
├── sales_summary/
├── monthly_sales/
├── product_summary/
├── customer_summary/
└── category_summary/
```

## 📊 Sales Summary

Used for overall business KPIs.

Examples:

```text
Total Sales
Total Profit
Total Orders
Total Customers
```

---

## 📅 Monthly Sales

Used for time-based analysis.

Examples:

```text
Monthly Sales
Monthly Profit
Monthly Orders
```

---

## 📦 Product Summary

Used for product performance analysis.

Examples:

```text
Product Name
Category
Total Sales
Total Profit
Quantity Sold
```

---

## 👥 Customer Summary

Used for customer performance analysis.

Examples:

```text
Customer Name
Customer Segment
Total Sales
Total Profit
Total Orders
```

---

## 🏷️ Category Summary

Used for category-level analysis.

Examples:

```text
Category
Total Sales
Total Profit
Total Orders
```

---

# 🚀 STEP 7 — Azure Synapse Analytics

Azure Synapse Analytics was used as the SQL analytics layer.

The CURATED datasets were accessed and queried using SQL.

Azure Synapse was used to:

- 🗃️ Query curated datasets
- 🔍 Validate transformed data
- 📊 Analyze sales data
- 📈 Analyze business metrics
- 💡 Support analytical reporting

## 🔵 Synapse Data Flow

```text
💎 ADLS GEN2 - CURATED LAYER
              ↓
🔵 AZURE SYNAPSE ANALYTICS
              ↓
🗃️ SQL QUERIES
              ↓
📊 POWER BI
```

---

# 📊 Power BI Dashboard

The final business-ready E-Commerce data was visualized using Power BI.

The dashboard provides an interactive view of sales, profit, customers, products, and business performance.

![E-Commerce Power BI Dashboard](https://github.com/jha22sumit/Azure-E-Commerce-Data-Analytics/blob/main/06.POWERBI/E-Commerce_Sales_analytics_dashboard_screenshot.PNG)

---

# 🎯 Dashboard KPIs

The dashboard includes important business performance indicators.

- 💰 Total Sales
- 📈 Total Profit
- 🛒 Total Orders
- 👥 Total Customers
- 🧾 Average Order Value
- 📊 Profit Margin

---

# 📈 Dashboard Visuals

| Visual | Business Analysis |
|---|---|
| 📈 Monthly Sales Trend | Analyze sales performance over time |
| 💰 Sales by Category | Compare category performance |
| 🏆 Top 5 Products by Sales | Identify the highest revenue-generating products |
| 👥 Top Customers by Sales | Identify high-value customers |
| 📍 Sales by State | Analyze geographical sales performance |
| 📦 Order Status Analysis | Monitor order distribution |
| 📋 Detailed Table | Analyze detailed E-Commerce transactions |

---

# 🎛️ Dashboard Filters

Interactive slicers can be used to analyze the dashboard based on:

- 📅 Year / Date
- 🏷️ Category
- 👥 Customer Segment
- 📍 State

---

# 💡 Business Insights

The Power BI dashboard helps generate valuable insights from E-Commerce data.

## 💰 Sales Performance

Analyze:

- Total Sales
- Sales trends
- Monthly performance
- Category-wise sales

### Business Question

```text
How is the overall business performing?
```

---

## 📈 Profitability Analysis

Analyze:

- Total Profit
- Profit Margin
- Profitable products
- Profitable categories

### Business Question

```text
Are high sales generating high profits?
```

---

## 🏆 Product Performance

The Top 5 Products visual helps identify:

- Best-selling products
- High-revenue products
- Products contributing significantly to sales

### Business Question

```text
Which products generate the highest revenue?
```

---

## 👥 Customer Performance

Customer analysis helps identify:

- High-value customers
- Customers generating high sales
- Customer contribution to revenue

### Business Question

```text
Which customers contribute the most to revenue?
```

---

## 🏷️ Category Performance

Category analysis helps identify:

- High-performing categories
- Low-performing categories
- Categories contributing the most revenue

### Business Question

```text
Which product categories perform the best?
```

---

## 📍 Geographic Performance

Sales by State helps analyze:

- High-performing states
- Low-performing states
- Regional sales performance

### Business Question

```text
Which states generate the highest sales?
```

---

## 📅 Sales Trends

Monthly analysis helps identify:

- Sales growth
- Sales decline
- Monthly trends
- Business performance over time

### Business Question

```text
How does business performance change over time?
```

---

# 🎯 Key Business Questions Answered

The dashboard helps answer the following questions:

```text
💰 What are the total sales?

📈 What is the total profit?

📊 What is the profit margin?

🛒 How many orders were placed?

👥 How many customers made purchases?

📅 How are sales changing over time?

🏆 Which products generate the highest sales?

👥 Which customers generate the highest revenue?

🏷️ Which categories perform best?

📍 Which states generate the highest sales?

📦 What is the order status distribution?
```

---

# 🏆 Project Results

✔ Successfully ingested five E-Commerce datasets

✔ Implemented a layered Data Lake architecture

✔ Created SOURCE, RAW, CLEAN, and CURATED data layers

✔ Performed data quality checks using PySpark

✔ Cleaned and validated E-Commerce datasets

✔ Joined multiple datasets to create an analytical dataset

✔ Created business metrics including Sales and Profit

✔ Created curated datasets for analytics

✔ Used Azure Synapse Analytics for SQL analysis

✔ Built an interactive Power BI dashboard

✔ Generated business insights for decision-making

---

# 🛠️ Technology Stack

| Technology | Usage |
|---|---|
| ☁️ Microsoft Azure | Cloud Platform |
| 🔷 Azure Data Factory | Data Ingestion |
| 🗄️ ADLS Gen2 | Data Storage |
| ⚡ Azure Databricks | Data Processing |
| 🔥 PySpark | Data Transformation |
| 🔵 Azure Synapse Analytics | SQL Analytics |
| 🗃️ SQL | Data Analysis |
| 📊 Power BI | Data Visualization |
| 🧮 DAX | Business Calculations |
| 🐙 GitHub | Version Control |

---

# 🎯 Key Skills Demonstrated

This project demonstrates practical knowledge of:

- ☁️ Microsoft Azure
- 🔷 Azure Data Factory
- 🗄️ Azure Data Lake Storage Gen2
- ⚡ Azure Databricks
- 🔥 PySpark
- 🔄 ETL / ELT Concepts
- 📥 Data Ingestion
- 🧹 Data Cleaning
- 🔍 Data Quality
- 🔗 Dataset Joins
- 🔄 Data Transformation
- 🧮 Business Logic
- 💎 Data Lake Architecture
- 🗃️ SQL
- 🔵 Azure Synapse Analytics
- 📊 Power BI
- 🧮 DAX
- 📈 KPI Reporting
- 💡 Business Analytics
- 📊 Data Visualization

---


# 📁 Repository Structure

```text
Azure-E-Commerce-Data-Analytics/
│
├── 01. ARCHITECTURE/
│   └── architecture flow of e-commerce project.png
│
├── 02.ADLS GEN 2/
│   └── ADLS Gen2 Storage Screenshots
│
├── 03.Azure Data Factory/
│   ├── ADF Pipeline Screenshots
│   └── ADF_Pipline_Run_Success_screenshot.PNG
│
├── 04.DATABRICKS/
│   ├── 01_Data_Quality_Cleaning
│   └── 02_ECommerce_Transformation
│
├── 05.SYNAPSE/
│   └── Synapse SQL Scripts and Screenshots
│
├── 06.POWERBI/
│   ├── Azure_E-Commerce_end_to_end_Powerbi_project.pbix
│   ├── Azure_E-Commerce_schema_&Data_tables_screenshot.PNG
│   ├── E-Commerce_Sales_analytics_dashboard_screenshot.PNG
│   └── sample files/
│
├── 07.DATASET/
│   ├── customers
│   ├── products
│   ├── orders
│   ├── order-items
│   └── payments
│
└── README.md

```

---
# 🚀 Final Project Flow
---
```text
                    🛒 SOURCE DATA
                         │
                         ▼
                🔷 AZURE DATA FACTORY
                         │
                         ▼
                   🗄️ ADLS GEN2
                    RAW LAYER
                         │
                         ▼
                 ⚡ AZURE DATABRICKS
              DATA QUALITY & CLEANING
                         │
                         ▼
                   🧹 ADLS GEN2
                   CLEAN LAYER
                         │
                         ▼
                 ⚡ AZURE DATABRICKS
            TRANSFORMATION & BUSINESS LOGIC
                         │
                         ▼
                   💎 ADLS GEN2
                  CURATED LAYER
                         │
                         ▼
               🔵 AZURE SYNAPSE ANALYTICS
                    SQL ANALYTICS
                         │
                         ▼
                    📊 POWER BI
                DASHBOARD & KPIs
                         │
                         ▼
                   💡 BUSINESS INSIGHTS
```

---

# 🏁 Project Outcome

This project demonstrates a complete **cloud-based E-Commerce Data Analytics pipeline**.

The solution transforms raw E-Commerce data into clean, structured, and business-ready datasets.

The project covers:

- 📥 Data Ingestion
- 🗄️ Data Lake Storage
- 🥉 RAW Data Layer
- 🧹 Data Cleaning
- 🔍 Data Quality Checks
- 🥈 CLEAN Data Layer
- 🔄 Data Transformation
- 🔗 Dataset Joins
- 🧮 Business Calculations
- 💎 CURATED Data Creation
- 🗃️ SQL Analytics
- 📊 Power BI Reporting
- 📈 KPI Reporting
- 💡 Business Insights

---

# 👤 Author

## Sumit Kumar

**Data Analyst | SQL | Power BI | Azure | Data Analytics**

🐙 GitHub: https://github.com/jha22sumit

💼 LinkedIn: https://www.linkedin.com/in/sumit-kumar-148566220/

---

⭐ If you find this project useful, please consider giving the repository a star!
