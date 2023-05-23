def main():
    n = int(input())
    students = []

    lowest_score = []
    second_lowest = []

    for i in range(n):
        name = input()
        score = float(input())
        student = [name, score]

        students.append(student)

        if lowest_score == []:
            lowest_score.append(student)
            continue

        if score < lowest_score[0][1]:
            second_lowest = lowest_score

            lowest_score = []
            lowest_score.append(student)
            continue

        if score == lowest_score[0][1]:
            lowest_score.append(student)
            continue

        if score > lowest_score[0][1] and second_lowest == []:
            second_lowest.append(student)
            continue

        if score > lowest_score[0][1] and score < second_lowest[0][1]:
            second_lowest = []
            second_lowest.append(student)
            continue

        if score > lowest_score[0][1] and score == second_lowest[0][1]:
            second_lowest.append(student)

    second_lowest = sorted(second_lowest, key=lambda x: x[0])

    for x in second_lowest:
        print(x[0])


main()
