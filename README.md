# Azure-E-Commerce-Data-Analytics
End-to-End E-Commerce Data Analytics Pipeline using Azure Data Factory, ADLS Gen2, Databricks, Synapse Analytics and Power BI.

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

The complete solution covers:

**Data Ingestion → Data Lake → Data Cleaning → Data Transformation → SQL Analytics → Power BI Reporting**

The objective is to transform raw E-Commerce data into a **clean, business-ready analytical dataset** and generate meaningful business insights through Power BI.

---

# 🏗️ End-to-End Architecture

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


☁️ Azure Resources

The following Azure resources were created for the project:

🔧 Resource	📌 Name	🎯 Purpose
📁 Resource Group	rg-ecommerce-data	Project resource management
🗄️ Storage Account	stecommercedatalake2026	ADLS Gen2 storage
🔷 Data Factory	adf-ecommerce-ingestion	Data ingestion
⚡ Databricks Workspace	dbw-ecommerce-analytics	Data processing
🔵 Synapse Workspace	syn-ecommerce-analytics	SQL analytics
📊 Power BI	E-Commerce Dashboard	Business reporting
