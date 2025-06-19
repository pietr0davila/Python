import sys
# Ler valor de salário mínimo
# Calcular quantos salários minímos o usuário recebe
# Exibir o resultado ("Você ganha {...} salários minímos")
# Base do salário = R$1.293,20

def get_value():
    while True:
        try:
            user_wage = float(input("Digite seu salário atual (formato 1234.56): R$"))
            min_wages = calculate_min_wage(user_wage)
            print_result(min_wages)
            print("Pressione [ctrl+C] para sair")        
        except ValueError:
            print("[ERRO] Digite valores válidos")
        except KeyboardInterrupt:
            print("\nSaindo...")
            sys.exit()
def calculate_min_wage(wage):
    min_wage = 1293.20
    print("Salário minímo: ", min_wage)
    print("Seu salário: ", int(wage))
    wage_count = wage / min_wage
    return wage_count
    
def print_result(result):
    if result >= 1 and result < 2:
        print("Você ganha um salário minímo")
    elif result < 1:
        print("Você ganha menos de um salário minímo")
    else:        
        print(f"Você ganha {int(result)} salários minímos")
    
def main():
    get_value()

if __name__ == "__main__":
    main()