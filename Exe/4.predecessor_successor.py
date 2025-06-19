# Recebe um número
# Imprime seu sucessor
# Imprime seu antecessor

def get_values():
    while True:
        try: 
            input_number = int(input("Digite o número: "))
            print("O número digitado é: ", input_number)
            get_predecessor(input_number)
            get_successor(input_number)
            
        except ValueError:
            print("[ERRO] Valor inválido digitado, tente novamente")
            continue

def get_predecessor(number):
    print("O seu antecessor é: ", number - 1)

def get_successor(number):
    print("O seu sucessor é: ", number + 1)

def main():
    get_values()

if __name__ == "__main__":
    main()