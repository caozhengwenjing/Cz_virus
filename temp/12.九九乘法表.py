i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%dx%d=%d' % (j, i, j * i), end=" ")
        j += 1
    i += 1
    print()