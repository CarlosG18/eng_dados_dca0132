# Atividade 6 - Consumindo dados com Spark Streaming a partir de um banco de dados MongoDB

Este projeto tem como objetivo a construção de uma aplicação capaz de consumir e processar dados em tempo real a partir de alterações realizadas em coleções MongoDB. A comunicação dos dados é feita via Apache Kafka, utilizando Debezium para captura de alterações (CDC), e o processamento é realizado com Spark Streaming por meio de uma aplicação desenvolvida em PySpark.

---

## 🧰 Tecnologias Utilizadas

* **Apache Kafka**
* **Apache Spark (PySpark + Spark Streaming)**
* **MongoDB**
* **Debezium** (para captura de alterações no MongoDB)
* **Docker**

---

## 📌 Objetivos da Prática

* Integrar Apache Kafka, Apache Spark e MongoDB para criar um pipeline de dados em tempo real.
* Capturar alterações feitas em coleções MongoDB e transmiti-las via Kafka.
* Processar dados transmitidos utilizando Spark Streaming com PySpark.

---

## 📝 Etapas da Implementação

Para esta aplicação, foi utilizado o cluster desenvolvido pelo [Professor Carlos Viegas](https://github.com/cmdviegas), por meio do repositório [Hadoop-spark](https://github.com/cmdviegas/hadoop-spark).

---

### 1. Configuração do Ambiente

#### MongoDB

Para rodar o MongoDB em modo replicaSet, foram feitas as seguintes configurações no `docker-compose.yml`:

```yaml
volumes:
  mongo_data:
    name: ${STACK_NAME}_mongo_data
    driver: local

mongo:
  image: mongo:6.0
  container_name: ${STACK_NAME}-mongo
  hostname: mongo
  ports:
    - "27017:27017"
  command: ["mongod", "--replSet", "rs0", "--bind_ip_all"]
  volumes:
    - mongo_data:/data/db
  networks:
    - ${STACK_NAME}_network
  healthcheck:
    test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
    interval: 10s
    timeout: 10s
    retries: 5
```

Após subir o container, foi necessário entrar no shell do MongoDB para iniciar o replica set:

```bash
docker exec -it spark-mongo mongosh
rs.initiate()
```

Com o replica set iniciado, podemos verificar o status com:

```bash
rs.status()
```

O status mostra que o replica set está configurado corretamente, destacando o membro principal com o host `mongo:27017`.

---

#### Apache Kafka

Para rodar o Kafka, foram seguidos os passos:

1. Entrar no container `spark-master`.
2. Instalar o Kafka.
3. Configurar o arquivo `$KAFKA_HOME/config/kraft/server.properties`.
4. Gerar um ID para o cluster:

   ```bash
   export KAFKA_CLUSTER_ID="$(kafka-storage.sh random-uuid)"
   ```
5. Preparar o diretório de logs:

   ```bash
   kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c $KAFKA_HOME/config/kraft/server.properties
   ```
6. Criar o tópico Kafka:

   ```bash
   kafka-topics.sh --create --topic topico-mongo --bootstrap-server spark-master:9092
   ```
7. Iniciar o servidor Kafka:

   ```bash
   kafka-server-start.sh $KAFKA_HOME/config/kraft/server.properties
   ```

Se no log aparecer:

```
[INFO KafkaRaftServer nodeId=1] Kafka Server started (kafka.server.KafkaRaftServer)
```

significa que o Kafka está rodando corretamente.

---

#### Debezium (Kafka Connect)

Para configurar o conector Debezium MongoDB:

1. Instalar o conector do MongoDB.
2. Ajustar o arquivo `$KAFKA_HOME/config/connect-standalone.properties`.
3. Iniciar o Kafka Connect standalone:

   ```bash
   connect-standalone.sh $KAFKA_HOME/config/connect-standalone.properties
   ```

Se iniciar com sucesso, verá a mensagem:

```
[INFO Kafka Connect started (org.apache.kafka.connect.runtime.Connect:77)]
```

4. Criar o arquivo de configuração do conector `mongoc.json` com o conteúdo:

```json
{
  "name": "mongo-connector", 
  "config": {
    "connector.class": "io.debezium.connector.mongodb.MongoDbConnector",
    "tasks.max": "1",
    "mongodb.hosts": "rs0/mongo:27017", 
    "mongodb.connection.string": "mongodb://mongo:27017/?replicaSet=rs0",
    "mongodb.name": "mongosrv",
    "topic.prefix": "topico-mongo",
    "database.include.list": "spark-streaming", 
    "collection.include.list": "spark-streaming.dados",
    "mongodb.ssl.enabled": "false"
  }
}
```

5. Registrar o conector via API REST:

```bash
curl -X POST -H "Content-Type: application/json" --data @/home/myuser/kafka/connect/debezium-connector-mongodb/mongoc.json http://spark-master:8083/connectors
```

6. Verificar o status do conector:

```bash
curl http://spark-master:8083/connectors/mongo-connector/status
```

Resposta esperada:

```json
{
  "name": "mongo-connector",
  "connector": {
    "state": "RUNNING",
    "worker_id": "172.31.0.3:8083"
  },
  "tasks": [
    {
      "id": 0,
      "state": "RUNNING",
      "worker_id": "172.31.0.3:8083"
    }
  ],
  "type": "source"
}
```

---

#### Apache Spark

* Acessar o Jupyter Notebook em `http://127.0.0.1:8888/`.
* Abrir o [notebook da aplicação Spark Streaming](spark-streaming.ipynb). 
* Inserir dados na coleção MongoDB e observar o processamento em tempo real no notebook.

---

## ⚙️ Resumo das Etapas

| Etapa                                      | Status |
| ------------------------------------------ | ------ |
| Rodar MongoDB em container                 | ✅      |
| Rodar cluster Hadoop/Spark                 | ✅      |
| Ajustar configurações do Kraft (Kafka)     | ✅      |
| Rodar servidor Kafka                       | ✅      |
| Configurar arquivo do conector Debezium    | ✅      |
| Rodar servidor Kafka Connect (Debezium)    | ✅      |
| Rodar MongoDB em modo replicaSet           | ✅      |
| Criar banco de dados                       | ✅      |
| Criar coleção                              | ✅      |
| Configurar conector Debezium (mongoc.json) | ✅      |
| Instalar curl                              | ✅      |
| Realizar requisição para API do conector   | ✅      |

---

## 🗂️ Informações Importantes

* **Tópico Kafka:** `topico-mongo`
* **Banco MongoDB:** `spark-streaming`
* **Coleção MongoDB:** `dados`

---

## Conclusão

Este projeto demonstrou a integração eficaz entre MongoDB, Kafka e Spark Streaming para criação de um pipeline de dados em tempo real. Utilizando Debezium para captura de mudanças no MongoDB, conseguimos transmitir os eventos via Kafka e processá-los dinamicamente com Spark Streaming.