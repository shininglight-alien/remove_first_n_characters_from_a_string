# Remove first n characters from a string

def get_input():
    string = input("String Entry: ")
    n = int(input("Enter a Number: "))
    return string, n

def remove_chars(string, n):
    if n < len(string):
        return string[n:]
    else:
        return "Error: Entered number is greater than the length of the string entered."
    
string, n = get_input()
print(remove_chars(string, n))