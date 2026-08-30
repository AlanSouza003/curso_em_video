def par(n=0):
    """
    -> Valores pares.

    Args:
        n (int): Ler um qualquer valor e depois verifica se o valor é par. Defaults to 0.

    Returns:
        bool: Retorna Verdadeiro se o valor for par, se for impar retorna Falso.
    """
    if n % 2 == 0:
        return True
    else:
        return False 
# TODO: Main Program
num = int(input("Digite um valor par: "))
if par(num):
    print(f"O valor {num} é par.")
else:
    print(f"O valor {num} não é par.")
help(par)