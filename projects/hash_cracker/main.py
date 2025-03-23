from package.arguments import add_parameters
"""
- Permitir que o usuário forneça o hash para quebrar
- Especificar o algoritmo usado
- Permitir ataques de dicionário
    - Abrir arquivo de dicionário
- Permitir ataque de força bruta - No futuro!!
- Converter cada palavra no algoritmo de criptografia e testar se os hashs são iguais
- Modo verbose para exibir cada tentativa incluindo erros
- Exibir se o resultado foi positivo ou não e o tempo do processo
- Alterar o número de threads

"""
def main():
    add_parameters()

if __name__ == "__main__":
    main()