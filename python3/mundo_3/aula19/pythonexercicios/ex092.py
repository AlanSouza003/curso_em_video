from datetime import date

employee_details = {}
employee_details['nome'] = str(input("Nome: "))
year_birth = int(input(f"Ano de nascimento de {employee_details['nome']}: "))
employee_details['idade'] = date.today().year - year_birth
employee_details['ctps'] = int(input("Nº da carteira de trabalho (0 não tem): "))
if employee_details['ctps'] >= 0:
    employee_details['adimitido'] = int(input("Ano de contratação: "))
    employee_details['salario'] = float(input("Salário: R$"))
    employee_details['aposentadoria'] = (employee_details['adimitido'] - year_birth) + 35
    print('─' * 30)
    print("<<<<<< DADOS DO FUNCIONÁRIO >>>>>>")
    print('─' * 30)
    for k, v in employee_details.items():
        print(f"{k} tem o valor {v}")
else:
    print('─' * 30)
    for k, v in employee_details.items():
        print(f"{k} tem o valor {v}")
