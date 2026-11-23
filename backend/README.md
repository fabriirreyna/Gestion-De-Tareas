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
back-main$ `python3 -m uvicorn src.main:app --reload`


## API Contract

### Convenciones

- Todas las rutas empiezan con `/api`.
- Rutas, parámetros y campos van en inglés; las descripciones, en español.
- Los recursos van en plural y los parámetros de ruta en `snake_case` entre llaves (`{task_id}`).
- `/me` representa al usuario autenticado.

### Endpoints

| Método | Ruta | Descripción | Acceso |
|---|---|---|---|
| POST | `/api/auth/login` | Iniciar sesión | Público |
| POST | `/api/auth/logout` | Cerrar sesión | Autenticado |
| POST | `/api/users` | Crear usuario | ADMIN |
| GET | `/api/users` | Listar usuarios | Autenticado |
| GET | `/api/users/me` | Ver mi perfil | Autenticado |
| GET | `/api/users/{user_id}` | Ver un usuario | Autenticado |
| POST | `/api/tasks` | Crear tarea | ADMIN, SUPERVISOR |
| GET | `/api/tasks` | Listar tareas | Autenticado |
| GET | `/api/tasks/{task_id}` | Ver detalle de tarea | Autenticado |
| PUT | `/api/tasks/{task_id}` | Editar tarea | ADMIN, SUPERVISOR |

### Autenticación

**POST `/api/auth/login`**

```json
// Request
{ "email": "usuario@empresa.com", "password": "Password123" }

// Response
{ "access_token": "jwt_token", "token_type": "bearer" }
```

**POST `/api/auth/logout`**

```json
// Response
{ "message": "Sesión cerrada correctamente" }
```

### Usuarios

**POST `/api/users`**

```json
// Request
{
  "first_name": "Juan",
  "last_name": "Pérez",
  "email": "juan@empresa.com",
  "password": "Password123",
  "role": "EMPLOYEE"
}
```

**Response de usuario** (la misma para `POST /users`, `GET /users/me` y `GET /users/{user_id}`; `GET /users` devuelve una lista de estos objetos):

```json
{
  "id": 1,
  "first_name": "Juan",
  "last_name": "Pérez",
  "email": "juan@empresa.com",
  "role": "EMPLOYEE",
  "is_active": true
}
```

### Tareas

**POST `/api/tasks`** y **PUT `/api/tasks/{task_id}`** usan el mismo request:

```json
{
  "title": "Reparar instalación eléctrica",
  "description": "Revisar la falla en la instalación eléctrica del edificio.",
  "priority": "HIGH",
  "due_date": "2026-11-22"
}
```

**Response de tarea** (la misma para crear, ver detalle y editar):

```json
{
  "id": 1,
  "title": "Reparar instalación eléctrica",
  "description": "Revisar la falla en la instalación eléctrica del edificio.",
  "priority": "HIGH",
  "status": "PENDING",
  "due_date": "2026-11-22",
  "created_by": 1,
  "assigned_to": null
}
```

`GET /api/tasks` devuelve una lista de tareas con los mismos campos, pero sin `description`.

---

## Valores permitidos

| Campo | Valores |
|---|---|
| `role` | `ADMIN`, `SUPERVISOR`, `EMPLOYEE` |
| `priority` | `LOW`, `MEDIUM`, `HIGH`, `URGENT` |
| `status` | `PENDING`, `IN_PROGRESS`, `COMPLETED`, `CANCELLED` |

- `is_active` (boolean): indica si el usuario puede acceder al sistema.
- `created_by`: id del usuario que creó la tarea.
- `assigned_to`: id del usuario asignado. En el Sprint 1 es siempre `null`, porque la asignación queda para una etapa posterior.

---

## Códigos de error

| Código | Nombre | Cuándo ocurre |
|---|---|---|
| 400 | Bad Request | Datos incorrectos o no válidos |
| 401 | Unauthorized | No autenticado o credenciales incorrectas |
| 403 | Forbidden | Sin permisos para la operación |
| 404 | Not Found | El recurso no existe |
| 409 | Conflict | Conflicto con el estado actual (ej: email ya registrado) |
| 422 | Unprocessable Entity | Los datos no cumplen las validaciones |
| 500 | Internal Server Error | Error interno del servidor |

---