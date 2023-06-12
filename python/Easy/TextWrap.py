def wrap(string, max_width):
    result = ""
    counter = 0

    for i in range(len(string)):
        if counter == max_width:
            result += "\n" + string[i]
            counter = 1
        else:
            result += string[i]
            counter += 1

    return result


string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4
print(wrap(string, max_width))
