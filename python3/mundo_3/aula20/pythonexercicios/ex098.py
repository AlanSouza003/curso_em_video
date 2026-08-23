from time import sleep
def count(start, end, step):
    print('─' * 50)
    print(f"CONTAGEM DE {start} ATE {end} DE {step} EM {step}...")
    sleep(1)
    if start < end:
        for c in range(start, end+1, step):
            print(c, end=' -> ', flush=True)
            sleep(0.9)
    else:
        for c in range(start, end-1, -step):
            print(c, end=' -> ', flush=True)
            sleep(0.9)
    print("FIM!")

# TODO: Main Program
count(1, 10, 1)
count(10, 0, 2)
print('─' * 50)
print("AGORA, VOCÊ PERSONALIZA SUA CONTAGEM...")
s = int(input("Inicio: "))
e = int(input("Fim: "))
st = int(input("Passos: "))
if st <= 0:
    st = st * -1
    if st == 0:
        st = 1
count(s, e, st)
