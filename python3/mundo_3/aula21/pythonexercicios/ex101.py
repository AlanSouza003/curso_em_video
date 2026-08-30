def vote(yearbirth):
    """
    -> Função criada para verificar se uma pessoa pode votar ou não.

    Args:
        yearbirth (int): Parâmetro criado para receber o ano de nascimento de uma pessoa 
        para verificar se é maior de 18 anos, menor de 18 anos ou se tem mais de 69 anos.

    Returns:
        bool: Retorna a classificação do voto de acordo com sua idade.
    """
    from datetime import date
    age = date.today().year - yearbirth
    if 18 <= age < 69:
        return f"Com {age} anos: VOTO OBRIGATÓRIO."
    elif 16 <= age <= 17  or age >= 70:
        return f"Com {age} anos: VOTO OPCIONAL."
    else:
        return f"Com {age} anos: NÃO VOTA."

# TODO: Main Program

year = int(input("Digite seu ano de nascimento: "))
print(vote(year))