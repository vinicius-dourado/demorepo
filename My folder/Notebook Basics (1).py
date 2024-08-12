# Databricks notebook source
print("Hello World")

# COMMAND ----------

# MAGIC %md
# MAGIC # title 1
# MAGIC ## title 2
# MAGIC ### title 3

# COMMAND ----------

# MAGIC %run ./setup

# COMMAND ----------

print(fullname)

# COMMAND ----------

# MAGIC %fs ls 'databricks-datasets/'

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
display(files)
