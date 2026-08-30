def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    from time import sleep
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f"{c} x ".replace('1 x', '1 ='), end='', flush=True)
            sleep(0.9)
            f *= c
        else:
            f *= c
    return f
# TODO: Main Program
print(fatorial(5, True))
