# Route Calculator API 360

Este proyecto es una API para calcular rutas entre ciudades utilizando una base de datos SQLite. Está desarrollado en Python y utiliza FastAPI para exponer los endpoints.

## Requisitos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- SQLite3

## Instalación

1. **Clona el repositorio o descarga el código fuente:**

   ```sh
   git clone https://github.com/emtipi/routeCalculatorAPI360
   cd routeCalculatorAPI360
   ```

2. **Crea y activa un entorno virtual (opcional pero recomendado):**

   ```sh
   python -m venv venv
   # En Windows
   .\venv\Scripts\activate
   # En Linux/MacOS
   source venv/bin/activate
   ```

3. **Instala las dependencias:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Verifica que el archivo de base de datos `cities_connections.db` esté en la raíz del proyecto.**

## Ejecución

1. **Inicia la API:**

   ```sh
   uvicorn main:app --reload
   ```

2. **Accede a la documentación interactiva:**

   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

## Estructura del Proyecto

- `main.py`: Punto de entrada de la API.
- `models.py`: Modelos de datos y lógica de acceso a la base de datos.
- `cities_connections.db`: Base de datos SQLite con las conexiones entre ciudades.
- `requirements.txt`: Lista de dependencias del proyecto.

## Notas

- Si necesitas modificar la estructura de la base de datos, edita el archivo `cities_connections.db` usando herramientas como DB Browser for SQLite.

## Licencia

Este proyecto está bajo la licencia MIT. Puedes modificarlo y distribuirlo libremente.