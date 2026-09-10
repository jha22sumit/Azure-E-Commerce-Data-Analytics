# Databricks notebook source
storage_account = "stecommercedatalake2026"

clean_base = f"abfss://clean@{storage_account}.dfs.core.windows.net"
curated_base = f"abfss://curated@{storage_account}.dfs.core.windows.net"

print("CLEAN:", clean_base)
print("CURATED:", curated_base)

# COMMAND ----------



# COMMAND ----------

customers_clean = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(f"{clean_base}/customers/")

display(customers_clean)

# COMMAND ----------

products_clean = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(f"{clean_base}/products/")

display(products_clean)

# COMMAND ----------

orders_clean = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(f"{clean_base}/orders/")

display(orders_clean)

# COMMAND ----------

order_items_clean = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(f"{clean_base}/order-items/")

display(order_items_clean)

# COMMAND ----------

payments_clean = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(f"{clean_base}/payments/")

display(payments_clean)

# COMMAND ----------

print("Customers:", customers_clean.count())
print("Products:", products_clean.count())
print("Orders:", orders_clean.count())
print("Order Items:", order_items_clean.count())
print("Payments:", payments_clean.count())

# COMMAND ----------

order_details = orders_clean.join(
    order_items_clean,
    on="order_id",
    how="inner"
)

display(order_details)

# COMMAND ----------

sales_detail = order_details.join(
    products_clean,
    on="product_id",
    how="inner"
)

display(sales_detail)

# COMMAND ----------

from pyspark.sql.functions import col

sales_detail = sales_detail.withColumn(
    "gross_sales",
    col("quantity") * col("unit_price")
)

display(sales_detail)

# COMMAND ----------

sales_detail = sales_detail.withColumn(
    "discount_amount",
    col("gross_sales") * col("discount") / 100
)

# COMMAND ----------

sales_detail = sales_detail.withColumn(
    "net_sales",
    col("gross_sales") - col("discount_amount")
)

# COMMAND ----------

sales_detail = sales_detail.withColumn(
    "total_cost",
    col("quantity") * col("cost_price")
)

# COMMAND ----------

sales_detail = sales_detail.withColumn(
    "profit",
    col("net_sales") - col("total_cost")
)

# COMMAND ----------

from pyspark.sql.functions import when

sales_detail = sales_detail.withColumn(
    "profit_margin",
    when(
        col("net_sales") != 0,
        (col("profit") / col("net_sales")) * 100
    ).otherwise(0)
)

# COMMAND ----------

sales_detail = sales_detail.join(
    customers_clean,
    on="customer_id",
    how="left"
)

display(sales_detail)

# COMMAND ----------

print(sales_detail.columns)

# COMMAND ----------

display(sales_detail.limit(10))

# COMMAND ----------

print(sales_detail.columns)

# COMMAND ----------

display(
    order_items_clean
    .select("discount")
    .distinct()
    .orderBy("discount")
)

# COMMAND ----------

order_items_clean.select(
    "discount"
).describe().show()

# COMMAND ----------

from pyspark.sql.functions import col, when

sales_detail = sales_detail.withColumn(
    "gross_sales",
    col("quantity") * col("unit_price")
)

sales_detail = sales_detail.withColumn(
    "discount_amount",
    col("gross_sales") * col("discount")
)

sales_detail = sales_detail.withColumn(
    "net_sales",
    col("gross_sales") - col("discount_amount")
)

sales_detail = sales_detail.withColumn(
    "total_cost",
    col("quantity") * col("cost_price")
)

sales_detail = sales_detail.withColumn(
    "profit",
    col("net_sales") - col("total_cost")
)

sales_detail = sales_detail.withColumn(
    "profit_margin",
    when(
        col("net_sales") != 0,
        (col("profit") / col("net_sales")) * 100
    ).otherwise(0)
)

# COMMAND ----------

display(
    sales_detail.select(
        "order_id",
        "product_id",
        "quantity",
        "unit_price",
        "discount",
        "gross_sales",
        "discount_amount",
        "net_sales",
        "total_cost",
        "profit",
        "profit_margin"
    ).limit(20)
)

# COMMAND ----------

display(
    sales_detail.select(
        "gross_sales",
        "discount_amount",
        "net_sales",
        "total_cost",
        "profit",
        "profit_margin"
    ).summary()
)

# COMMAND ----------

display(
    dbutils.fs.ls(
        "abfss://curated@stecommercedatalake2026.dfs.core.windows.net/"
    )
)

# COMMAND ----------

curated_sales = sales_detail.select(
    "order_id",
    "order_item_id",
    "order_date",
    "customer_id",
    "customer_name",
    "customer_segment",
    "city",
    "state",
    "product_id",
    "product_name",
    "category",
    "subcategory",
    "brand",
    "quantity",
    "unit_price",
    "cost_price",
    "discount",
    "gross_sales",
    "discount_amount",
    "net_sales",
    "total_cost",
    "profit",
    "profit_margin",
    "order_status",
    "payment_method",
    "shipping_city",
    "shipping_state"
)

# COMMAND ----------

print("Curated rows:", curated_sales.count())
print("Curated columns:", len(curated_sales.columns))

display(curated_sales.limit(20))

# COMMAND ----------

curated_sales.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(
        f"{curated_base}/sales/"
    )

# COMMAND ----------

