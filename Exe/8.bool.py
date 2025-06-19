# Lê 2 valores booleanos (true/0 - false/1)
# imprime se os 2 são verdadeiros ou não 
def main():
    while True:
        value_A = int(input("Digite um valor entre 0 e 1: "))
        if value_A < 0 or value_A > 2:
            print("Valor 1 inválido, atribuindo para 1")
            value_A = 1
        value_B = int(input("Digite um valor entre 0 e 2: "))
        if value_B < 0 or value_B > 2:
            print("Valor 2 inválido, atribuindo para 1")
            value_B = 1
        treat_bool(value_A, value_B)
def treat_bool(a, b):
    if a == 0 and b == 0:
        print("Os 2 valores são true (0)")
    elif a == 1 and b == 1:
        print("Os 2 valores são falsos (1)")
    else:
        print("Os 2 valores são diferentes (0/1)")
if __name__ == "__main__":
    main()
