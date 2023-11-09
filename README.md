# Nombre del Proyecto

¡Bienvenido a Dogs-Api!

## Descripción

Es una API para perros sencilla, creada con fines de evaluación. .

## Requisitos

Asegúrate de tener instalados los siguientes requisitos antes de ejecutar la aplicación:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

# Configuración

Antes de ejecutar la aplicación, asegúrate de configurar las siguientes variables de entorno en un archivo `.env` en la raíz del proyecto:

```bash

# Archivo .env

# Configuración api
DJANGO_SECRET_KEY=changeme
DJANGO_ALLOWED_HOSTS=127.0.0.0
JWT_PASSWORD=changeme

# Configuración de la base de datos
DB_NAME=dbname
DB_USER=rootuser
DB_PASS=changeme

```

## Ejecución en Desarrollo

Para ejecutar la aplicación en un entorno de desarrollo, utiliza el siguiente comando en tu terminal:

```bash

docker-compose up -d

```

## Despliegue

Para desplegar la aplicación en un entorno de producción, sigue estos pasos:

1. Asegúrate de tener el archivo `docker-compose-deploy.yml` en la raíz del proyecto.

2. Ejecuta el siguiente comando en tu terminal:

```bash

docker-compose -f docker-compose-deploy.yml up -d

```
