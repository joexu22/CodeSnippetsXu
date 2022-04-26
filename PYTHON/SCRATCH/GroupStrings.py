## The following code groups a list of strings into disjoint based on unique characters in each string.

## The following is the list of strings to be grouped.
strings = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
unique_characters = ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]

## The following code creates a list of unique characters in each string.
## The unique characters are sorted alphabetically.
def getUniqueCharacters(strings):
    unique_characters = []
    for string in strings:
        for char in string:
            if char not in unique_characters:
                unique_characters.append(char)
    unique_characters.sort()
    return unique_characters

print(getUniqueCharacters(strings))
