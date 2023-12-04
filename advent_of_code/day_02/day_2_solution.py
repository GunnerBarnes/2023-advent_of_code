# 12 red, 13 green, 14 blue

# input_file = './sample.txt'
input_file = './input.txt'


def part_one():
    with open(input_file) as f:
        lines = f.readlines()
        sum = 0
        for idx, line in enumerate(lines):
            line = line.split(':')[1].split(';')
            possible = True
            for games in line:
                games = games.strip().split(',')

                for game in games:
                    game = game.strip().split(' ')
                    if ((game[1] == 'red' and int(game[0]) > 12) or
                       (game[1] == 'green' and int(game[0]) > 13) or
                       (game[1] == 'blue' and int(game[0]) > 14)):
                        possible = False

            if possible:
                sum += (idx + 1)

        print("result_sum: ", sum)


def part_two():
    with open(input_file) as f:
        lines = f.readlines()
        sum = 0
        for line in lines:
            line = line.split(':')[1].split(';')
            red_max, green_max, blue_max = 0, 0, 0

            for games in line:
                games = games.strip().split(',')

                for game in games:
                    game = game.strip().split(' ')
                    if (game[1] == 'red' and int(game[0]) > red_max):
                        red_max = int(game[0])
                    elif (game[1] == 'green' and int(game[0]) > green_max):
                        green_max = int(game[0])
                    elif (game[1] == 'blue' and int(game[0]) > blue_max):
                        blue_max = int(game[0])

            sum += (red_max * green_max * blue_max)

        print("sum: ", sum)


part_two()
