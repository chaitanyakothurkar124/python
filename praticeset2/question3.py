numbers = [3, 7, 2, 9, 7, 4]
seen = set()
for i in numbers:
    if i in seen:
        print("Duplicate")
        break
    seen.add(i)