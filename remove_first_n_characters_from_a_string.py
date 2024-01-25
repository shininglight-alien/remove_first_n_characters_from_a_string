# Remove first n characters from a string

def remove_chars():
    string = input("String Entry: ")
    n = int(input("Enter a Number: "))
    if n < len(string):
        return string[n:]
    else:
        return "Error: n is greater than the length of the string"

print(remove_chars())  # User inputs the string and n