import re


def replace(match):
    if match.group() == "&&":
        return "and"
    else:
        return "or"


def main():
    n = int(input())
    strings = []

    for _ in range(n):
        string = input()

        replaced_string = re.sub(r"(?<= )([&]{2}|[|]{2})(?= )", replace, string)

        print(replaced_string)


main()
