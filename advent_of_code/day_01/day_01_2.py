# for each line in input file,
# find first digit in string, find last digit in string
# add resulting two-digit number to running total

#input_file = './sample3.txt'
input_file = './input_final.txt'
# with sample2.txt, output should be 71 + 21 = 92

spelled_out_numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def main():
    with open(input_file) as f:
        running_total: int = 0
        lines = f.readlines()

        dev_count = 0
        for line in lines:
            # find first and last digit
            first_digit = get_digit(line)
            first_digit_word = get_word_number(
                    line[:line.find(first_digit)],
                    line.find(first_digit),  True
            )
            if (
                first_digit_word != ''
                and line.find(first_digit_word) < line.find(first_digit)
            ):
                first_digit = str(spelled_out_numbers[first_digit_word])
            last_digit = get_digit(line[::-1])
            last_digit_word = get_word_number(
                    line[line.rfind(last_digit):],
                    0, False
            )
            if (
                    last_digit_word != ''
                    and line.find(last_digit_word) > line.find(last_digit)
            ):
                last_digit = str(spelled_out_numbers[last_digit_word])
            running_total += combineDigits(first_digit, last_digit)
            dev_count += 1
            print("line_count: ", dev_count)
            # print("Running total: ", running_total)
    # return running_total

# should only need to change this function:
# find the first numeric character, make note of the index
# then we can check if any spelled out number exists before that index


def get_digit(line: str) -> str:
    first_char_digit: str = ''
    for idx, char in enumerate(line):
        if char.isnumeric():
            first_char_digit = char
            break

    return first_char_digit


def combineDigits(first_digit: str, last_digit: str) -> int:
    result: str = first_digit + last_digit
    print("Combined digits: ", result)
    return int(result)


def get_word_number(sub_line: str, numeric_digit: int, is_first: bool) -> str:
    # if any (x in sub_line for x in spelled_out_numbers)
    # get word with lowest start index
    # then return the value for that key in our dictionary

    target_word = ''
    target_word_index = numeric_digit
    for word in spelled_out_numbers:
        word_index = sub_line.find(word)
        if is_first:
            if word_index >= 0 and word_index < target_word_index:
                target_word_index = word_index
                target_word = word
        else:
            if word_index >= 0 and word_index > target_word_index:
                target_word_index = word_index
                target_word = word

    return target_word


main()
