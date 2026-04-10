import re

def validate_dni(dni: str) -> bool:
    if not dni:
        return False

    dni = dni.strip().upper()
    pattern = r'^\d{8}[A-Z]$'

    if not re.match(pattern, dni):
        return False

    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    number = int(dni[:-1])
    letter = dni[-1]

    return letters[number % 23] == letter


def validate_phone(phone: str) -> bool:
    if not phone:
        return False

    phone = re.sub(r'\D', '', phone)

    return len(phone) >= 9


def validate_email(email: str) -> bool:
    if not email:
        return False

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None