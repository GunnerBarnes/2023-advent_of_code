# read input file and create list of input lines
# file = open("./sample.txt", "r")
# input = file.read()
# input_list = input.split('\n')
input_file = './input.txt'


def part_one():
    with open(input_file) as f:
        lines = f.readlines()
        sum = 0
        for line in lines:
            nums = []
            for letter in line:
                if ord(letter) <= 57 and ord(letter) != 10:
                    nums.append(letter)
            sum += int(nums[0] + nums[-1])
    print(sum)


def part_two():
    with open(input_file) as f:
        lines = f.readlines()
        sum = 0
        integer_names = [
                'zero',
                'one',
                'two',
                'three',
                'four',
                'five',
                'six',
                'seven',
                'eight',
                'nine'
                ]
        for line in lines:
            nums = []
            for i, letter in enumerate(line):
                for val, name in enumerate(integer_names):
                    if name in line[i:i+len(name)]:
                        nums.append(str(val))
                    if ord(letter) <= 57 and ord(letter) != 10:
                        nums.append(letter)

            sum += int(nums[0] + nums[-1])
    print(sum)


part_two()
