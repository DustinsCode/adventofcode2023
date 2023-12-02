import re


total = 0

with open("./input.txt") as f:
    lines = f.readlines()

    for line in lines:
        numbers = re.sub("[a-z]+", "", line.strip())

        if(len(numbers) == 1):
            numbers = f"{numbers}{numbers}"
        else:
            numbers = f"{numbers[0]}{numbers[len(numbers) - 1]}"

        total += int(numbers)
    
    print(total)

f.close()