# Backend

## Como correr el proyecto
Ejecutar los siguientes comandos en orden.

### 1. Crear entorno virtual
`python3 -m venv .venv`
### 2. Activar entorno virtual
 - En Linux `source .venv/bin/activate`
 - En Windows (powershell) `.venv\Scripts\Activate.ps1`
### 3. Instalar dependencias necesarias
`pip install -r requirements.txt`
### 4. Iniciar el servidor
`fastapi dev src/main.py`
back-main$ python3 -m uvicorn src.main:app --reload
