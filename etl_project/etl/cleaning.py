"""
MÓDULO: etl.cleaning

RESPONSABILIDAD:
- Normalizar y limpiar los datos antes de validación.

FUNCIONES:

1. trim_strings(df)
   - Elimina espacios al inicio y final de todos los strings.

2. normalize_case(df)
   - nombre → capitalizado
   - correo → minúsculas

3. remove_accents(text)
   - Elimina tildes y caracteres especiales.

4. normalize_phone(phone)
   - Elimina todo excepto dígitos.

5. clean_dataframe(df)
   - Aplica todas las funciones anteriores de forma orquestada.

VARIABLES:
- STRING_COLUMNS → columnas tipo texto

INTERACCIÓN:
- transformer.py utiliza este módulo

OBJETIVO:
- Garantizar consistencia antes de validar
"""