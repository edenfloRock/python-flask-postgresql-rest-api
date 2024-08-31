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
sudo dnf install postgresql-devel  #sudo apt-get install libpq-dev
sudo dnf groupinstall "Development Tools"
pip install -r requirements.txt


```

- Dentro del archivo *.env* se debe especificar los datos de acceso a la base de datos.

```sh
cd src
python -B app.py
```

Una vez arrancada la aplicación, usar los URLs:

- http://127.0.0.1:5000/api/movies/

- http://127.0.0.1:5000/api/movies/77849cb0-f33b-4157-b664-de7dad3fa21a  
