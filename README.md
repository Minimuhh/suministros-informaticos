# suministros-informaticos
Sistema que maneja los suministros informaticos


## Objetivos del proyecto:

El objetivo es crear una plataforma para una empresa de suministros informáticos, en la cual se
desarrollara una aplicación web que le ayude con la gestión tanto de sus productos como con la de sus
proveedores permitiéndole ver en tiempo real datos y estadísticas de sus ventas y salidas de almacen.

## Stack tecnológico y alternativas evaluadas

Stack tecnologico:
- Frontend:
- HTML
- CSS(Bootstrap)
- Javascript
- Backend:
- Flask
- Sqlite3
- pip

## Alternativas evaluadas:
- Django
- React
- Tailwindcss
- Postgresql
- Mysql.

## Explicación de los requisitos de la aplicación:

Flask: Es un framework de rapido desarrollo hecho en python que nos permite crear aplicaciones web
simples y complejas con gran facilidad.
Bootstrap: Framework de css que nos ayuda al rapido desarrollo del diseño y estilado de una pagina web
Sqlite3: Base de datos versatil muy util y potente para proyectos pequeños que no requiren gran cantidad
de consultas.

## Manual de instalación


## Instalación

```
pip install -r requirements.txt
```
### Instalacion en Docker

- Construyendo la imagen: 
```
docker build -t <nombre-imagen>:<tag> .
ejemplo:
docker build -t suministros:latest .
```
<nombre-imagen> : nombre que le vamos a poner a la imagen(cualquiera :) )
<tag>: una etiqueta cualquiera que nos va a ayudar a identificar un especifico build (cualquiera tambien)

- Corriendo la imagen en un contenedor:

```
docker run -d -p <port-exposed>:<port-internal> <nombre-imagen>:<tag>
ejemplo:
docker run -d -p 8000:5000 suministros:latest
```
-d es "detach mode" que corre el contenedor sin necesidad de ver los cambios en la terminal
-p es el puerto en el cual queremos correr el contenedor

- Deteniendo el contenedor

```
docker stop <hash-code-container>
docker stop 893ff1fe1825
```

** Repite la operacion cada vez que hayas hecho un cambio en el proyecto
	- build image
	- run image 
	- stop image 


## Conclusiones y evolutivos del proyecto (cosas a mejorar)
