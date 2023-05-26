def main():
    n = int(input())
    words = {}
    counter = 0
    appearances = ""

    for i in range(n):
        word = input()

        if words.get(word) == None:
            counter += 1
            words[word] = 1
        else:
            words[word] += 1

    for x in words:
        value = str(words[x])

        if len(appearances) == 0:
            appearances = value
            continue

        appearances += " " + value

    print(counter)
    print(appearances)


main()
