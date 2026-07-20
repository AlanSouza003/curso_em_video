import os
from time import sleep
tabela_brasileirao = (
    "Palmeiras", "Flamengo", "Fluminense", "Athletico-PR", "Bragantino", "Bahia", "Coritiba",
    "São Paulo", "Athletico-MG", "Corinthians", "Cruzeiro", "Botafogo", "EC Vitória",
    "Internacional", "Santos", "Grêmio", "Vasco da Gama", "Remo", "Mirassol", "Chapecoense" 
)
def limpatela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def continuar_programa():
    while True:
        continuar = str(
            input("Deseja escolher outra opção? [S/n] ")
        ).lower()
        if continuar in ["s", "sim"]:
            return True
        elif continuar in ["n", "nao", "não"]:
            print("Saindo do programa", end="")
            for c in range(3):
                print(f'.', end="", flush=True)
                sleep(1)
            print()
            return False
        else:
            print("Valor incorreto! Tente novamente.")
            
def barra_processando(texto="PROCESSANDO"):
    for i in range(21):
        barra = "█" * i + "░" * (20 - i)
        print(f'\r\033[1;92m[{barra}] {i * 5}%\033[0m', end="", flush=True)
        sleep(0.09)
    print()
while True:
    limpatela()
    try:
        print(
            f"DIGITE UMAS DAS OPÇÕES ABAIXO:\n"
            f"[ 1 ] MOSTRAR A TABELA DO BRASILEIRÃO\n"
            f"[ 2 ] OS 5 PRIMEIROS COLOCADOS\n"
            f"[ 3 ] OS 4 ÚLTIMOS COLOCADOS\n"
            f"[ 4 ] TIMES EM ORDEM ALFABÉTICA\n"
            f"[ 5 ] VER A POSIÇÃO DO SEU TIME FAVORITO."
        )
        opcao = int(
            input("Digite a sua opção [ou 0 para encerrar]: ")
            )
        if opcao == 0:
            break
        if opcao > 5:
            print("Digite valores de 1 até 5 ou 0 para encerrar.")
            input("Der enter para continuar")
            continue
    except ValueError:
        print("Valor incorreto! Tente novamente.")
        input("Der enter para continuar")
        continue
    barra_processando()
    if opcao == 1:
        limpatela()
        print("CLASSIFICAÇÃO")
        print("--------------")
        for posicao, time in enumerate(tabela_brasileirao):
            print(f"{posicao+1:>2} - {time}")
    elif opcao == 2:
        limpatela()
        print("Os cincos primeiros colocados da tabela são:")
        for posicao in range(0, len(tabela_brasileirao[0:5])):
            print(f"{posicao+1} - {tabela_brasileirao[posicao]}")
    elif opcao == 3:
        limpatela()
        print("Os quatros ultimos colocados são:")
        for posicao, time in enumerate(tabela_brasileirao):
            if posicao >= 16:
                print(f"{posicao+1} - {tabela_brasileirao[posicao]}")
    elif opcao == 4:
        limpatela()
        print("Times em ordem alfabética:")
        ordem_alfabetica = sorted(tabela_brasileirao)
        for ordem in range(0, len(ordem_alfabetica)):
            print(f"{ordem+1:>2} - {ordem_alfabetica[ordem]}")
    elif opcao == 5:
        time_favorito = str(
            input("Digite o nome do time que deseja ver a classificação: ")
        )
        print("Classificação:")
        print("---------------")
        for posicao, filtro in enumerate(tabela_brasileirao):
            if filtro.count(time_favorito):
                print(f"{posicao+1} - {filtro}")
    print()
    if not continuar_programa():
        break
