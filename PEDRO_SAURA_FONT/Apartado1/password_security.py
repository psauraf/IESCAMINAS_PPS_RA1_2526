import math
import random
import string
from dataclasses import dataclass


@dataclass
class PasswordAnalysis:
    length: int
    charset_size: int
    entropy_bits: float
    classification: str


def calculate_charset_size(password: str) -> int:
    """Calcula el tamaño del conjunto de caracteres usado en la contraseña."""
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digits = any(c.isdigit() for c in password)
    symbols_set = set(string.punctuation)
    has_symbols = any(c in symbols_set for c in password)

    size = 0
    if has_lower:
        size += 26
    if has_upper:
        size += 26
    if has_digits:
        size += 10
    if has_symbols:
        size += len(symbols_set)
    return size


def calculate_entropy(password: str) -> float:
    """
    Entropía aproximada en bits: H ≈ length * log2(charset_size)
    """
    if not password:
        return 0.0

    charset_size = calculate_charset_size(password)
    if charset_size == 0:
        return 0.0

    return len(password) * math.log2(charset_size)


def classify_entropy(entropy_bits: float) -> str:
    """
    Clasifica la contraseña según la entropía.

      < 28   -> Muy débil
      28-35  -> Débil
      36-59  -> Media
      60-127 -> Fuerte
      >=128  -> Muy fuerte
    """
    if entropy_bits < 28:
        return "Muy débil"
    elif entropy_bits < 36:
        return "Débil"
    elif entropy_bits < 60:
        return "Media"
    elif entropy_bits < 128:
        return "Fuerte"
    else:
        return "Muy fuerte"


def analyze_password(password: str) -> PasswordAnalysis:
    """Devuelve un objeto con el análisis completo de la contraseña."""
    length = len(password)
    charset_size = calculate_charset_size(password)
    entropy_bits = calculate_entropy(password)
    classification = classify_entropy(entropy_bits)

    return PasswordAnalysis(
        length=length,
        charset_size=charset_size,
        entropy_bits=entropy_bits,
        classification=classification,
    )


def generate_password(
    length: int = 16,
    use_lower: bool = True,
    use_upper: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """Genera una contraseña aleatoria con las características indicadas."""
    if length <= 0:
        raise ValueError("La longitud debe ser mayor que 0.")

    charset = ""
    if use_lower:
        charset += string.ascii_lowercase
    if use_upper:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += string.punctuation

    if not charset:
        raise ValueError("Debe activarse al menos un tipo de carácter.")

    return "".join(random.choice(charset) for _ in range(length))
