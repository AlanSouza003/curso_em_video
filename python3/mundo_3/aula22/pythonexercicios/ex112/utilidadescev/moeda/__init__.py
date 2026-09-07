def half(v=0, formt=False):
    """
    -> Mostrando a metade de um valor.
    :param v: Recebe um valor n
    :param formt: (opcional), formata o valor no formato padrão do pais
    :return: o valor ja somado e caso queira também com a formatação da moeda
    """
    s = v / 2
    return s if not formt else moeda(s)


def double(v=0, formt=False):
    """
    -> Mostrando o dobro de um valor.
    :param v: Recebe um valor n
    :param formt: (opcional), formata o valor no formato padrão do pais
    :return: o valor ja somado e caso queira também com a formatação da moeda
    """
    s = v * 2
    return s if not formt else moeda(s)


def rise(v=0, rate=0, formt=False):
    """
    -> Mostrando a soma de uma porcentagem de um valor.
    :param v: Recebe um valor n
    :param rate: (opcional), faz o calcula de um valor com uma porcentagem expecifica
    :param formt: (opcional), formata o valor no formato padrão do pais
    :return: o valor ja somado e caso queira também com a formatação da moeda
    """
    s = v + (v * rate / 100)
    return s if not formt else moeda(s)


def cutback(v=0, rate=0, formt=False):
    """
    -> Mostrando a soma de uma porcentagem de um valor.
    :param v: Recebe um valor n
    :param rate: (opcional), faz o calcula de um valor com uma porcentagem expecifica
    :param formt: (opcional), formata o valor no formato padrão do pais
    :return: o valor ja somado e caso queira também com a formatação da moeda
    """
    s = v - (v * rate / 100)
    return s if not formt else moeda(s)


def moeda(v=0, coin="R$"):
    """
    -> Formatando a moeda para o formato padrão do pais
    :param v: Recebe um valor n
    :param coin: Mostra a sigla da moeda do pais
    :return: O valor formatado
    """
    return f"{coin}{v:.2f}".replace(".", ",")

def summary(v=0, r=0, c=0):
    """
    -> Resumo completo do valor recebido
    :param v: Recebe o valor n
    :param r: Recebe o valor da porcentagem de aumento do valor n
    :param c: Recebe o valor da porcentagem de redução do valor n
    """
    print("─" * 30)
    print(f"RESUMO DO VALOR".center(30))
    print("─" * 30)
    print(f"Preço analizado: ".ljust(20) + f"{moeda(v)}")
    print(f"Dobro do preço: ".ljust(20) + f"{double(v, True)}")
    print(f"Metade do preço: ".ljust(20) + f"{half(v, True)}")
    print(f"{r}% de aumento: ".ljust(20) + f"{rise(v, r,True)}")
    print(f"{c}% de redução: ".ljust(20) + f"{cutback(v, c, True)}")
    print("─" * 30)