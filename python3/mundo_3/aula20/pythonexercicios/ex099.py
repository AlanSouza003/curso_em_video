from time import sleep
def bigger(*num):
    count = big = 0
    print("Analise dos valores passados...")
    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.9)
        count += 1
        if n > big:
            big = n
    print(f"Foram informados {count} valores ao todo.\nO maior valor foi o {big}.")
    print('─' * 50)

# TODO: Main Program
bigger(2, 9, 4, 5, 7, 1)
bigger(4, 7, 0)
bigger(1, 2)
bigger(6)
bigger()
