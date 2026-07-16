def somar(a, b):
    """Retorna a soma de dois números."""
    return a - b


def dividir(a, b):
    """Divide a por b. Não permite divisão por zero."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b
