# 12 red, 13 green, 14 blue

# input_file = './sample.txt'
input_file = './input.txt'

rule_colors = {'red': 12, 'green': 13, 'blue': 14}


def part_one():
    with open(input_file) as f:
        lines = f.readlines()
        result_sum = 0
        for idx, line in enumerate(lines):
            game_id = idx + 1
            colors = line[line.find(':') + 2:].split(',')
            is_valid = True

            for color in colors:
                values = color.split()
                if values[1] in rule_colors:
                    if int(values[0]) > rule_colors[values[1]]:
                        is_valid = False
                        break

            if is_valid:
                print("valid game: ", game_id)
                result_sum += game_id

        print("result_sum: ", result_sum)


part_one()
