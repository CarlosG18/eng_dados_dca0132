from pyspark.sql import SparkSession

# realizando configurações da seção no PySpark
spark = (
    SparkSession.builder
        .master("yarn")
        .appName("People Count")
        .getOrCreate()
)

# definindo o RDD
rdd = spark.sparkContext.textFile("file:///home/myuser/myfiles/conjunto2.csv")

#removendo o cabeçalho
head = rdd.first()
dados = rdd.filter(lambda linha: linha != head)

# Separando os campos por vírgula
dados_processados = dados.map(lambda linha: linha.split(",")) \
                         .map(lambda campos: (campos[0],campos[1]))  # pegando o nome e o cargo

# ordenando do rdd pelo cargo, retirando duplicatas, aplicando o map para contagem (cargo, 1) e depois fazendo o reduce para a contagem dos cargos
dados_processados.sortBy(lambda x: x[1]).distinct().map(lambda x: (x[1],1)).reduceByKey(lambda a, b: a + b).collect()