display(
    dbutils.fs.ls(
        f"{curated_base}/sales/"
    )
)

# COMMAND ----------

from pyspark.sql.functions import sum, countDistinct, avg, round

sales_summary = curated_sales.agg(
    sum("gross_sales").alias("total_gross_sales"),
    sum("discount_amount").alias("total_discount"),
    sum("net_sales").alias("total_net_sales"),
    sum("total_cost").alias("total_cost"),
    sum("profit").alias("total_profit"),
    countDistinct("order_id").alias("total_orders"),
    countDistinct("customer_id").alias("total_customers"),
    countDistinct("product_id").alias("total_products")
)

sales_summary = sales_summary.select(
    round("total_gross_sales", 2).alias("total_gross_sales"),
    round("total_discount", 2).alias("total_discount"),
    round("total_net_sales", 2).alias("total_net_sales"),
    round("total_cost", 2).alias("total_cost"),
    round("total_profit", 2).alias("total_profit"),
    "total_orders",
    "total_customers",
    "total_products"
)

display(sales_summary)

# COMMAND ----------

from pyspark.sql.functions import year, month, sum, countDistinct, round

monthly_sales = curated_sales.groupBy(
    year("order_date").alias("year"),
    month("order_date").alias("month")
).agg(
    sum("net_sales").alias("total_sales"),
    sum("profit").alias("total_profit"),
    countDistinct("order_id").alias("total_orders")
)

monthly_sales = monthly_sales.select(
    "year",
    "month",
    round("total_sales", 2).alias("total_sales"),
    round("total_profit", 2).alias("total_profit"),
    "total_orders"
).orderBy("year", "month")

display(monthly_sales)

# COMMAND ----------

product_summary = curated_sales.groupBy(
    "product_id",
    "product_name",
    "category",
    "subcategory",
    "brand"
).agg(
    sum("quantity").alias("units_sold"),
    sum("net_sales").alias("total_sales"),
    sum("profit").alias("total_profit"),
    countDistinct("order_id").alias("total_orders")
)

product_summary = product_summary.select(
    "product_id",
    "product_name",
    "category",
    "subcategory",
    "brand",
    "units_sold",
    round("total_sales", 2).alias("total_sales"),
    round("total_profit", 2).alias("total_profit"),
    "total_orders"
).orderBy(
    col("total_sales").desc()
)

display(product_summary)

# COMMAND ----------

customer_summary = curated_sales.groupBy(
    "customer_id",
    "customer_name",
    "customer_segment",
    "city",
    "state"
).agg(
    countDistinct("order_id").alias("total_orders"),
    sum("quantity").alias("total_units"),
    sum("net_sales").alias("total_sales"),
    sum("profit").alias("total_profit")
)

customer_summary = customer_summary.select(
    "customer_id",
    "customer_name",
    "customer_segment",
    "city",
    "state",
    "total_orders",
    "total_units",
    round("total_sales", 2).alias("total_sales"),
    round("total_profit", 2).alias("total_profit")
).orderBy(
    col("total_sales").desc()
)

display(customer_summary)

# COMMAND ----------

category_summary = curated_sales.groupBy(
    "category"
).agg(
    sum("quantity").alias("units_sold"),
    sum("net_sales").alias("total_sales"),
    sum("profit").alias("total_profit"),
    countDistinct("order_id").alias("total_orders")
)

category_summary = category_summary.select(
    "category",
    "units_sold",
    round("total_sales", 2).alias("total_sales"),
    round("total_profit", 2).alias("total_profit"),
    "total_orders"
).orderBy(
    col("total_sales").desc()
)

display(category_summary)

# COMMAND ----------

# Write Sales Summary
sales_summary.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(f"{curated_base}/sales_summary/")

# Write Monthly Sales
monthly_sales.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(f"{curated_base}/monthly_sales/")

# Write Product Summary
product_summary.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(f"{curated_base}/product_summary/")

# Write Customer Summary
customer_summary.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(f"{curated_base}/customer_summary/")

# Write Category Summary
category_summary.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(f"{curated_base}/category_summary/")

print("All aggregate datasets written successfully.")

# COMMAND ----------

display(
    dbutils.fs.ls(curated_base)
)

# COMMAND ----------

display(
    dbutils.fs.ls(f"{curated_base}/sales/")
)

display(
    dbutils.fs.ls(f"{curated_base}/sales_summary/")
)

display(
    dbutils.fs.ls(f"{curated_base}/monthly_sales/")
)

display(
    dbutils.fs.ls(f"{curated_base}/product_summary/")
)

display(
    dbutils.fs.ls(f"{curated_base}/customer_summary/")
)

display(
    dbutils.fs.ls(f"{curated_base}/category_summary/")
)

# COMMAND ----------

print("Sales:", curated_sales.count())
print("Sales Summary:", sales_summary.count())
print("Monthly Sales:", monthly_sales.count())
print("Product Summary:", product_summary.count())
print("Customer Summary:", customer_summary.count())
print("Category Summary:", category_summary.count())

# COMMAND ----------

dbutils.fs.rm(
    "abfss://clean@stecommercedatalake2026.dfs.core.windows.net/test/",
    True
)

# COMMAND ----------

display(
    dbutils.fs.ls(
        "abfss://clean@stecommercedatalake2026.dfs.core.windows.net/"
    )
)