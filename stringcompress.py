def compress(str1):
    s = ""
    i = 0

    # We traverse the string and run a while loop every time the character of string is same as previous.
    while (i <= len(str1)-1):
        count = 1
        ch = str1[i]
        j = i

        # While loop if character is same as next character.
        while (j < len(str1)-1):
            if (str1[j] == str1[j+1]):
                count = count+1
                j = j+1
            else:
                # Incase the character is not as same as previous break from this loop.
                break

        s = s + ch + str(count)
        i = j+1
# This section makes sure that same string is returned if length is not compressed
    if len(s) >= len(str1):
        return str1
    else:
        return s


if __name__ == "__main__":
    print(compress("AAAAABBBBBBBCCCCCDE"))
    print(compress("ABCDEF"))
