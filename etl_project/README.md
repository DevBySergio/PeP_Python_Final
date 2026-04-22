# 🧩 ETL Data Pipeline Project

## 📌 Descripción

Este proyecto implementa un **pipeline ETL (Extract, Transform, Load)** completo utilizando Python, orquestado con Apache Airflow y desplegado mediante contenedores Docker.

El sistema procesa ficheros CSV con información de clientes y tarjetas, aplica transformaciones, validaciones y anonimización de datos sensibles, y finalmente carga la información en una base de datos relacional PostgreSQL.

---

## 🏗️ Arquitectura del sistema

El proyecto está basado en una arquitectura modular con los siguientes componentes:

- **ETL en Python**
  - Procesamiento de datos con `pandas`
  - Validaciones personalizadas (DNI, teléfono, email)
  - Anonimización mediante hashing SHA-256 con SALT

- **Orquestación**
  - Apache Airflow para ejecución automática del pipeline
  - DAG programado para ejecución diaria

- **Base de datos**
  - PostgreSQL como sistema de almacenamiento relacional

- **Contenerización**
  - Docker y Docker Compose para levantar todo el entorno

---

## 🧱 Stack tecnológico

| Componente    | Tecnología              |
| ------------- | ----------------------- |
| Lenguaje      | Python 3.11             |
| ETL           | pandas, SQLAlchemy      |
| Base de datos | PostgreSQL 15           |
| Orquestación  | Apache Airflow 2.8      |
| Contenedores  | Docker + Docker Compose |
| Hashing       | SHA-256 + SALT          |

---

## 📁 Estructura del proyecto

```
etl_project/
├── dags/                  # DAGs de Airflow
├── etl/                   # Lógica ETL
├── db/                    # Scripts SQL
├── data/
│   ├── input/             # CSV de entrada
│   └── output/            # CSV procesados
├── logs/                  # Logs del sistema
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

## 🔄 Funcionamiento del pipeline

1. **Extracción**
   - Lectura de ficheros CSV desde `data/input/`
   - Filtrado por patrón:
     - `Clientes-YYYY-MM-DD.csv`
     - `Tarjetas-YYYY-MM-DD.csv`

2. **Transformación**
   - Limpieza de datos (trim, normalización)
   - Validaciones:
     - DNI
     - Teléfono
     - Email

   - Generación de flags:
     - `*_ok` / `*_ko`

   - Anonimización:
     - DNI → hash SHA-256
     - Tarjeta → hash SHA-256
     - CVV → hash SHA-256

3. **Carga**
   - Inserción en PostgreSQL
   - Creación automática de tablas si no existen

4. **Salida**
   - Generación de ficheros limpios en `data/output/`

---

## 🔐 Seguridad y anonimización

- Uso de hashing SHA-256 con SALT configurable
- No se almacenan datos sensibles en claro:
  - DNI anonimizado
  - Número de tarjeta anonimizado
  - CVV nunca almacenado en texto plano

---

## ⚙️ Configuración

El proyecto utiliza variables de entorno definidas en el archivo `.env`:

```
POSTGRES_USER=etl_user
POSTGRES_PASSWORD=etl_pass
POSTGRES_DB=etl_db

HASH_SALT=my_super_secret_salt
```

---

## 🚀 Ejecución del proyecto

### 1. Requisitos previos

- Docker
- Docker Compose

---

### 2. Construir y levantar los servicios

Desde la raíz del proyecto:

```bash
docker-compose up --build
```

---

### 3. Acceso a Airflow

Una vez levantado el entorno:

- URL: http://localhost:8080
- Usuario: `admin`
- Contraseña: `admin`

---

### 4. Activar el pipeline

1. Acceder a la interfaz web de Airflow
2. Buscar el DAG: `etl_pipeline`
3. Activarlo (toggle ON)
4. Ejecutarlo manualmente o esperar a la ejecución programada (03:00 AM)

---

## 📂 Uso del sistema

1. Colocar los ficheros CSV en:

```
data/input/
```

2. Ejecutar el pipeline (manual o automático)

3. Consultar resultados:

- CSV transformados → `data/output/`
- Datos cargados → PostgreSQL

---

## 🧪 Ejemplo de ficheros válidos

- `Clientes-2025-11-10.csv`
- `Tarjetas-2025-11-10.csv`

---

## 📝 Consideraciones

- Solo se procesan ficheros que cumplan el patrón especificado
- Los ficheros inválidos son ignorados
- El sistema está preparado para ampliaciones:
  - Logging avanzado
  - Manejo de errores
  - Tests automatizados

---

## 👥 Equipo

Proyecto desarrollado como parte de una práctica de ingeniería de datos.

---

## 📈 Posibles mejoras

- Implementación de logging estructurado
- Gestión de errores y registros rechazados (`rows_rejected.csv`)
- Tests unitarios con pytest
- CI/CD con GitHub Actions
- Uso de herramientas como Prefect o Spark

---

## 📄 Licencia

Uso académico
