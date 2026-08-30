def notes(*note, situ=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param note: uma ou mais notas dos alunos (aceita várias).
    :param situ: (opcional) indicando se deve ou não adicionar uma situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dic = {}
    dic['total'] = len(note)
    dic['maior'] = max(note)
    dic['menor'] = min(note)
    dic['média'] = sum(note) / len(note)
    if situ:
        if dic['média'] >= 7:
            dic['situação'] = 'BOA'
        elif dic['média'] >= 5:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = 'RUIM'
            
    return dic
reply = notes(3.5, 2, 6.5, 2, 7, 4, situ=True)
print(reply)
# help(notes)
