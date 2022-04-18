from selecting_positive import selecting_positive
import inspect
import pytest

def test_not_none():
  assert selecting_positive([10,20,35,74], 13) is not None, "Esperado valor diferente de 'None'"

def test_type():
  assert type(selecting_positive([10,20,35,74], 13)) == list, "Esperado uma lista"

def test_parameters():
  assert len(inspect.getfullargspec(selecting_positive).args) == 2, "Assinatura da função poderá receber apenas dois parâmetros"

@pytest.mark.parametrize("list1, number, expected_result", [
  ([10,20,30,40], 20, [30,40]),
  ([10,20,30], -1, [10,20,30]),
  ([10,15,35], 50, [])
])
def test_selecting_positive(list1, number, expected_result):
  assert selecting_positive(list1, number) == expected_result, f"{expected_result} são os valores em {list1} maiores do que {number}"
