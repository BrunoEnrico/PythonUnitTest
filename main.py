from codigo.bytebank import Funcionario

def test_nascimento():
    bruno = Funcionario(nome='Bruno', data_nascimento="13/01/2000", salario=1000)
    return bruno.idade()


print(test_nascimento())