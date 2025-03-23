import package_operations.calculator.factorial as factorial
import package_operations.calculator.double as double
import package_operations.calculator.triple as triple

input_value = int(input("Digite um número para as operações: "))
print(factorial.factorial(input_value))
print(double.double(input_value))
print(triple.triple(input_value))