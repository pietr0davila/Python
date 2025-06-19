import argparse
import sys
import os

# Adiciona diretório ao path para permitir a importação de comandos
sys.path.append(os.path.join(os.path.dirname(__file__), "commands"))
from commands.help_command import helpFun

def parse_args():
    # Cria um parser de argumentos
    parser = argparse.ArgumentParser(add_help=False)

    # Define os argumentos esperados
    parser.add_argument('-w', '--wordlist', type=str, help="Especifica a wordlist a ser utilizada.")
    parser.add_argument('-t', '--threads', type=int, default=1, help="Número de threads a ser utilizado (padrão: 1).")
    parser.add_argument('-h', '--hash_type', type=str, help="Especifica o tipo de hash a ser quebrado.")
    parser.add_argument('-f', '--file', type=str, help="Especifica o arquivo com os hashes.")
    parser.add_argument("--help", action="store_true", help="Exibe a ajuda.")

    # Faz o parsing dos argumentos
    args = parser.parse_args()

    # Se o usuário pedir ajuda, chama a função de ajuda e encerra
    if args.help:
        helpFun()
        exit(1)

    # Verifica se os argumentos obrigatórios foram fornecidos
    if not args.wordlist or not args.hash_type or not args.file:
        print("Erro: Os argumentos '-w/--wordlist', '--hash_type' e '-f/--file' são obrigatórios.")
        sys.exit(1)

    return args