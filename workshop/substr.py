#  Create a function that takes two strings as a parameter
#  Returns the starting index where the second one is starting in the first one
#  Returns `-1` if the second string is not in the first one
def find_substring(string, substring):
    if substring in string:
        return string.index(substring)
    else:
        return -1
print(find_substring("this is what I'm searching in", "not"))
