# ERROS, EXCEÇÕES E SEUS TRATAMENTOS.

## EXCEÇÕES
"""
n = int(input('Número: '))
print(f"O valor digitado foi o {n}.")

-> O código acima aparentemente não apresenta nenhum erro. Mas, se observarmos, ele pode
apresentar erro. Exemplo: Se eu digitar o valor '8', ele vai aceitar normalmente, mas,
se eu digitar 'oito' por extenso ele vai dar ValueError. No caso o código esta 100% correto
o que acontece é uma exceção.
"""
## Exemplo 2:
"""
a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a / b
print(f"O resultado foi: {r}")

-> Como no código acima, este também esta 100% correto, porém, na matematica sabemos
que a divisão por 0 é um problema, caso o usuário digite 0, o python vai retornar uma mensagem
dizendo "ZeroDivisionError", pois o 0 não existe na divisão de número inteiros e reias.
"""
# >>> É para lidarmos com isso usamos o comando "Try except".
#   => Dentro de try colocamos a operação e em except colocamos a falha.

