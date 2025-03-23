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
            if os.path.exists(arguments.hash):
                print("Test")
        else:
            print("O arquivo não é um path")
    if arguments.wordlist:
        print(arguments.wordlist)
    if arguments.verbose:
        print(arguments.verbose)
    