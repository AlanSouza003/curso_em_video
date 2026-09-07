"""
# Módulos e Pacotes.
- A modularização serve para deixar o código visualmente mais limpo e organizado,
e mais facil de fazer reajustes. Exemplo abaixo:
"""
from uteis import fatorial, dobro, triplo # ? o arquivo "uteis" contém fuções que 
                                          # ? é trazida para o programa principal.

# TODO: Programa Principal
num = int(input("Digite um valor: "))
fat = fatorial(num)
print(f"O fatorial de {num} é {fat}.")
print(f"O dobro de {num} é {dobro(num)}.")
print(f"O triplo de {num} é {triplo(num)}.")

"""
# * Vantagens 

- Organização do código

- Facilidade na manutenção 

- Ocultação de código detalhado

- Reutilização em outros projetos
"""