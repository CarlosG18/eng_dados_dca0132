from pyspark.sql import SparkSession

# realizando configurações da seção
spark = (
    SparkSession.builder
        .master("yarn")
        .appName("People Count")
        .getOrCreate()
)

# definindo o contexto
rdd = spark.sparkContext.textFile("file:///home/myuser/myfiles/README.md")

rdd = spark.sparkContext.textFile("file:///home/myuser/myfiles/conjunto2.csv")

#removendo o cabeçalho
head = rdd.first()
dados = rdd.filter(lambda linha: linha != head)

# Separando os campos por vírgula e tratando os tipos
dados_processados = dados.map(lambda linha: linha.split(",")) \
                         .map(lambda campos: (campos[0],campos[1]))  # pegando o nome do cargo

#retirando as duplicatas
remove_duplicatas = dados.distinct()

remove_duplicatas.collect()

#dados_processados.collect()

dados_processados.distinct().collect()
