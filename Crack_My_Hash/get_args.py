import argparse

def create_args():
    parser = argparse.ArgumentParser (
        prog="\n===== Crack My Hash =====\n",
        description="Use main.py --help command to see all the options",
        epilog="Project made for educational purposes\n",
    )

    parser.add_argument("hash", help="Hash to be cracked, first positional argument")
    parser.add_argument("wordlist", help="wordlist that will be used to crack the hash, second positional arguments")
    parser.add_argument("-ht", "--hash_type", help="hash Type, use --hash_type_help to get all the options")
    