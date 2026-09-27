s="hello"
t= "olleh"

def validanagram(s, t):

    if len(s) != len(t):
        return False

    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    for char in t:
        if char not in freq:
            return False
        else:
            freq[char] -= 1


        if freq[char] < 0:
            return False

    return True

print(validanagram(s, t))

