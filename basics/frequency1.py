numbers = [1, 2, 1, 3, 2, 1, 4, 3]

freq = {}

for num in numbers:
    if num in freq:
        freq[num] = freq[num] + 1
    else:
        freq[num] = 1

print(freq)