def get_winner(player_1, player_2):
    if player_1.choice == "Rock" and player_2.choice == "Scissors":
        return player_1

    if player_1.choice == "Scissors" and player_2.choice == "Paper":
        return player_1

    if player_1.choice == "Paper" and player_2.choice == "Rock":
        return player_1

    return player_2
