# 🧪 PythonUnitTest

Projeto pessoal com o objetivo de praticar testes unitários em Python utilizando a biblioteca `pytest`.

A aplicação simula um sistema simples de Recursos Humanos, com regras de negócio aplicadas à classe `Funcionario`.

---

## 📁 Estrutura do Projeto

PythonUnitTest/
<pre>
  
├── codigo/
    └── bytebank.py
├── coverage.xml
├── main.py
├── pytest.ini
├── report.xml
├── requirements.txt
└── tests/
    ├── __init__.py
    └── test_bytebank.py
</pre>

---

## ⚙️ Funcionalidades

A classe `Funcionario` oferece os seguintes métodos:

- `idade()` – Calcula a idade com base na data de nascimento no formato `DD/MM/AAAA`.
- `sobrenome()` – Retorna o sobrenome do funcionário.
- `decrescimo_salario()` – Aplica uma redução de 10% em salários acima de R$ 100.000, caso o sobrenome seja "Magalhães" ou "Silva".
- `calcular_bonus()` – Retorna 10% do salário como bônus. Lança exceção se o valor exceder R$ 1.000.
- `__str__()` – Representação legível do objeto `Funcionario`.

---

## ✅ Testes Automatizados

Os testes cobrem os seguintes casos:

- Cálculo correto da idade.
- Aplicação do desconto salarial em condições específicas.
- Tratamento de exceções no cálculo do bônus.
- Verificação da representação textual (`__str__`).
- Retorno correto do nome.
- Cálculo de bônus dentro do limite permitido.

---

## ▶️ Como Executar os Testes

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/BrunoEnrico/PythonUnitTest.git
   cd PythonUnitTest

👨‍💻 Este projeto é de uso pessoal apenas para fins educacionais.
