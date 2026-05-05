"""
MÓDULO: etl.anonymization

RESPONSABILIDAD:
- Proteger datos sensibles mediante hashing.

FUNCIONES:

1. hash_value(value)
   - Aplica SHA-256 con SALT
   - Retorna hash hexadecimal

VARIABLES:
- HASH_SALT (desde config/env)

CAMPOS A ANONIMIZAR:
- DNI → dni_hash
- numero_tarjeta → numero_tarjeta_hash
- CVV → cvv_hash

INTERACCIÓN:
- transformer.py

IMPORTANTE:
- Nunca almacenar datos sensibles en claro
"""
import hashlib
from etl.config import HASH_SALT

def hash_value(value: str) -> str:
    if value is None:
        value = ""
    raw = f"{HASH_SALT}{value}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()