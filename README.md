
# 🛒 Azure E-Commerce Data Analytics

<p align="center">
  <img src="https://img.shields.io/badge/Azure-Cloud-blue?logo=microsoftazure" />
  <img src="https://img.shields.io/badge/ADF-Data%20Ingestion-blue?logo=microsoftazure" />
  <img src="https://img.shields.io/badge/ADLS%20Gen2-Data%20Lake-blue?logo=microsoftazure" />
  <img src="https://img.shields.io/badge/Databricks-PySpark-orange?logo=databricks" />
  <img src="https://img.shields.io/badge/Synapse-SQL-blue?logo=microsoftazure" />
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi" />
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

---

# 🏗️ End-to-End Architecture

![image alt](https://github.com/jha22sumit/Azure-E-Commerce-Data-Analytics/blob/main/01.%20ARCHITECTURE/architecture%20flow%20of%20e-commerce%20project.png)  


```text
                         🛒 E-COMMERCE SOURCE DATA
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
          👥 Customers        📦 Products         🛒 Orders
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  │
                           🧾 Order Items
                                  │
                            💳 Payments
                                  │
                                  ▼
                    🔷 AZURE DATA FACTORY
                       Data Ingestion
                                  │
                                  ▼
                   🗄️ ADLS GEN2 - RAW
                                  │
                                  ▼
                    ⚡ AZURE DATABRICKS
                   Data Quality & Cleaning
                                  │
                                  ▼
                  🧹 ADLS GEN2 - CLEAN
                                  │
                                  ▼
                    ⚡ AZURE DATABRICKS
                Business Logic & Transformation
                                  │
                                  ▼
                 💎 ADLS GEN2 - CURATED
                                  │
                                  ▼
                  🔵 AZURE SYNAPSE ANALYTICS
                     SQL Analytics Layer
                                  │
                                  ▼
                         📊 POWER BI
                    Interactive Dashboard

---



## ☁️ Azure Services Used

| Service | Purpose |
|---|---|
| 🔷 Azure Data Factory | Data ingestion and orchestration |
| 🗄️ Azure Data Lake Storage Gen2 | Centralized data storage |
| ⚡ Azure Databricks | Data cleaning and transformation |
| 🔵 Azure Synapse Analytics | SQL analytics |
| 📊 Power BI | Data visualization and reporting |

---

# 📂 Source Datasets

The project uses five E-Commerce datasets.

## 👥 Customers

Customer-related information.

```text
customer_id
customer_name
email
city
state
signup_date
customer_segment
```

---

## 📦 Products

Product-related information.

```text
product_id
product_name
category
subcategory
brand
unit_price
cost_price
```

---

## 🛒 Orders

Order-level information.

```text
order_id
customer_id
order_date
order_status
payment_method
shipping_city
shipping_state
```

---

## 🧾 Order Items

Product-level order information.

```text
order_item_id
order_id
product_id
quantity
discount
```

---

## 💳 Payments

Payment-related information.

```text
payment_id
order_id
payment_date
payment_status
payment_amount
```

---

# 🚀 STEP 1 — Create Azure Storage Account

The first step was to create an Azure Storage Account with **Hierarchical Namespace enabled** to use Azure Data Lake Storage Gen2.

## 🗄️ Storage Account

```text
stecommercedatalake2026
```

Azure Data Lake Storage Gen2 was used as the central storage platform for the project.

The project follows a layered data architecture:

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

The following containers were used:

```text
source
raw
clean
curated
```

---

## 📂 Source Layer

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

---

## 🥉 RAW Layer

The RAW layer stores the original ingested data.

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

- Preserve raw data
- Store original records
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

- Remove duplicates
- Validate records
- Handle missing values
- Clean text fields
- Validate data types

---

## 🥇 CURATED Layer

The CURATED layer contains business-ready datasets.

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

The five source datasets were uploaded to the Azure Data Lake Storage Gen2 Source layer.

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

## 🔷 ADF Pipelines

Five pipelines were created for the five datasets:

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
Source Data
     ↓
Copy Data Activity
     ↓
RAW Layer
```

---

## 📸 Azure Data Factory Screenshot

![image alt](https://github.com/jha22sumit/Azure-E-Commerce-Data-Analytics/blob/main/03.Azure%20Data%20Factory/ADF_Pipline_Run_Success_screenshot.PNG)  


---

# 🚀 STEP 4 — Azure Databricks Setup

Azure Databricks was used for:

- ⚡ Data Quality Checks
- 🧹 Data Cleaning
- 🔄 Data Transformation
- 🔗 Dataset Joins
- 🧮 Business Calculations

## ⚡ Databricks Workspace

```text
dbw-ecommerce-analytics
```

PySpark was used for data processing.

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

The following data quality operations were performed.

## 🔍 Duplicate Check

Duplicate records were checked and removed where required.

```python
df = df.dropDuplicates()
```

---

## ❌ NULL Value Check

Important columns were checked for NULL values.


---

## 📅 Date Validation

Date fields were converted into appropriate date format.



```

---

## 🔢 Numeric Validation

Numeric fields were validated
```


## ✂️ Text Cleaning

Text fields were cleaned and trimmed where required.


# 🧹 Customers Data Cleaning

The Customers dataset was processed using the following steps:

- Remove duplicate records
- Validate customer_id
- Check NULL values
- Clean text fields
- Validate customer information

Output:

```text
clean/customers/
```

---

# 🧹 Products Data Cleaning

The Products dataset was processed using:

- Remove duplicate records
- Validate product_id
- Validate unit_price
- Validate cost_price
- Check NULL values
- Clean category
- Clean brand

Output:

```text
clean/products/
```

---

# 🧹 Orders Data Cleaning

The Orders dataset was processed using:

- Remove duplicate records
- Validate order_id
- Validate customer_id
- Convert order_date
- Clean order_status
- Clean payment_method
- Clean shipping_city
- Clean shipping_state

Output:

```text
clean/orders/
```

---

# 🧹 Order Items Data Cleaning

The Order Items dataset was processed using:

- Remove duplicate records
- Validate order_item_id
- Validate order_id
- Validate product_id
- Validate quantity
- Validate discount
- Remove invalid records

Output:

```text
clean/order-items/
```

---

# 🧹 Payments Data Cleaning

The Payments dataset was processed using:

- Remove duplicate records
- Validate payment_id
- Validate order_id
- Convert payment_date
- Validate payment_amount
- Clean payment_status

Output:

```text
clean/payments/
```

---

# 🚀 STEP 6 — Data Transformation and Business Logic

After data cleaning, all datasets were loaded from the CLEAN layer.

The datasets were joined to create a unified E-Commerce analytical dataset.

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



# 🚀 STEP 7 — Azure Synapse Analytics

Azure Synapse Analytics was used as the SQL analytics layer.

The CURATED datasets were accessed and queried using SQL.

## 🔵 Data Flow

```text
💎 CURATED DATA
       ↓
🔵 AZURE SYNAPSE ANALYTICS
       ↓
🗃️ SQL QUERIES / VIEWS
       ↓
📊 POWER BI
```

Synapse provides a structured analytics layer between the Data Lake and Power BI.

---

# 📊 Power BI Dashboard

The final business-ready data was visualized using Power BI.

![image alt](https://github.com/jha22sumit/Azure-Retail-Sales-Analytics/blob/main/01.ARCHITECTURE/Architecture%20screenshot.png)  
)

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
- 🗃️ SQL
- 🔵 Azure Synapse Analytics
- 📊 Power BI
- 🧮 DAX
- 📈 KPI Reporting
- 📊 Data Visualization

---

# 📁 Repository Structure

```text
Azure-ECommerce-Data-Analytics/
│
├── README.md
│
├── Architecture/
│   └── ECommerce_Architecture.png
│
├── ADF/
│   ├── ADF_All_Pipelines.png
│   ├── ADF_Copy_Activity.png
│   └── ADF_Pipeline_Run_Success.png
│
├── Databricks/
│   ├── 01_Data_Quality_Cleaning.py
│   └── 02_ECommerce_Transformation.py
│
├── Synapse/
│   └── Synapse_SQL_Views.sql
│
├── PowerBI/
│   ├── ECommerce_Dashboard.pbix
│   └── ECommerce_Dashboard.png
│
└── Screenshots/
    ├── ADLS_RAW_Layer.png
    ├── ADLS_CLEAN_Layer.png
    ├── ADLS_CURATED_Layer.png
    ├── Databricks_Notebooks.png
    └── Synapse_Views.png
```

---


---

# 💡 Business Insights

The project enables analysis of:

- 💰 Sales Performance
- 📈 Profitability
- 📦 Product Performance
- 🏆 Top Products
- 👥 Customer Performance
- 📍 Geographic Sales
- 📅 Monthly Trends
- 🛒 Order Performance
- 🏷️ Category Performance

---

# 🚀 Final Project Flow

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

The solution transforms raw E-Commerce data into clean and business-ready datasets.

The project covers:

- 📥 Data Ingestion
- 🗄️ Data Lake Storage
- 🧹 Data Cleaning
- 🔍 Data Quality Checks
- 🔄 Data Transformation
- 🔗 Dataset Joins
- 🧮 Business Calculations
- 💎 Curated Data Creation
- 🗃️ SQL Analytics
- 📊 Power BI Reporting
- 💡 Business Insights

---

# 👤 Author

## Sumit Kumar

**Data Analyst | SQL | Power BI | Azure | Data Analytics**

🐙 GitHub:  
https://github.com/jha22sumit

💼 LinkedIn:  
https://www.linkedin.com/in/sumit-kumar-148566220/

---

⭐ If you find this project useful, please consider giving the repository a star!
