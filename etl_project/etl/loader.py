"""
MÓDULO: etl.loader

RESPONSABILIDAD:
- Insertar datos en la base de datos.

FUNCIONES:

1. load_clientes(df, engine)
   - Inserta en tabla 'clientes'
   - if_exists = 'append'

2. load_tarjetas(df, engine)
   - Inserta en tabla 'tarjetas'

3. save_output_csv(df, output_path, filename)
   - Guarda CSV transformado

VARIABLES:
- TABLE_CLIENTES
- TABLE_TARJETAS

INTERACCIÓN:
- pipeline.py
- db.connection.py

CONSIDERACIONES:
- Evitar duplicados (posible mejora futura)
- Manejo de errores de inserción
"""