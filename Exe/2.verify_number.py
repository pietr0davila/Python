# Receber um número
# Verificar se ele é Par ou Ímpar
# Verificar se é positivo ou negativo

class InvalidNumberZero(Exception):
    def __init__(self, message): 
        super().__init__(message)
        self.message = message

def get_number():
    while True:
        try:
            input_number = float(input("Digite um número para analisar... "))
            if input_number == 0:
                raise InvalidNumberZero("Zero não é par / impar nem um número positivo / negativo")
             
        except ValueError:
            print("\n[!] Entrada inválida, Digite um número válido")
            continue
        except InvalidNumberZero:
            print("\n[!] ERRO NOS VALORES FORNECIDOS")
            continue
        
        is_odd_or_even(input_number)
        is_positive_or_negative(input_number)

def is_odd_or_even(number):
    if number.is_integer():
        if number % 2 == 0:
            print("O número " + number + " é Par!")
        else: 
            print("O número " + number + " digitado é Ímpar!")
    else:
        print("Não é possível verificar se um número decimal é Par ou ímpar")
        
def is_positive_or_negative(number):
    if number < 0:
        print("O número " + number + " é Negativo!")
    elif number == 0:
        print("O número é 0");
    else: 
        print("O número " + number + " é Positivo")
    
def main():
    get_number()

if __name__ == "__main__":
    main()