str = input("Enter a string: ")

sum = 0 

for char in str:
    if '0' <= char <= '9':
        sum += int(char)
print("The sum of the digits from the inputted string is: ", sum)
