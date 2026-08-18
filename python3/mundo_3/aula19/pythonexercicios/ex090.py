dict_student = {}

dict_student['name'] = str(input('Nome: '))
dict_student['average'] = float(input(f'Média de {dict_student["name"]}: '))
if dict_student['average'] >= 7:
    dict_student['status'] = "Aprovado!"
elif 5 <= dict_student['average'] < 7:
    dict_student['status'] = 'Recuperação!'
else:
    dict_student['status'] = "Reprovado!"
print(f"O nome é igual á {dict_student['name']}")
print(f"A média é igual á {dict_student['average']}")
print(f"A situação é igual á {dict_student['status']}")
