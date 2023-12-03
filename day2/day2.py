
def main():
    with open("./input.txt") as f:
        games = f.readlines()
        sum_of_powers = 0

        for game in games:
            parsed = game.split(":")

            game_num = parsed[0]
            game_num = int(game_num.split(" ")[1])

            rolls = parsed[1].strip()
            rolls = rolls.replace(";", ",")
            rolls = rolls.split(",")

            reds = []
            greens = []
            blues = []
            for roll in rolls:
                roll = roll.strip()
                amount = int(roll.split(" ")[0])

                if "red" in roll:
                    reds.append(amount)
                elif "green" in roll:
                    greens.append(amount)
                elif "blue" in roll:
                    blues.append(amount)

            min_red = max(reds)
            min_green = max(greens)
            min_blue = max(blues)

            sum_of_powers += min_red * min_green * min_blue
            
        print(sum_of_powers)

        f.close()

if __name__ == "__main__":
    main()