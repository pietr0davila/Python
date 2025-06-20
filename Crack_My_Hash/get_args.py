import argparse

def create_args():
    parser = argparse.ArgumentParser (
        prog="\n===== Crack My Hash =====\n",
        description="Use main.py --help command to see all the options",
        epilog="Project made for educational purposes\n",
    )
    args = parser.parse_args()
    parser.add_argument("hash", help="Hash to be cracked, first positional argument")
    parser.add_argument("wordlist", help="wordlist that will be used to crack the hash, second positional arguments")
    parser.add_argument("-ht", "--hash_type", help="hash Type, use --type_help to get all the options")
    parser.add_argument("--type_help")
    if not args.hash:
        print("O argumento hash é obrigatório[1], ele indica o hash a ser quebrado")
    if not args.wordlist:
        print("O argumento wordlist[2] é obrigatório, ele indica a wordlist usada para quebrar o hash")
    
