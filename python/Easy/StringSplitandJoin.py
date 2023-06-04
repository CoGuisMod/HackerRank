def main(string):
    # return string.replace(" ", "-")
    return "-".join(string.split(" "))


string = "this is a string"
main(string)
