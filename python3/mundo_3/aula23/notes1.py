try: # |> Operação
    a = int(input("Numerador: ")) 
    b = int(input("Denominador: "))
    r = a / b
except Exception as erro: # |> Falhou 
    print(f"Problema encontrado foi: {erro}\nDa tipo: {erro.__class__}")
except KeyboardInterrupt: # |> Falhou
    print("\nO usuário interrompeu o programa!")
else: # |> Deu certo 
    print(f"O resultado foi: {r}")
finally: # |> Certo/Falha
    print("Volte sempre! Muito obrigado!")
