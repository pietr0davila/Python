# Ler 3 valores diferentes
# Exibir os 3 em ordem decrescentes (Menor para o menor)
# E.g: 1, 2, 3

def main():
    numbers = []
    for i in range(3):
        number = float(input("Digite um número: "))
        numbers.append(number)
        numbers.sort()

    print(f"Número 1: {numbers[0]}")
    print(f"Número 2: {numbers[1]}")
    print(f"Número 3: {numbers[2]}")

if __name__ == "__main__":
    main()
