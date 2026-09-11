CREATE DATABASE ecommerce_analytics;
CREATE OR ALTER VIEW dbo.vw_sales_summary
AS
SELECT
    total_gross_sales,
    total_discount,
    total_net_sales,
    total_cost,
    total_profit,
    total_orders,
    total_customers,
    total_products
FROM OPENROWSET(
    BULK 'https://stecommercedatalake2026.dfs.core.windows.net/curated/sales_summary/',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS rows;


SELECT *
FROM dbo.vw_sales_summary;


CREATE OR ALTER VIEW dbo.vw_monthly_sales
AS
SELECT
    year,
    month,
    total_sales,
    total_profit,
    total_orders
FROM OPENROWSET(
    BULK 'https://stecommercedatalake2026.dfs.core.windows.net/curated/monthly_sales/',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS rows;


SELECT *
FROM dbo.vw_monthly_sales
ORDER BY year, month;


CREATE OR ALTER VIEW dbo.vw_product_summary
AS
SELECT
    product_id,
    product_name,
    category,
    subcategory,
    brand,
    units_sold,
    total_sales,
    total_profit,
    total_orders
FROM OPENROWSET(
    BULK 'https://stecommercedatalake2026.dfs.core.windows.net/curated/product_summary/',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS rows;

SELECT TOP 20 *
FROM dbo.vw_product_summary
ORDER BY total_sales DESC;



CREATE OR ALTER VIEW dbo.vw_customer_summary
AS
SELECT
    customer_id,
    customer_name,
    customer_segment,
    city,
    state,
    total_orders,
    total_units,
    total_sales,
    total_profit
FROM OPENROWSET(
    BULK 'https://stecommercedatalake2026.dfs.core.windows.net/curated/customer_summary/',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS rows;


SELECT TOP 20 *
FROM dbo.vw_customer_summary
ORDER BY total_sales DESC;


CREATE OR ALTER VIEW dbo.vw_category_summary
AS
SELECT
    category,
    units_sold,
    total_sales,
    total_profit,
    total_orders
FROM OPENROWSET(
    BULK 'https://stecommercedatalake2026.dfs.core.windows.net/curated/category_summary/',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS rows;

SELECT *
FROM dbo.vw_category_summary
ORDER BY total_sales DESC;


CREATE OR ALTER VIEW dbo.vw_sales
AS
SELECT
    order_id,
    order_item_id,
    order_date,
    customer_id,
    customer_name,
    customer_segment,
    city,
    state,
    product_id,
    product_name,
    category,
    subcategory,
    brand,
    quantity,
    unit_price,
    cost_price,
    discount,
    gross_sales,
    discount_amount,
    net_sales,
    total_cost,
    profit,
    profit_margin,
    order_status,
    payment_method,
    shipping_city,
    shipping_state
FROM OPENROWSET(
    BULK 'https://stecommercedatalake2026.dfs.core.windows.net/curated/sales/',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS rows;


SELECT TOP 20 *
FROM dbo.vw_sales;




SELECT * FROM dbo.vw_sales_summary;

SELECT TOP 10 * 
FROM dbo.vw_monthly_sales
ORDER BY year, month;

SELECT TOP 10 *
FROM dbo.vw_product_summary
ORDER BY total_sales DESC;

SELECT TOP 10 *
FROM dbo.vw_customer_summary
ORDER BY total_sales DESC;

SELECT *
FROM dbo.vw_category_summary
ORDER BY total_sales DESC;

SELECT TOP 10 *
FROM dbo.vw_sales;