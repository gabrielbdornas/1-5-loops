from factorial import factorial

import inspect
import pytest

def test_not_none():
  assert factorial(3) is not None, "Esperado valor diferente de 'None'"

def test_type():
  assert type(factorial(3)) == int, "Esperado valor numérico"

def test_parameters():
  assert len(inspect.getfullargspec(factorial).args) == 1, "Assinatura da função poderá receber apenas um parâmetro"

@pytest.mark.parametrize("number, expected_result", [
  (3, 6),
  (5, 120),
  (7, 5040)
])
def test_factorial(number, expected_result):
  assert factorial(number) == expected_result, f"O fatorial de {number} é {expected_result}"