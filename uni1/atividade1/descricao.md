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

- 🔗 [Servidor](https://hub.docker.com/layers/carlosg18docker/eng_dados/servertcp/images/sha256-1048bff77a0d13faae823d8ded2bf8b23554b960c74e855f53c0b46ae2483ed1)
- 🔗 [Cliente]([https://dockerhub.com/carlosg18docker/eng_dados:clienttcp](https://hub.docker.com/layers/carlosg18docker/eng_dados/clienttcp/images/sha256-96d045d41d74ef737f2bdd46f4192f922909998805cb6dae1032b88ea19fa417))
