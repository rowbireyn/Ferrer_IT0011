i = 1
while i <= 5:
    if i <= 3:
        num = 2 * i - 1
    else:
        num = i + 2
    
    j = 1
    while j <= num:
        print(num, end="")
        j += 1
    print()
    
    i += 1