# Ler um número
# Exibir o número com reajuste de 5% 

def main():
    while True:
        try:
            number = float(input("Digite o número: "))
            treat_number(number)
        except ValueError:
            print("Digite um número válido")

def treat_number(value):
    percent = (value * 5) / 100
    value_plus_percent = value + percent
    value_minus_percent = value - percent
    print(f"O Valor digitado acrescido a 5% é: {value_plus_percent}\
    O valor digitado decrescido 5% é: {value_minus_percent}")

if __name__ == "__main__":
    main()
