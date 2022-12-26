# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Spark SQL Lab
# MAGIC 
# MAGIC ##### Tasks
# MAGIC 1. Create a DataFrame from the **`events`** table
# MAGIC 1. Display the DataFrame and inspect its schema
# MAGIC 1. Apply transformations to filter and sort **`macOS`** events
# MAGIC 1. Count results and take the first 5 rows
# MAGIC 1. Create the same DataFrame using a SQL query
# MAGIC 
# MAGIC ##### Methods
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/spark_session.html" target="_blank">SparkSession</a>: **`sql`**, **`table`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html" target="_blank">DataFrame</a> transformations: **`select`**, **`where`**, **`orderBy`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.DataFrame.html" target="_blank">DataFrame</a> actions: **`select`**, **`count`**, **`take`**
# MAGIC - Other <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html" target="_blank">DataFrame</a> methods: **`printSchema`**, **`schema`**, **`createOrReplaceTempView`**

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-00.2L

# COMMAND ----------

# MAGIC %md ### 1. Create a DataFrame from the **`events`** table
# MAGIC - Use SparkSession to create a DataFrame from the **`events`** table

# COMMAND ----------

# TODO
events_df = FILL_IN

# COMMAND ----------

# MAGIC %md ### 2. Display DataFrame and inspect schema
# MAGIC - Use methods above to inspect DataFrame contents and schema

# COMMAND ----------

# TODO

# COMMAND ----------

# MAGIC %md ### 3. Apply transformations to filter and sort **`macOS`** events
# MAGIC - Filter for rows where **`device`** is **`macOS`**
# MAGIC - Sort rows by **`event_timestamp`**
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_32.png" alt="Hint"> Use single and double quotes in your filter SQL expression

# COMMAND ----------

# TODO
mac_df = (events_df
          .FILL_IN
         )

# COMMAND ----------

# MAGIC %md ### 4. Count results and take first 5 rows
# MAGIC - Use DataFrame actions to count and take rows

# COMMAND ----------

# TODO
num_rows = mac_df.FILL_IN
rows = mac_df.FILL_IN

# COMMAND ----------

# MAGIC %md **4.1: CHECK YOUR WORK**

# COMMAND ----------

from pyspark.sql import Row

assert(num_rows == 97150)
assert(len(rows) == 5)
assert(type(rows[0]) == Row)
print("All test pass")

# COMMAND ----------

# MAGIC %md ### 5. Create the same DataFrame using SQL query
# MAGIC - Use SparkSession to run a SQL query on the **`events`** table
# MAGIC - Use SQL commands to write the same filter and sort query used earlier

# COMMAND ----------

# TODO
mac_sql_df = spark.FILL_IN

display(mac_sql_df)

# COMMAND ----------

# MAGIC %md **5.1: CHECK YOUR WORK**
# MAGIC - You should only see **`macOS`** values in the **`device`** column
# MAGIC - The fifth row should be an event with timestamp **`1592540419446946`**

# COMMAND ----------

verify_rows = mac_sql_df.take(5)
assert (mac_sql_df.select("device").distinct().count() == 1 and len(verify_rows) == 5 and verify_rows[0]['device'] == "macOS"), "Incorrect filter condition"
assert (verify_rows[4]['event_timestamp'] == 1592540419446946), "Incorrect sorting"
del verify_rows
print("All test pass")

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Run the following cell to delete the tables and files associated with this lesson.

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
