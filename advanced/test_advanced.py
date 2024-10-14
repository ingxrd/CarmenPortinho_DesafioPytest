import pytest
import os

# Função str_to_bool
def str_to_bool(string):
    if string.lower() in ['yes', 'y', '1']:
        return True
    elif string.lower() in ['no', 'n', '0']:
        return False

# Testes para a função str_to_bool
@pytest.mark.parametrize("string", ['Y', 'y', '1', 'YES'])
def test_str_to_bool_true(string):
    assert str_to_bool(string) is True

@pytest.mark.parametrize("string", ['N', 'n', '0', 'NO'])
def test_str_to_bool_false(string):
    assert str_to_bool(string) is False






















# Método final para limpar, o arquivo temporário apos a conclusão dos testes
@pytest.fixture
def tmpfile(tmpdir):
    def write():
        file = tmpdir.join("done")
        file.write("1")
        return file.strpath
    return write

class TestFile:
    """
    Criada um arquivo temporário no `path` do sistema, mesmo que não saiba o caminho direto,
    o uso do `tempfile()` faz a criação desse arquivo temporário.
    faz a abertura e criação no comando `_f.read()`
    faz a `assert`, "escreve" no arquivo o numero 1 para realizarmos os módulos:
    `test_str_to_bool_true` e `test_str_to_bool_false`
    
    Obs: A palavra-chave `assert` permite que você teste se uma condição no seu código retorna `True`, caso contrário, o programa irá gerar um `AssertionError`.
    """

    def test_f(self, tmpfile):
        path = tmpfile()
        with open(path) as _f:
            contents = _f.read()
        assert contents == "1"