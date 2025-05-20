from pyspark.sql import SparkSession

# realizando configurações da seção
spark = (
    SparkSession.builder
        .master("yarn")
        .appName("People Count")
        .getOrCreate()
        .sparkContext
)

# definindo o contexto
rdd = spark.textFile("myfiles/conjunto2.csv")
