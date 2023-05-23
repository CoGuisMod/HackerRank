def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    solution = []

    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                sum = i + j + k
                if sum != n:
                    solution.append([i, j, k])

    print(solution)


main()
