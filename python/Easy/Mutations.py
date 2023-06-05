def mutate_string(string, position, character):
    new_string = ""
    position = position

    for i in range(len(string)):
        if i != position:
            new_string += string[i]
        else:
            new_string += character

    return new_string


string = "abracadabra"
position = 5
character = "k"
mutate_string(string, position, character)
