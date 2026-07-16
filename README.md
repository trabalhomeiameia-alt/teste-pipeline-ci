# Exemplo de testes contínuos com GitHub Actions

Este projeto demonstra um pipeline de Integração Contínua (CI) que executa
automaticamente testes em Python usando PyTest.

## Executar localmente

```bash
pip install -r requirements.txt
pytest -v
```

## Pipeline

O arquivo `.github/workflows/testes.yml` executa os testes automaticamente
quando ocorre:

- push na branch `main`;
- pull request direcionado à branch `main`.

## Como demonstrar uma falha

Altere temporariamente a função `somar` em `calculadora.py`:

```python
def somar(a, b):
    return a - b
```

Faça commit e push. O teste `test_somar_dois_numeros` falhará e o pipeline
ficará vermelho. Depois, restaure `return a + b`, faça outro commit e push,
e o pipeline ficará verde.
