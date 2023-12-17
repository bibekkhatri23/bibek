# for i in range(1, 4):
#     for j in range(1, i + 1):
#         print(j, end='')
#     print()

i = 1
while i <= 3:
    j = 1
    while j <= i:
        print(j, end='')
        j += 1
    print()
    i += 1
