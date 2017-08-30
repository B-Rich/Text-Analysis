# TASK: Find if a string has all unique characters.
# Returns: Boolean
def isUniqueChars(inString):
    # Immediately return if the string length
    # exceeds the number of unique chars.
    if (len(inString) > 128):
        return False

    char_set = [False for i in range(128)]
    for i in range(len(inString)):
        val = ord(inString[i])
        if (char_set[val]):
            return False
        char_set[val] = True
    return True