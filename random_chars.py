import argparse
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
from random import randrange

WORD_BANK_LOC = "./google-10000-english-usa-no-swears.txt"


def generate_random_chars(bank: str, num_chars: int):
    res = ""
    for _ in range(num_chars):
        res += bank[randrange(0, len(bank))]
    return res


def get_alpha_chars(string):
    return [char for char in string if char.isalpha()]


def splice_str(string, new_string, location):
    if location + len(new_string) > len(string):
        raise IndexError("Replaced string is outside bounds of current string")
    return string[:location] + new_string + string[location + len(new_string) :]


def generate_random_char_word(bank):
    res = ""
    while True:
        next_char = bank[randrange(0, len(bank))]
        if next_char == " ":
            break
        res += next_char
    return res


def splice_random_words(word_source, text, count):
    res = text
    for _ in range(count):
        rand_word = word_source[randrange(0, len(word_source))]
        if len(rand_word) > len(text):
            continue
        rand_index = randrange(0, len(text) - len(rand_word))
        res = splice_str(res, rand_word, rand_index)
    return res


def main():
    parser = argparse.ArgumentParser(
        prog="Random Character Generator",
        description="Generates random characters for me to type in monkeytype",
    )
    default_bank = ascii_lowercase + " "
    parser.add_argument("num_chars", type=int)
    parser.add_argument("--character-list", type=str, default=default_bank)
    parser.add_argument("--add-uppercase", action="store_true")
    parser.add_argument("--add-numbers", action="store_true")
    parser.add_argument("--intersperse-real-words", action="store_true")
    parser.add_argument("--word-bank", type=str, default=WORD_BANK_LOC)

    args = parser.parse_args()
    bank = args.character_list
    word_bank_loc = args.word_bank
    if args.add_uppercase:
        bank += "".join(get_alpha_chars(bank)).upper()
    if args.add_numbers:
        bank += digits

    result = generate_random_chars(bank, args.num_chars)
    if args.intersperse_real_words:
        with open(word_bank_loc, "r", encoding="utf-8") as reader:
            word_bank = [word.strip() for word in reader.readlines()]
            result = splice_random_words(word_bank, result, args.num_chars // 100)

    print(result)


if __name__ == "__main__":
    main()
