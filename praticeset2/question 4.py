numbers = [2, 5, 2, 8, 5, 2, 9, 8]
freq = {}
for i in numbers:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)