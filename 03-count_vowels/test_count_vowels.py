from count_vowels import count_vowels
import inspect
import pytest

def test_not_none():
  assert count_vowels('string') is not None, "Esperado valor diferente de 'None'"

def test_type():
  assert type(count_vowels('string')) == int, "Esperado valor numérico"

def test_parameters():
  assert len(inspect.getfullargspec(count_vowels).args) == 1, "Assinatura da função poderá receber apenas um parâmetro"

@pytest.mark.parametrize("string, expected_result", [
  ('texto', 2),
  ('qualquer palavra', 7),
  ('palavras sem acento', 7)
])
def test_count_vowels(string, expected_result):
  assert count_vowels(string) == expected_result, f"A quantidade de vogais em {string} é {expected_result}"