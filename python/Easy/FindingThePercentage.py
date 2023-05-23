if __name__ == "__main__":
    n = int(input())
    students = {}

    for i in range(n):
        line = input().split()

        name = line[0]
        line.pop(0)

        marks = []
        for x in line:
            value = float(x)
            marks.append(value)

        students[name] = marks

    student = input()
    student_average = 0

    for x in students[student]:
        student_average += x

    student_average = student_average / 3
    print(format(student_average, ".2f"))
