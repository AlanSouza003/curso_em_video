# Variaveis de controle
soma = c_mais_caro = c = 0
produto_barato = ''
print(
    '=' * 25
)

print(
    f'{'LOJA PAGUE MAIS':^25} \n'
    f'{'E LEVE MENOS':^25}'
)

print(
    '=' * 25
)

while True:

    nome_produto = str(
        input('Produto: ')
    ).strip()

    valor_produto_str = str(
        input('Valor: R$')
    ).strip()

    valor_limpo = valor_produto_str.replace('.', '')

    valor_final = valor_limpo.replace(',', '.')

    if valor_final.replace('.', '', 1).isdigit():

        valor_produto = float(valor_final)

        soma += valor_produto

        if valor_produto > 1000:

            c_mais_caro += 1

        if c == 0:

            mais_barato = valor_produto
            produto_barato = nome_produto
            c += 1

        else:

            if valor_produto < mais_barato:

                produto_barato = nome_produto
                mais_barato = valor_produto

    else:
        print('VALOR INVÁLIDO!')

    carrinho = str(
        input('Deseja adicionar mais itens? [S/N] ')
    ).strip().upper()

    if carrinho not in ['S', 'SIM']:
        break
    c += 1
soma_format = f'{soma:,.2f}'.replace(
    '.', 'X').replace(',', '.').replace('X', ',')
print(
    '-'*20
)
print(
    f'{'NOTA FISCA':^20}'
    )
print(
    '-'*20
)

print(
    f'Você gastou um total de R${soma_format}\n'
    f'Você comprou {c_mais_caro} produtos acima de R$1.000,00 reais.\n'
    f'O produto mais barato que você comprou foi "{produto_barato.upper()}".\n'
    f'Que custou R${mais_barato}.'
)