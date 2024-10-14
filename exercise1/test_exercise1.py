import unittest

#função str_to_bool
def str_to_bool(value):
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False
    
class TestStrToBool(unittest.TestCase): #a classe para testar o metodo acima

    def test_y_is_true(self): #verifica se o result existe o 'y' na string
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self): #verifica se o result existe o 'Yes' na string
        result = str_to_bool('Yes')
        self.assertTrue(result)

    def test_invalid_input(self): #verifica se o result teve alguma inserção invalida
        with self.assertRaises(AttributeError):
            str_to_bool(1)

if __name__ == '__main__':
    unittest.main() #executar o arquivo  diretamente
    
'''#correção
def str_to_bool(value):
    try:
        value = value.lower()
    except AttributeError:
        raise AttributeError(f"{value} must be of type string")
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False
    
def test_invalid_input(self):
        with self.assertRaises(AttributeError):
            str_to_bool(1)'''
