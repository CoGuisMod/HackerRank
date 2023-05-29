def main(array):
    new_array = ""

    for i in range(len(array)):
        value = array[i]

        if value.isupper():
            value = value.lower()
            new_array += value
            continue

        else:
            value = value.upper()
            new_array += value
            continue

    print(new_array)


array = "lKJHjkudfhkjsadSKJX"
main(array)
