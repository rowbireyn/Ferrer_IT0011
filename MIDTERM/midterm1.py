with open("C:/Users/xiaolongbao/Documents/GitHub/Ferrer_IT0011/numbers.txt") as f:
    for i, line in enumerate(f, 1):
        total = sum(map(int, line.strip().split(",")))
        result = "Palindrome" if str(total) == str(total)[::-1] else "Not a palindrome"
        print(f"Line {i}: {line.strip()} (sum {total}) - {result}")
f.close()