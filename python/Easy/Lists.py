def main():
    n = int(input())
    list = []

    for i in range(n):
        line = input().split()

        command = line[0]

        firsValue = 0
        if len(line) >= 2:
            firsValue = int(line[1])

        secondValue = 0
        if len(line) >= 3:
            secondValue = int(line[2])

        if command == "insert":
            list.insert(firsValue, secondValue)

        if command == "print":
            print(list)

        if command == "remove":
            list.remove(firsValue)

        if command == "append":
            list.append(firsValue)

        if command == "sort":
            list.sort()

        if command == "pop":
            list.pop()

        if command == "reverse":
            list.reverse()


main()
