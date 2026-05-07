# TESTME

## Objetivo

Dejar el proyecto listo para una demo desde cero, arrancarlo, ejecutar el DAG y comprobar que el ETL carga datos correctamente.

El repositorio queda preparado con solo dos archivos de entrada validos:

- `data/input/Clientes-2026-05-07.csv`
- `data/input/Tarjetas-2026-05-07.csv`

---

## 1. Reinicio completo

Desde la raiz del proyecto:

```bash
docker compose down -v
find logs -mindepth 1 -delete
find data/output -mindepth 1 -delete
```

Esto elimina:

- contenedores
- red Docker
- volumen de PostgreSQL
- logs generados
- CSV procesados en `data/output`

---

## 2. Comprobar archivos de demo

Verifica que solo existan los CSV validos:

```bash
find data/input -maxdepth 1 -type f | sort
```

Debes ver:

```text
data/input/.gitkeep
data/input/Clientes-2026-05-07.csv
data/input/Tarjetas-2026-05-07.csv
```

---

## 3. Levantar el proyecto

```bash
docker compose up --build -d
docker compose ps
```

Espera a que:

- `etl_postgres` aparezca como `healthy`
- `airflow-webserver` este `Up`
- `airflow-scheduler` este `Up`

---

## 4. Abrir Airflow

- URL: `http://localhost:8080`
- Usuario: `admin`
- Password: `admin`

---

## 5. Ejecutar el DAG

1. Activar el DAG `etl_pipeline`
2. Lanzar un `Manual Run`

Si quieres probarlo por terminal en vez de la UI:

```bash
docker compose exec airflow-scheduler airflow tasks test etl_pipeline run_etl_pipeline 2026-05-07
```

---

## 6. Comprobar salida

Ver CSV generados:

```bash
find data/output -maxdepth 1 -type f | sort
```

Debes obtener:

```text
data/output/.gitkeep
data/output/clean_Clientes-2026-05-07.csv
data/output/clean_Tarjetas-2026-05-07.csv
```

---

## 7. Comprobar base de datos

```bash
docker compose exec postgres psql -U etl_user -d etl_db -c "SELECT COUNT(*) AS clientes FROM clientes;"
docker compose exec postgres psql -U etl_user -d etl_db -c "SELECT COUNT(*) AS tarjetas FROM tarjetas;"
```

Para la demo actual, el resultado esperado es:

- `clientes = 3`
- `tarjetas = 3`

---

## 8. Ver el detalle cargado

```bash
docker compose exec postgres psql -U etl_user -d etl_db -c "SELECT * FROM clientes;"
docker compose exec postgres psql -U etl_user -d etl_db -c "SELECT * FROM tarjetas;"
```

---

## 9. Si algo falla

Logs de la tarea:

```bash
docker compose exec airflow-scheduler airflow tasks test etl_pipeline run_etl_pipeline 2026-05-07
```

Logs del scheduler:

```bash
docker compose logs airflow-scheduler --tail=200
```

Logs del webserver:

```bash
docker compose logs airflow-webserver --tail=200
```

---

## 10. Reset rapido para repetir la demo

```bash
docker compose down -v
find logs -mindepth 1 -delete
find data/output -mindepth 1 -delete
docker compose up --build -d
```
