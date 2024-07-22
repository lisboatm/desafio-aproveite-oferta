T = int(input("Digite o número de casos de teste: "))

for _ in range(T):
    entrada = input("Digite N e K separados por espaço: ").strip()

    # Verifica se a entrada não está vazia
    if entrada:
        entrada = entrada.split()

        # Verifica se a entrada tem pelo menos dois elementos
        if len(entrada) >= 2:
            N = int(entrada[0])
            K = int(entrada[1])

            garrafas_cheias = N // K
            garrafas_vazias = N % K

            # O total de garrafas cheias e vazias
            total = garrafas_cheias + (1 if garrafas_vazias > 0 else 0)
            print(total)
        else:
            print("Entrada inválida: menos de dois valores fornecidos.")
    else:
        print("Entrada vazia ou inválida.")
