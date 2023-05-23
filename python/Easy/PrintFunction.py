import math


def main():
    n = int(input())
    power = 0
    solution = 0

    for i in range(n):
        solution = solution + ((10**power) * n)
        power += int(math.log10(n)) + 1
        n -= 1

    print(solution)


main()
