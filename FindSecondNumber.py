n = [12, 35, 1, 10, 34]

smallest_n = n[0]
largest_n = n[0]
second_largest_n = n[0]

for i in n:
    if i > largest_n:
        largest_n = i

for i in n:
    if i < smallest_n:
        smallest_n = i
for i in n:
    if i > second_largest_n and i < largest_n:
        second_largest_n = i

print(smallest_n)
print(largest_n)



