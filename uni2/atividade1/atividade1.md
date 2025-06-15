# Atividade 4 - Trabalhando com dados do Banco de dados com o PySpark

### ⚙️ Etapas do pipeline

#### 1. **Início da sessão Spark**

```python
SparkSession.builder.master("yarn").appName("Data Transform").getOrCreate()
```

A sessão é criada para rodar no cluster YARN.

---

#### 2. **Leitura de dados do PostgreSQL**

Os dados são lidos de uma tabela chamada `processos` usando o conector JDBC:

```python
df = spark.read.format("jdbc") \
    .option("url", "jdbc:postgresql://10.13.123.0:5432/curso_spark") \
    .option("dbtable", "processos") \
    .option("user", "postgres") \
    .option("password", "spark") \
    .option("driver", "org.postgresql.Driver") \
    .load()
```

---

#### 3. **Limpeza de dados**

Remoção de registros duplicados:

```python
df_clean = df.drop_duplicates()
```

* Linhas antes da limpeza: `300673`
* Linhas após limpeza: `164099`

---

#### 4. **Visualização de dados**

Visualização de amostras dos dados processados:

```python
df_clean.show()
```

Principais colunas:

* `ID_PROC`, `VARA`, `CLASSE`, `QTD_RDA_PROC`, `QTD_RTE_PROC`, `FAIXA_CAUSA`, `TEMPO_DIAS`, `ARRAY_ASSUNTO`

---

#### 5. **Agregações por vara**

Cálculo do total de réus e reclamantes por vara:

```python
from pyspark.sql.functions import sum, desc

df_agrupado_vara = df_clean.groupBy('VARA').agg(
    sum('QTD_RDA_PROC').alias('TOTAL_REUS'),
    sum('QTD_RTE_PROC').alias('TOTAL_RECLAMANTES')
).orderBy(desc('TOTAL_REUS'))
```

---

#### 6. **Exportação dos resultados**

Os dados agregados são gravados de volta no PostgreSQL na tabela `carlos`:

```python
df_agrupado_vara.write.format("jdbc") \
    .option("url", "jdbc:postgresql://10.13.123.0:5432/curso_spark") \
    .option("dbtable", "carlos") \
    .option("user", "postgres") \
    .option("password", "spark") \
    .option("driver", "org.postgresql.Driver") \
    .save()
```

---

#### 7. **Validação dos dados exportados**

Leitura da tabela `carlos` para validação:

```python
df = spark.read.format("jdbc") \
    .option("url", "jdbc:postgresql://10.13.123.0:5432/curso_spark") \
    .option("dbtable", "carlos") \
    .option("user", "postgres") \
    .option("password", "spark") \
    .option("driver", "org.postgresql.Driver") \
    .load()

df.show()
```

---

### 📌 Observações

* O sistema usa Spark com YARN, adequado para grandes volumes de dados.
* A estrutura permite fácil substituição da origem e destino de dados.
* As colunas `QTD_RDA_PROC` e `QTD_RTE_PROC` representam, respectivamente, a quantidade de réus e reclamantes por processo.
