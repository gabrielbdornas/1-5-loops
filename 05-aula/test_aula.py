from aula import (
                  approved_alunes,
                  approved_alunes_names,
                  count_letters
                )
import inspect
import pytest

def test_not_none():
  assert approved_alunes() is not None, "Esperado valor diferente de 'None'"
  assert approved_alunes_names() is not None, "Esperado valor diferente de 'None'"
  assert count_letters('string') is not None, "Esperado valor diferente de 'None'"

def test_type():
  assert type(approved_alunes()) == int, "Esperado valor numérico"
  assert type(approved_alunes_names()) == list, "Esperado uma lista"
  assert type(count_letters('string')) == dict, "Esperado um dicionário"

def test_parameters():
  assert len(inspect.getfullargspec(approved_alunes).args) == 0, "Assinatura da função não recebe parâmetros"
  assert len(inspect.getfullargspec(approved_alunes_names).args) == 0, "Assinatura da função não recebe parâmetros"
  assert len(inspect.getfullargspec(count_letters).args) == 1, "Assinatura da função poderá receber apenas um parâmetro"

@pytest.mark.parametrize("expected_result", [
  3
])
def test_approved_alunes(expected_result):
  assert approved_alunes() == expected_result, f"Apenas {expected_result} 3 alunos foram aprovados"

@pytest.mark.parametrize("expected_result", [
  ['Tulio', 'Rafaela', 'Fernando']
])
def test_appoved_alunes_names(expected_result):
  assert approved_alunes_names() == expected_result, f"Apenas os alunos {expected_result} foram aprovados"

@pytest.mark.parametrize("string, expected_result", [
  ('texto', {'t':2, 'e':1, 'o':1, 'x':1}),
  ('palavra', {'p':1, 'a':3, 'l':1, 'v':1, 'r':1}),
  ('banana', {'b':1, 'a':3, 'n':2})
])
def test_count_letters(string, expected_result):
  assert count_letters(string) == expected_result, f"A quantidade de vezes que cada letra aparece na palavra {string} é {expected_result}"
  