# 🧪 Trabalhando com MongoDB e PySpark

Este projeto demonstra como realizar operações com dados utilizando **Apache Spark** e **MongoDB**, incluindo:

* Execução do MongoDB via Docker
* Inserção e consulta de dados usando `pymongo`
* Leitura, transformação e escrita de dados com **PySpark**
* Integração entre Spark e MongoDB

---

## 1. 📦 Pré-requisitos

Antes de começar, verifique se você tem o seguinte instalado:

* [Docker](https://www.docker.com/)
* [Apache Spark](https://spark.apache.org/) com o conector MongoDB (`mongo-spark-connector`)
* [Jupyter Notebook](https://jupyter.org/) (opcional, para executar o arquivo `.ipynb`)

---

## 2. 🚀 Subindo o MongoDB com Docker

Execute o comando abaixo para iniciar o MongoDB em um container Docker:

```bash
docker run -d \
  --name meu-mongo \
  --network spark_network \
  -p 27017:27017 \
  mongo
```

Esse comando cria um container chamado `meu-mongo`, conectado à rede Docker `spark_network`, com a porta padrão `27017` exposta.

---

## 3. 🔗 Testando conexão com MongoDB usando `pymongo`

### 3.1 Criando um banco e inserindo um documento

Utilize o seguinte código Python para testar a conexão com o MongoDB e inserir um documento:

```python
from pymongo import MongoClient

client = MongoClient("mongodb://meu-mongo:27017/")

db = client.test_database
collection = db.test_collection

result = collection.insert_one({"nome": "carlos"})
print(result.acknowledged)
```

### 3.2 Verificando a criação no shell do Mongo

Acesse o shell do Mongo dentro do container:

```bash
docker exec -it meu-mongo mongosh
```

Em seguida, execute:

```mongodb
show dbs;
```

Saída esperada (exemplo):

```
admin          40.00 KiB
config         60.00 KiB
local          40.00 KiB
test_database  40.00 KiB
```

---

## 4. 📝 Inserindo dados reais com `pymongo`

### 4.1 Inserindo dados do CSV para o MongoDB

```python
import csv

db = client.ufrn
collection_discente = db.discentes

with open('discentes-2024.csv', 'r', newline='') as f:
    data = csv.DictReader(f, delimiter=';')
    for linha in data:
        collection_discente.insert_one(linha)
```

### 4.2 Verificando a inserção via shell:

<p align="center">
  <img src="https://github.com/CarlosG18/eng_dados_dca0132/blob/main/uni2/atividade2/image/eng_dadospymongo.png" alt="simulacao">
</p>

```mongodb
use ufrn
db.discentes.find().limit(5)
```

<p align="center">
  <img src="https://github.com/CarlosG18/eng_dados_dca0132/blob/main/uni2/atividade2/image/eng_dados.png" alt="simulacao">
</p>

---

## 5. 🔍 Integração PySpark com MongoDB

### 5.1 Inicializando o Spark com URIs do MongoDB

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MongoSparkExample") \
    .config("spark.mongodb.read.connection.uri", "mongodb://meu-mongo:27017/test_database.collection_exemplo") \
    .config("spark.mongodb.write.connection.uri", "mongodb://meu-mongo:27017/test_database.collection_exemplo") \
    .getOrCreate()
```

---

## 6. 💾 Salvando transformações do Spark no MongoDB

Após realizar transformações no DataFrame (por exemplo, filtrando alunos do SiSU), salve os dados de volta no MongoDB com:

```python
alunos_sisu.write.format("mongodb") \
    .mode("overwrite") \
    .option("connection.uri", "mongodb://meu-mongo:27017/") \
    .option("database", "ufrn") \
    .option("collection", "alunos_sisu") \
    .save()
```

---

## 7. 📁 Arquivo principal

O código completo está no notebook:

* [`atividade_mongo.ipynb`](./atividade_mongo.ipynb)
