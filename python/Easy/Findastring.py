def main(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if i + len(sub_string) > len(string):
                break
            if string[i : i + len(sub_string)] == sub_string:
                count += 1
    return count


string = "ABCDCDC"
sub_string = "CDC"
main(string, sub_string)
