# 🗂️ Atividade 2 - Programando MapReduce em Hadoop

A atividade consiste na programação de funções **Map** e **Reduce** para processamento de dados em um cluster **Hadoop**, utilizando datasets reais.

## 🧰 Estrutura da Atividade

A prática está dividida em duas tarefas principais, cada uma com objetivos específicos:

* **Tarefa 1 – Contagem de Palavras**: Conta a quantidade de ocorrências de cada palavra em um arquivo de texto.
* **Tarefa 2 – Acessos por IP**: Analisa um log de servidor HTTP para contabilizar acessos por endereço IP.

Ambas as tarefas utilizam scripts Python (`mapper.py` e `reducer.py`) customizados e são executadas em um ambiente Hadoop.

## 📁 Conteúdo do Repositório

* `mapper_tarefa1.py` – Script de mapeamento para a contagem de palavras.
* `reducer_tarefa1.py` – Script de redução para a contagem de palavras.
* `mapper_tarefa2.py` – Script de mapeamento para análise de acessos por IP.
* `reducer_tarefa2.py` – Script de redução para análise de acessos por IP.
* `README.md` – Instruções e detalhes da atividade.

## 📚 Recursos Utilizados

* 📂 **Código base para início da prática:**
  [Scripts iniciais](https://www.dca.ufrn.br/~viegas/disciplinas/DCA0132/files/Scripts/)

* 📄 **Datasets utilizados:**
  [https://goo.gl/A3MhFS](https://goo.gl/A3MhFS)

## 📝 Descrição das Tarefas

### 1. 📊 Contagem de Palavras

* **Arquivo:** `texto.txt` (6,5MB)
* **Requisitos:**

  * A saída deve conter: `palavra<TAB>quantidade`
  * A contagem deve ser **case-insensitive** (ex: "Casa" = "casa")
  * A saída deve estar em **ordem decrescente de frequência**

### 2. 🌐 Acessos por IP

* **Arquivo:** `access.log.new` (244MB)
* **Requisitos:**

  * A saída deve conter: `IP<TAB>quantidade de acessos`
  * Apenas o endereço IP de cada linha do log deve ser considerado
  * A saída final deve estar em **ordem decrescente de acessos**

## ▶️ Como Executar no Hadoop

1. **Subir arquivos para o HDFS:**

   ```bash
   hdfs dfs -put texto.txt /user/seu_usuario/
   hdfs dfs -put access.log.new /user/seu_usuario/
   ```

2. **Executar a tarefa no cluster:**

   ```bash
   hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
     -input /user/seu_usuario/texto.txt \
     -output /user/seu_usuario/saida_tarefa1 \
     -mapper mapper_tarefa1.py \
     -reducer reducer_tarefa1.py \
     -file mapper_tarefa1.py \
     -file reducer_tarefa1.py
   ```

   *(Adapte os caminhos para a Tarefa 2 conforme necessário.)*

3. **Visualizar o resultado:**

   ```bash
   hdfs dfs -cat /user/seu_usuario/saida_tarefa1/part-00000
   ```
