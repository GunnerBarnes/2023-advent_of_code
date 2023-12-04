# for each line in input file,
# find first digit in string, find last digit in string
# add resulting two-digit number to running total

input_file = './input.txt'
# expected result for sample file is 33


def main():
    with open(input_file) as f:
        running_total: int = 0
        lines = f.readlines()

        for line in lines:
            # find first and last digit
            first_digit = getIndexOfDigit(line)
            last_digit = getIndexOfDigit(line[::-1])
            running_total += combineDigits(first_digit, last_digit)

    print("Running total: ", running_total)
    # return running_total


def getIndexOfDigit(line: str) -> str:
    for char in line:
        if char.isnumeric():
            return str(char)

    return ""


def combineDigits(first_digit: str, last_digit: str) -> int:
    result: str = first_digit + last_digit
    return int(result)


main()
