# Lendo o sexo do usuário
sexo = str(input('\033[1;97mQual o seu sexo? [M/F]\033[0m')).strip().upper()

# Repete até que o usuário digite uma opção válida (M, MASCULINO, F ou FEMININO)
while sexo not in ['M', 'MASCULINO'] and sexo not in ['F', 'FEMININO']:

   print('\033[1;91mDados incorretos! Tente novamente.\n\033[0m')
   sexo = str(input('\033[1;97mQual o seu sexo? [M/F]\033[0m')).strip().upper()

# Exibe mensagem de confirmação pois o sexo foi validado com sucesso
print(f'\033[1;92mSexo {sexo} cadastrado com sucesso!\033[0m')
