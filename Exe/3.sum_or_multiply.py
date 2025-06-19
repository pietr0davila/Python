from time import sleep
"""
Receber 2 números (A e B)
Se os 2 valores forem iguais, somar A com B
Senão multiplicar A por B
Em todas as circunstâncias, armazenar e exibir o valor em uma variável C
"""

def get_values():
    try:
        number_A = float(input("Digite um número: "))
        number_B = float(input("Digite outro número: "))
        is_equal_result = is_equal(number_A, number_B)
        number_C = calculate_result(is_equal_result, number_A, number_B)
        return number_C
    except ValueError:
        print("[ERRO] Digite caracteres válidos!")
        
def is_equal(number1, number2):
    if number1 == number2:
        print("Os números são iguais")
        print("Somando...")
        sleep(1.5)
        return True
    else:
        print("Os números são diferentes")
        print("Multiplicando...")
        sleep(1.5)
        return False

def calculate_result(is_equal, number1, number2):
    if is_equal:
        number_C = number1 + number2
    else:
        number_C = number1 * number2
    return number_C
    
def main():
    print(get_values())

if __name__ == "__main__":
    main()