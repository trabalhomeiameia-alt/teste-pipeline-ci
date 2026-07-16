import pytest

from calculadora import dividir, somar


def test_somar_dois_numeros():
    assert somar(2, 3) == 5


def test_somar_numero_negativo():
    assert somar(-2, 5) == 3


def test_dividir_dois_numeros():
    assert dividir(10, 2) == 5


def test_dividir_por_zero():
    with pytest.raises(ValueError, match="Não é possível dividir por zero"):
        dividir(10, 0)
