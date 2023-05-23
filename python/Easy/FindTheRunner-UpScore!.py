def main():
    n = int(input())
    scores = input().split()

    first_runner = None
    second_runner = None

    for x in scores:
        score = int(x)

        if first_runner == None:
            first_runner = score
            continue

        if score > first_runner:
            second_runner = first_runner
            first_runner = score
            continue

        if score < first_runner and second_runner == None:
            second_runner = score
            continue

        if score < first_runner and score > second_runner:
            second_runner = score
            continue

    print(second_runner)


main()
