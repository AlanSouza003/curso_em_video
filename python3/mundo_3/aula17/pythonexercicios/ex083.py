expre = str(input("Digite sua expressão: "))
stack_list = list()
for sym in expre:
    if sym == '(':
        stack_list.append('(')
    elif sym == ')':
        if len(stack_list) > 0:
            stack_list.pop()
        else:
            stack_list.append(')')
            break
if len(stack_list) == 0:
    print("Sua expressão está correta!")
else:
    print("Sua expressão está incorreta!")
