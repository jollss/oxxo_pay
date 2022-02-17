# Cloyster

<div style="text-align:right"><img src="https://img.pokemondb.net/artwork/vector/large/cloyster.png" width="250"/></div>

cloyster es un Microserervicio para el proceso de pagos por medio de conekta.

Permite inicializar con la estructura básica un proyecto con Flask + SQLAlchemy + Alembic + MySQL.

### *NO usa docker-compose*

## Uso
Crear la imagen
1. docker build -t cloyster:ejmeplo .
```shell
docker build -t image:version .
```
2. Correr la imagen

Windows:
```
docker run --rm -it --env-file=.env_example -v ${PWD}:/usr/src/app -p 5091:5000 --name cloyster  cloyster:ejmeplo
```
*NIX:
```
docker run --rm -it --env-file=.env_example -v $(pwd):/usr/src/app -p 5091:5000 --name cloyster  cloyster:ejmeplo
```
Comentarios:el .env_example remplazalo por .env para que no modifiques nada de los ejemplos
## Licencia

Cura Deuda 2022
