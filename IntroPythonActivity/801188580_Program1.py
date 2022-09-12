def string_ends(str):
    if len(str) < 2:
        return ''
    return str[0:2] + str[-2:]
string = input("Enter string with length ateast 2")
stringToReturn = string_ends(string)
print(stringToReturn)
