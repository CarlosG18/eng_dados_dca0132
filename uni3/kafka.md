# Anotações sobre o Apache Kafka

## arquitetura
- produtor,
- consumidor,
- broker,
- topicos,
- partições, 
- offset - usado para saber quais topicos foram lidos e fazer a leitura de novos dados,
- controler (Kraft) - gerencia o cluster

## Formato de mensagem do Kafka

- chave
- valor
- offset
- timestamp

**obs**:
- Os dados são imutaveis
- Os dados ficam armazenados indefinidamente ou por um tempo configuravel
- debezium -> conector que monitora alterações no banco, mandando a alteração para o topico do kafka
