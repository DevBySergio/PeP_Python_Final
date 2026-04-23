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

import re

# Expresión regular para validar el formato del DNI:
# - 8 dígitos seguidos de una letra (mayúscula o minúscula)
DNI_PATTERN = r'^\d{8}[A-Za-z]$'

# Expresión regular para validar emails estándar
EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


def validate_dni(dni: str) -> bool:
    """
    Valida un DNI español.

    Pasos:
    1. Comprueba que el valor sea string.
    2. Elimina espacios en blanco.
    3. Valida el formato (8 números + letra).
    4. Calcula la letra esperada usando el algoritmo oficial.
    5. Compara la letra calculada con la proporcionada.

    Devuelve:
        True si el DNI es válido, False en caso contrario.
    """
    
    if not isinstance(dni, str):
        return False

    # Elimino espacios al inicio y final
    dni = dni.strip()

    if not re.match(DNI_PATTERN, dni):
        return False

    letters = "TRWAGMYFPDXBNJZSQVHLCKE"

    # Extraigo la parte numérica del DNI
    number = int(dni[:-1])

    # Calculo la letra esperada (módulo 23)
    expected_letter = letters[number % 23]

    # Comparo la letra calculada con la proporcionada
    return dni[-1].upper() == expected_letter


def validate_phone(phone: str) -> bool:
    """
    Valida un número de teléfono.

    Reglas:
    1. Debe ser string.
    2. Solo puede contener dígitos.
    3. Debe tener al menos 9 caracteres.

    Devuelve:
        True si es válido, False en caso contrario.
    """

    if not isinstance(phone, str):
        return False

    phone = phone.strip()

    if not phone.isdigit():
        return False

    return len(phone) >= 9


def validate_email(email: str) -> bool:
    """
    Valida un email mediante expresión regular.

    Reglas:
    1. Debe ser string.
    2. Se eliminan espacios.
    3. Debe cumplir el patrón estándar de email.

    Devuelve:
        True si el email es válido, False en caso contrario.
    """

    if not isinstance(email, str):
        return False

    email = email.strip()

    return re.match(EMAIL_PATTERN, email) is not None


def generate_flag_pair(is_valid: bool) -> tuple[str, str]:
    """
    Convierte un booleano en un par de flags tipo ETL.

    Reglas:
    - Si es válido (True)  → ("Y", "N")
    - Si es inválido (False) → ("N", "Y")

    Uso típico:
    - Primer valor: flag OK
    - Segundo valor: flag KO

    Devuelve:
        Tupla (ok_flag, ko_flag)
    """
    
    return ("Y", "N") if is_valid else ("N", "Y")