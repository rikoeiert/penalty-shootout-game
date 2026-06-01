import random

stats = {
    "games_played": 0,
    "player_wins": 0,
    "computer_wins": 0
}

directions = ["left", "center", "right"]

is_goal = lambda shot, guess: shot != guess # lambda näitab, et kui shot ja guess on erinevad, siis on see värav, kui samad, siis on see tõrje.


def greet():
    print("Welcome to the Soccer Penalty Shootout!")


def get_direction(prompt):
    while True:
        choice = input(prompt).lower().strip()

        if choice in directions:
            return choice

        print("Please type left, center or right.")


def choose_level():
    print("\n--- CHOOSE LEVEL ---")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        level = input("Choose level 1, 2 or 3: ").strip()

        if level in ["1", "2", "3"]:
            return int(level)

        print("Invalid level, try again.")


def computer_goalkeeper(level, player_shot):
    chance = random.randint(1, 100)

    if level == 1:
        return random.choice(directions)

    if level == 2:
        if chance <= 40:
            return player_shot
        return random.choice(directions)

    if level == 3:
        if chance <= 65:
            return player_shot
        return random.choice(directions)


def computer_attack(level, player_guess):
    chance = random.randint(1, 100)

    if level == 1:
        return random.choice(directions)

    if level == 2:
        if chance <= 40:
            possible_shots = directions.copy() # copy() meetodiga luuakse uus nimekiri, mis on sama kui directions, et saaks seda muuta ilma algset nimekirja mõjutamata.
            possible_shots.remove(player_guess) 
            return random.choice(possible_shots) # remove() meetodiga eemaldatakse player_guess nimekirjast possible_shots, et arvuti ei valiks sama suunda, mida mängija arvas.
        return random.choice(directions) # kui chance on suurem kui 40, siis arvuti valib suvalise suuna, mis võib olla sama, mida mängija arvas, või erinev.

    if level == 3:
        if chance <= 65:
            possible_shots = directions.copy()
            possible_shots.remove(player_guess)
            return random.choice(possible_shots)
        return random.choice(directions)


def show_stats():
    print("\n--- STATISTICS ---")
    print("Games played:", stats["games_played"])
    print("Player wins:", stats["player_wins"])
    print("Computer wins:", stats["computer_wins"])


def take_penalties(player_score, computer_score, round_name, level):
    print("\n" + round_name + ":")

    player_scored = False
    computer_scored = False

    player_shot = get_direction("Choose your shot direction (left, center, right): ")
    computer_guess = computer_goalkeeper(level, player_shot)

    if is_goal(player_shot, computer_guess):
        print("Goalkeeper guessed " + computer_guess + ". Goal!")
        player_score += 1
        player_scored = True
    else:
        print("Goalkeeper guessed " + computer_guess + "! Shot saved!")

    player_guess = get_direction("Guess the computer's shot direction (left, center, right): ")
    computer_shot = computer_attack(level, player_guess)

    if is_goal(computer_shot, player_guess):
        print("Computer shot " + computer_shot + ". Goal for computer!")
        computer_score += 1
        computer_scored = True
    else:
        print("You guessed " + player_guess + "! You saved it!")

    print("Score: You " + str(player_score) + " - " + str(computer_score) + " Computer")

    return player_score, computer_score, player_scored, computer_scored


def penalty_shootout():
    player_score = 0
    computer_score = 0
    rounds = 5

    level = choose_level()

    for i in range(rounds):
        player_score, computer_score, player_scored, computer_scored = take_penalties(
            player_score,
            computer_score,
            "Round " + str(i + 1),
            level
        )

    extra_round = 1

    while player_score == computer_score:
        player_score, computer_score, player_scored, computer_scored = take_penalties(
            player_score,
            computer_score,
            "Sudden Death Round " + str(extra_round),
            level
        )

        if player_scored != computer_scored:
            break

        extra_round += 1

    print("\nFinal Score:")
    print("You " + str(player_score) + " - " + str(computer_score) + " Computer")

    stats["games_played"] += 1

    if player_score > computer_score:
        print("You win!")
        stats["player_wins"] += 1
    else:
        print("Computer wins!")
        stats["computer_wins"] += 1


def menu():
    greet()

    while True:
        print("\n--- MENU ---")
        print("1. Play game")
        print("2. Show stats")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            penalty_shootout()
        elif choice == "2":
            show_stats()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


menu()