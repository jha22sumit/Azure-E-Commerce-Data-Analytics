# Databricks notebook source
storage_account = "stecommercedatalake2026"

raw_base = f"abfss://raw@{storage_account}.dfs.core.windows.net"
clean_base = f"abfss://clean@{storage_account}.dfs.core.windows.net"

print("RAW:", raw_base)
print("CLEAN:", clean_base)

# COMMAND ----------

customers_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(f"{raw_base}/customers/customers.csv")
)

display(customers_df)

# COMMAND ----------

customers_df.printSchema()

# COMMAND ----------

print("Customer records:", customers_df.count())

# COMMAND ----------

from pyspark.sql.functions import col, sum, when

customers_df.select(
    [
        sum(when(col(c).isNull(), 1).otherwise(0)).alias(c)
        for c in customers_df.columns
    ]
).show()

# COMMAND ----------

print("Total records:", customers_df.count())
print("Distinct records:", customers_df.distinct().count())

# COMMAND ----------

customers_df.groupBy("customer_id") \
    .count() \
    .filter(col("count") > 1) \
    .show()

# COMMAND ----------

customers_clean = customers_df.dropDuplicates()

# COMMAND ----------

customers_clean = customers_clean.filter(
    col("customer_id").isNotNull()
)

# COMMAND ----------

from pyspark.sql.functions import trim

customers_clean = (
    customers_clean
    .withColumn("customer_name", trim(col("customer_name")))
    .withColumn("email", trim(col("email")))
    .withColumn("city", trim(col("city")))
    .withColumn("state", trim(col("state")))
    .withColumn("customer_segment", trim(col("customer_segment")))
)

# COMMAND ----------

customers_clean = (
    customers_clean
    .fillna({
        "city": "Unknown",
        "state": "Unknown",
        "customer_segment": "Unknown"
    })
)

# COMMAND ----------

print("RAW customers:", customers_df.count())
print("CLEAN customers:", customers_clean.count())

display(customers_clean)

# COMMAND ----------

customers_clean.select(
    [
        sum(when(col(c).isNull(), 1).otherwise(0)).alias(c)
        for c in customers_clean.columns
    ]
).show()

# COMMAND ----------

customers_clean.groupBy("customer_id") \
    .count() \
    .filter(col("count") > 1) \
    .show()

# COMMAND ----------

# DBTITLE 1,Persist cleaned customers
customers_clean.write\
    .mode("overwrite") \
    .option("header", "true") \
    .csv(f"{clean_base}/customers/")

# COMMAND ----------

display(customers_clean)

# COMMAND ----------

print("Clean Customers Rows:", customers_clean.count())

# COMMAND ----------

customers_clean.write \
    .mode("overwrite") \
    .option("header", "true") \
    .option("delimiter", ",") \
    .csv("abfss://clean@stecommercedatalake2026.dfs.core.windows.net/customers/")

# COMMAND ----------

display(
    dbutils.fs.ls(
        "abfss://clean@stecommercedatalake2026.dfs.core.windows.net/customers/"
    )
)

# COMMAND ----------

clean_customers_check = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("abfss://clean@stecommercedatalake2026.dfs.core.windows.net/customers/")

display(clean_customers_check)

# COMMAND ----------

products_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("abfss://raw@stecommercedatalake2026.dfs.core.windows.net/products/products.csv")

display(products_df)

# COMMAND ----------

products_df.printSchema()
print("Original Products Rows:", products_df.count())

display(
    products_df.select([
        sum(col(c).isNull().cast("int")).alias(c)
        for c in products_df.columns
    ])
)

# COMMAND ----------

from pyspark.sql.functions import col, trim

products_clean = products_df \
    .dropDuplicates() \
    .filter(col("product_id").isNotNull()) \
    .filter(col("unit_price").isNotNull()) \
    .filter(col("unit_price") >= 0) \
    .filter(col("cost_price").isNotNull()) \
    .filter(col("cost_price") >= 0) \
    .withColumn("product_name", trim(col("product_name"))) \
    .withColumn("category", trim(col("category"))) \
    .withColumn("subcategory", trim(col("subcategory"))) \
    .withColumn("brand", trim(col("brand")))

# COMMAND ----------

print("Clean Products Rows:", products_clean.count())

display(products_clean)

# COMMAND ----------

products_clean.write \
    .mode("overwrite") \
    .option("header", "true") \
    .option("delimiter", ",") \
    .csv("abfss://clean@stecommercedatalake2026.dfs.core.windows.net/products/")

# COMMAND ----------

display(
    dbutils.fs.ls(
        "abfss://clean@stecommercedatalake2026.dfs.core.windows.net/products/"
    )
)

# COMMAND ----------

orders_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("abfss://raw@stecommercedatalake2026.dfs.core.windows.net/orders/orders.csv")

display(orders_df)

# COMMAND ----------

orders_df.printSchema()

# COMMAND ----------

print(orders_df.columns)
print("Original Orders Rows:", orders_df.count())

