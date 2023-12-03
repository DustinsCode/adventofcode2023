
def main():

    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    with open("./input.txt") as f:
        games = f.readlines()
        possible_games = 0

        for game in games:
            parsed = game.split(":")

            game_num = parsed[0]
            game_num = int(game_num.split(" ")[1])

            rounds = parsed[1].strip()
            rounds = rounds.split(";")
            is_good_game = True
            for round in rounds:
                rolls = round.split(", ")
                for roll in rolls:
                    roll = roll.strip()
                    amount = int(roll.split(" ")[0])

                    if "red" in roll:
                        if amount > MAX_RED:
                            is_good_game = False
                    elif "green" in roll:
                        if amount > MAX_GREEN:
                            is_good_game = False
                    elif "blue" in roll:
                        if amount > MAX_BLUE:
                            is_good_game = False

            if is_good_game:
                possible_games += game_num

        print(possible_games)
        f.close()

if __name__ == "__main__":
    main()