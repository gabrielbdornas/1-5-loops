from multiplication_table import (
                                    multiplication_table,
                                    other_multiplication_table
                                )
import inspect
import pytest

def test_not_none():
  assert multiplication_table(3) is not None, "Esperado valor diferente de 'None'"
  assert other_multiplication_table(3) is not None, "Esperado valor diferente de 'None'"

def test_type():
  assert type(multiplication_table(3)) == list, "Esperado uma lista"
  assert type(other_multiplication_table(3)) == list, "Esperado uma lista"

def test_parameters():
  assert len(inspect.getfullargspec(multiplication_table).args) == 1, "Assinatura da função poderá receber apenas um parâmetro"
  assert len(inspect.getfullargspec(other_multiplication_table).args) == 1, "Assinatura da função poderá receber apenas um parâmetro"

@pytest.mark.parametrize("number, expected_result", [
  (3, [3,6,9,12,15,18,21,24,27,30]),
  (5, [5,10,15,20,25,30,35,40,45,50]),
])
def test_multiplication_table(number, expected_result):
  assert multiplication_table(number) == expected_result, f"A tabuada do {number} é {expected_result}"

@pytest.mark.parametrize("number, expected_result", [
  (3, [3,6,9,12,15,18,21,24,27,30]),
  (5, [5,10,15,20,25,30,35,40,45,50]),
])
def test_other_multiplication_table(number, expected_result):
  assert other_multiplication_table(number) == expected_result, f"A tabuada do {number} é {expected_result}"
