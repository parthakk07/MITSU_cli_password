import argparse
import random
import string

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--length", type=int)
parser.add_argument("-c", "--count", type=int)
parser.add_argument("-n", "--numbers", action="store_true")
parser.add_argument("-u", "--uppercase", action="store_true")
parser.add_argument("-s", "--special", action="store_true")

args = parser.parse_args()

if args.count is None:
    args.count = 1

for i in range(args.count):
    all_char = string.ascii_lowercase
    if args.uppercase:
        all_char += string.ascii_uppercase
    if args.special:
        all_char += string.punctuation
    if args.numbers:
        all_char += string.digits
    password = random.choices(all_char, k=args.length)
    print("".join(password))
