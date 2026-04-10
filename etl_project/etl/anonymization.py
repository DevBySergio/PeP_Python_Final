import hashlib
import os

SALT = os.getenv("HASH_SALT")

def hash_value(value: str) -> str:
    if not value:
        return None
    return hashlib.sha256((SALT + value).encode()).hexdigest()