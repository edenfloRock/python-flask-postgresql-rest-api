# API Rest con Python, PostgreSQL y Flask


Este es un proyecto de ejemplo para utilizar un base de datos PostgreSQL y acceder a ella desde una API Rest usando Python y Flask.

Se debe considerar los siguiente:

- Se asume que se cuenta con una base de datos PostgreSQL configurada con los respectivos accesos.

- Descarga de archivos

```sh
git clone
```

- Conectarse a la bd de PostgreSQL y ejecutar los scripts contenidos en el archivo */src/database/scripts/scripts.sql* 

- Crear ambiente e instalar las dependencias necesarias:
```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

- Dentro del archivo *.env* se debe especificar los datos de acceso a la base de datos.

```sh
cd src
python -B app.py
```