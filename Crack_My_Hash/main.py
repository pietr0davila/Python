from get_args import create_args
import argparse
# Script que quebra senhas usando wordlists
# 1. Precisa de leitura de todas as palavras da wordlist
# 2. precisa transformar o texto da wordlist no hash correspondente
# 3. Compara o hash da palavra com o hash fornecido pelo usuário

# Funções: 
# 1. suporte a vários tipos de hash (Hashlib)
# 2. Argumentos via Cli - --hash, --wordlist, --type...

if __name__ == "__main__":
    
