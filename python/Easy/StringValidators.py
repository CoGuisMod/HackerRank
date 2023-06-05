def main(string):
    has_alphanum = False
    has_alphabet = False
    has_digits = False
    has_lowercase = False
    has_uppercase = False

    lowercase_abc = "abcdefghijklmnopqrstuvwxyz"
    uppercase_abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for x in string:
        if x in lowercase_abc:
            has_alphabet = True
            has_lowercase = True
        elif x in uppercase_abc:
            has_alphabet = True
            has_uppercase = True
        else:
            try:
                number = int(x)
                has_digits = True
            except:
                continue

    if has_alphabet or has_digits:
        has_alphanum = True

    print(has_alphanum)
    print(has_alphabet)
    print(has_digits)
    print(has_lowercase)
    print(has_uppercase)


string = "123"
main(string)
