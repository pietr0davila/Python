import argparse
import sys
import os

def add_parameters():
    parser = argparse.ArgumentParser(
        prog="Hash-Cracker\nArguments: ",
        description="Program for broke passwords!",
        epilog="Use responsibly"
    )
    parser.add_argument("hash", help="Hash file/text")
    parser.add_argument("-f", action="store_true",
                        help="Place this argument before the hash if it is a file")
    parser.add_argument("-w", "--wordlist", help="Passwords wordlist")
    parser.add_argument("-v", "--verbose", action="store_true", help="Turn on verbose mode")
    args = parser.parse_args()
    treat_parameters(args)
def treat_parameters(arguments):
    if arguments.hash:
        if arguments.f:
            hash_file = arguments.hash
            if os.path.exists(hash_file) and os.access(hash_file, os.R_OK):
                with open(hash_file, "r", encoding="utf-8") as file:
                    file.read()
            else:
                print("File does not exists or you don't have access")
        else:
            pass
    if arguments.wordlist:
        print(arguments.wordlist)
    if arguments.verbose:
        print(arguments.verbose)
    