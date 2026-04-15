"""
MÓDULO: etl.validators

RESPONSABILIDAD:
- Validar campos críticos del negocio.

FUNCIONES:

1. validate_dni(dni)
   - Formato: 8 números + letra
   - Validación real de letra

2. validate_phone(phone)
   - Solo dígitos
   - Longitud mínima (ej: 9)

3. validate_email(email)
   - Regex estándar de email

4. generate_flag_pair(is_valid)
   - Convierte booleano en:
        ok → "Y"/"N"
        ko → "N"/"Y"

VARIABLES:
- DNI_PATTERN
- EMAIL_PATTERN

INTERACCIÓN:
- transformer.py

OUTPUT:
- Booleanos + flags OK/KO
"""