import os
from pyspark.sql import SparkSession

# Suppress most Spark logging directly in memory
os.environ["PYSPARK_SUBMIT_ARGS"] = (
    "--conf spark.driver.extraJavaOptions=-Dlog4j.rootCategory=ERROR,console pyspark-shell"
)

# Create Spark session
spark = SparkSession.builder.appName("BigDataProject").getOrCreate()

# Also set Spark context log level to ERROR
spark.sparkContext.setLogLevel("ERROR")

# Test DataFrame
data = spark.range(5)
data.show()

print("PySpark is working!")

