# Anotações - DockerCompose

## Networks

objetivo: 

## Volumes

objetivo: persistir dados e criar um vinculo de dados do host para o container

```yaml
services:
  app:
    

```
## comandos do dockercompose

- **tty**: imprime tudo que roda no terminal

## iniciando um dockercompose

- DOCKER-COMPOSE.YAML

- subir todos os containers do dockercompose:
```bash
docker compose up
```

- subir apenas um serviço do dockercompose:
```bash
docker compose run <nome_do_serviço>
```

- para todos os serviços do dockercompose:
```bash
docker compose stop 
```

- para e apaga os serviço do dockercompose:
```bash
docker compose down
```
