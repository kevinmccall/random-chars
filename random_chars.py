import argparse
import os
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
from random import randrange
from pathlib import Path


def generate_random_chars(bank: str, num_chars: int):
    res = ""
    for _ in range(num_chars):
        res += bank[randrange(0, len(bank))]
    return res


def get_alpha_chars(string):
    return [char for char in string if char.isalpha()]


def file_validator(string):
    if os.path.isfile(string):
        return string
    else:
        raise FileNotFoundError(string)


def main():
    parser = argparse.ArgumentParser(
        prog="Random Character Generator",
        description="Generates random characters for me to type in monkeytype",
    )
    default_bank = ascii_lowercase + " "
    parser.add_argument("num_chars", type=int)
    parser.add_argument("--character-list", type=str, default=default_bank)
    parser.add_argument("--input-file", type=file_validator)
    parser.add_argument("--add-uppercase", action="store_true")
    parser.add_argument("--add-numbers", action="store_true")

    args = parser.parse_args()
    bank = args.character_list
    if args.input_file:
        bank = Path(args.input_file).read_text().replace("\n", "")
    if args.add_uppercase:
        bank += "".join(get_alpha_chars(bank)).upper()
    if args.add_numbers:
        bank += digits
        

    result = generate_random_chars(bank, args.num_chars)

    print(result)


if __name__ == "__main__":
    main()
