import re


number_dict = {
    "one":   "1",
    "two":   "2",
    "three": "3",
    "four":  "4",
    "five":  "5",
    "six":   "6",
    "seven": "7",
    "eight": "8",
    "nine":  "9",
}

def get_number_from_substring(s: str):
    for key in number_dict.keys():
            if key in s:
                return number_dict[key]
    return None

def find_first_digit(line: str):
    start_str = ""
    for char in line:
        if(char.isdigit()):
            return char
        
        start_str += char
        result = get_number_from_substring(start_str)
        if result != None:
            return result
 
def find_last_digit(line: str):
    end_str = ""
    line_reversed = line[::-1]
    for char in line_reversed:
        if(char.isdigit()):
            return char
        
        end_str = char + end_str
        result = get_number_from_substring(end_str)
        if result != None:
            return result

def main():
    total = 0

    with open("./input.txt") as f:
        lines = f.readlines()

        for line in lines:
            
            first_digit = 0
            last_digit = 0
            
            first_digit = find_first_digit(line.strip())
            last_digit = find_last_digit(line)
           
            total += int(first_digit + last_digit)
        
        print(total)

    f.close()


if __name__ == '__main__':
    main()