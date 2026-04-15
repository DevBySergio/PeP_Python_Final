"""
MÓDULO: etl.transformer

RESPONSABILIDAD:
- Transformar los datos de entrada en datos listos para DB.

FUNCIONES:

1. transform_clientes(df)
   PROCESO:
   - Limpieza (cleaning.py)
   - Validación:
        dni_valid
        telefono_valid
        correo_valid
   - Generación flags:
        dni_ok / dni_ko
        telefono_ok / telefono_ko
        correo_ok / correo_ko
   - Anonimización:
        dni_hash
   - Selección y renombrado columnas

2. transform_tarjetas(df)
   PROCESO:
   - Limpieza
   - Anonimización:
        numero_tarjeta_hash
        cvv_hash
   - Eliminación de CVV original
   - Selección columnas finales

VARIABLES:
- CLIENTES_COLUMNS_FINAL
- TARJETAS_COLUMNS_FINAL

INTERACCIÓN:
- pipeline.py

OUTPUT:
- DataFrames listos para carga
"""