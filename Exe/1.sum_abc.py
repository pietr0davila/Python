# Receber números A, B e C (num_1, num_2, num_3)
# Somar Número A com número B
# Verificar se sum (Soma de A e B) é maior que C

def get_numbers():    
    try: 
        number_A = float(input("Digite o número A: "))
        number_B = float(input("Digite o número B: "))
        number_C = float(input("Digite o número C: "))
    
    except ValueError:
        return get_numbers()
    
    return number_A, number_B, number_C

def verify_numbers(a, b, c):
    sum_ab = a + b

    if sum_ab > c:
        return "A soma de A e B é maior que C"
    elif sum_ab == c:
        return "A soma de A e B é igual a C"
    else: 
        return "A soma de A e B é menor que C"

def main():
    number_A, number_B, number_C = get_numbers()
    result = verify_numbers(number_A, number_B, number_C)
    print(result)

if __name__ == "__main__":
    main()