# COMMAND ----------

from pyspark.sql.functions import col, sum

display(
    orders_df.select([
        sum(col(c).isNull().cast("int")).alias(c)
        for c in orders_df.columns
    ])
)

# COMMAND ----------

from pyspark.sql.functions import col, trim, to_date

orders_clean = orders_df \
    .dropDuplicates() \
    .filter(col("order_id").isNotNull()) \
    .filter(col("customer_id").isNotNull()) \
    .withColumn("order_date", to_date(col("order_date"))) \
    .filter(col("order_date").isNotNull()) \
    .withColumn("order_status", trim(col("order_status"))) \
    .withColumn("payment_method", trim(col("payment_method"))) \
    .withColumn("shipping_city", trim(col("shipping_city"))) \
    .withColumn("shipping_state", trim(col("shipping_state")))

# COMMAND ----------

print("Original Orders Rows:", orders_df.count())
print("Clean Orders Rows:", orders_clean.count())

display(orders_clean)

# COMMAND ----------

display(
    orders_clean.select([
        sum(col(c).isNull().cast("int")).alias(c)
        for c in orders_clean.columns
    ])
)

# COMMAND ----------

orders_clean.write \
    .mode("overwrite") \
    .option("header", "true") \
    .option("delimiter", ",") \
    .csv("abfss://clean@stecommercedatalake2026.dfs.core.windows.net/orders/")

# COMMAND ----------

display(
    dbutils.fs.ls(
        "abfss://clean@stecommercedatalake2026.dfs.core.windows.net/orders/"
    )
)

# COMMAND ----------

order_items_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("abfss://raw@stecommercedatalake2026.dfs.core.windows.net/order-items/order_items.csv")

display(order_items_df)

# COMMAND ----------

order_items_df.printSchema()

# COMMAND ----------

print(order_items_df.columns)

# COMMAND ----------

print("Original Order Items Rows:", order_items_df.count())

# COMMAND ----------

from pyspark.sql.functions import col, sum

display(
    order_items_df.select([
        sum(col(c).isNull().cast("int")).alias(c)
        for c in order_items_df.columns
    ])
)

# COMMAND ----------

from pyspark.sql.functions import col

order_items_clean = order_items_df \
    .dropDuplicates() \
    .filter(col("order_item_id").isNotNull()) \
    .filter(col("order_id").isNotNull()) \
    .filter(col("product_id").isNotNull()) \
    .filter(col("quantity").isNotNull()) \
    .filter(col("quantity") > 0) \
    .filter(col("discount").isNotNull()) \
    .filter(col("discount") >= 0)

# COMMAND ----------

print("Original Order Items Rows:", order_items_df.count())
print("Clean Order Items Rows:", order_items_clean.count())

display(order_items_clean)

# COMMAND ----------

display(
    order_items_clean.select([
        sum(col(c).isNull().cast("int")).alias(c)
        for c in order_items_clean.columns
    ])
)

# COMMAND ----------

order_items_clean.write \
    .mode("overwrite") \
    .option("header", "true") \
    .option("delimiter", ",") \
    .csv("abfss://clean@stecommercedatalake2026.dfs.core.windows.net/order-items/")

# COMMAND ----------

display(
    dbutils.fs.ls(
        "abfss://clean@stecommercedatalake2026.dfs.core.windows.net/order-items/"
    )
)

# COMMAND ----------

payments_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("abfss://raw@stecommercedatalake2026.dfs.core.windows.net/payments/payments.csv")

display(payments_df)

# COMMAND ----------

payments_df.printSchema()

# COMMAND ----------

print("Original Payments Rows:", payments_df.count())

# COMMAND ----------

from pyspark.sql.functions import col, sum

display(
    payments_df.select([
        sum(col(c).isNull().cast("int")).alias(c)
        for c in payments_df.columns
    ])
)

# COMMAND ----------

print(payments_df.columns)

# COMMAND ----------

from pyspark.sql.functions import col, trim, to_date

payments_clean = payments_df \
    .dropDuplicates() \
    .filter(col("payment_id").isNotNull()) \
    .filter(col("order_id").isNotNull()) \
    .withColumn("payment_date", to_date(col("payment_date"))) \
    .filter(col("payment_date").isNotNull()) \
    .filter(col("payment_amount").isNotNull()) \
    .filter(col("payment_amount") >= 0) \
    .withColumn("payment_status", trim(col("payment_status")))

# COMMAND ----------

print("Original Payments Rows:", payments_df.count())
print("Clean Payments Rows:", payments_clean.count())

display(payments_clean)

# COMMAND ----------

payments_clean.write \
    .mode("overwrite") \
    .option("header", "true") \
    .option("delimiter", ",") \
    .csv("abfss://clean@stecommercedatalake2026.dfs.core.windows.net/payments/")

# COMMAND ----------

display(
    dbutils.fs.ls(
        "abfss://clean@stecommercedatalake2026.dfs.core.windows.net/payments/"
    )
)