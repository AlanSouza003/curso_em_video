# Tabela de cores
VERMELHO_CLARO  = '\033[1;91m'
VERDE_CLARO     = '\033[1;92m'
AMARELO_CLARO   = '\033[1;93m'
AZUL_CLARO      = '\033[1;94m'
RESET           = '\033[0m'
print(f'{AZUL_CLARO}-={RESET}' * 20)
print(f'{AMARELO_CLARO}ANALISADOR DE TRIÂNGULO{RESET}')
print(f'{AZUL_CLARO}-={RESET}' * 20)
m1 = float(input('Primeira medida: '))
m2 = float(input('Segunda medida: '))
m3 = float(input('Terceira medida: '))
if m2 + m3 > m1 and m1 + m3 > m2 and m1 + m2 > m3:
    print(f'As médidas acima {VERDE_CLARO}PODEM FORMAR{RESET} um triângulo!')
else:
    print(f'As médidas acima {VERMELHO_CLARO}NÃO PODEM FORMAR{RESET}  um triângulo!')
