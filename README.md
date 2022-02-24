# Cloyster

<div style="text-align:center"><img src="https://img.pokemondb.net/artwork/vector/large/cloyster.png" width="250"/></div>

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
docker run --rm -it --env-file=.env_example -v ${PWD}:/usr/src/app -p 5009:5000 --name cloyster  cloyster:ejmeplo
```
*NIX:
```
docker run --rm -it --env-file=.env_example -v $(pwd):/usr/src/app -p 5009:5000 --name cloyster  cloyster:ejmeplo
```
Comentarios:el .env_example remplazalo por .env para que no modifiques nada de los ejemplos y solo agrega en el gitignore el .env que utilices
## Licencia

Cura Deuda 2022

# tags version semantica
Estructura
primer digito es la version en la que se lanza un realese o a prod(version mayor)
segundo digito se añade cierta funcionabilidad o neuva libreria
tercer digito hace referencia a los fix que se agregan o correccion de errores
## Crear un tag 
git tag  -a v1.0.0 -m "Version 1.0.0 oxxopay-conekta"
## Referencia a un commit
 git tag -a versiondetag el hashtag -m "tu comentario del tag"
## Ver tag
git tag muestra los tag existente
git show versiontag y se mostrara el commit especifico y el comentario del tag
