n1 = int(input("Adicione um número: "))
n2 = int(input("Adicione outro número: "))

print("\n- Operações -\n1- Soma\n2- Subtração\n3- Raiz")
op = int(input("Você quer realizar qual operação? "))

if op == 1:
    print(f"{n1} + {n2} = {n1 + n2}")

elif op == 2:
    print(f"{n1} - {n2} = {n1 - n2}")

else:
    print(f"{n1}^2 = {n1 ** (1 / 2)}\n{n2}^2 = {n2 ** (1 / 2)}")
