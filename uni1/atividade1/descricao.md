# 🐳 Atividade 1 - Criação de Imagens e Containers Docker

Este repositório contém a aplicação **cliente-servidor** desenvolvida como parte da Atividade 1 da disciplina, juntamente com os arquivos de configuração necessários para a criação e orquestração de containers Docker.

## 📦 Estrutura do Projeto

O projeto está dividido em duas aplicações principais:

- **Servidor**: Responsável por processar e responder às requisições recebidas.
- **Cliente**: Realiza requisições ao servidor e exibe as respostas.

Ambas as aplicações estão containerizadas e podem ser executadas simultaneamente utilizando o **Docker Compose**.

## 📁 Conteúdo do Repositório

- `Dockerfile-cliente` – Define a imagem Docker para a aplicação cliente.
- `Dockerfile-servidor` – Define a imagem Docker para a aplicação servidor.
- `docker-compose.yml` – Arquivo de orquestração para executar os containers em conjunto.

## ▶️ Como Executar

1. **Clone este repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <nome-do-repositorio>
   ```

2. **Execute o Docker Compose:**
   ```bash
   docker-compose up --build
   ```

3. As aplicações cliente e servidor estarão rodando nos containers definidos. Consulte os logs do terminal para ver a comunicação entre eles.

## 📤 Submissão

A aplicação está disponível no DockerHub nos links abaixo:

- 🔗 **Servidor:** [dockerhub.com/carlosg18docker/eng_dados:servertcp](https://dockerhub.com/carlosg18docker/eng_dados:servertcp)
- 🔗 **Cliente:** [dockerhub.com/carlosg18docker/eng_dados:clienttcp](https://dockerhub.com/carlosg18docker/eng_dados:clienttcp)

## Duvidas

- 1. se o serviço for a mesma coisa de um serviço já criado, (no caso tem dois serviços de cliente só que fazem a mesma coisa) existe alguma forma mais "compacta" de definir isso sem precisar repetir tudo novamente?

- 2. confirmar isso, se o elemento tiver configurações ele vai precisar colocar o ":" se caso não precise colocar o "-":

```
networks:
      network1:
        ipv4_address:

networks:
    - network1 
```