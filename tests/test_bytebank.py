from codigo.bytebank import Funcionario
from pytest import mark
import pytest


class TestClass:
    def test_born_date_13_10_2000_must_return_25(self):
        entry = "13/01/2000"
        expected = 25

        test_employee = Funcionario("Bruno", data_nascimento=entry, salario=2500)
        result = test_employee.idade()

        assert result == expected

    @mark.decrescimo_salario
    def test_salario_100000_deve_resultar_em_90000(self):
        entrada = 100000
        esperado = 90000

        funcionario = Funcionario("Paulo Magalhães", data_nascimento="01/01/2000", salario=entrada)

        funcionario.decrescimo_salario()
        result = funcionario.salario
        assert result == esperado

    def test_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000

            funcionario = Funcionario("Paulo Magalhães", data_nascimento="01/01/2000", salario=entrada)
            resultado = funcionario.calcular_bonus()

            return resultado

    def test_print_atributo_str_da_classe(self):
        nome, data_nascimento, salario = "Bruno", "13/01/2000", 100000
        esperado =  f'Funcionario({nome}, {data_nascimento}, {salario})'
        funcionario = Funcionario(nome, data_nascimento, salario)
        esperado = funcionario.__str__()

        assert esperado == esperado

    def test_retorna_nome(self):
        entrada = "Bruno"
        funcionario = Funcionario("Bruno", "13/01/2000", 100000)
        esperado = funcionario.nome

        assert entrada == esperado

    def test_caso_comum_de_bonus(self):
        entrada = 900
        funcionario = Funcionario("Bruno", "13/01/2000", 9000)
        esperado = funcionario.calcular_bonus()
        assert entrada == esperado













