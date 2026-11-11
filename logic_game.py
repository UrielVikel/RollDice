import random
from storge import *


def get_name():
    escape_name_found = False
    while not escape_name_found:
        name = input("Enter name: ").strip()
        if name != "":
            return name


def get_rounds():
    escape_round_found = False
    while not escape_round_found:
        try:
            rounds = int(input("How many rounds?: "))
            if rounds > 0 and rounds <= 10:
                return rounds
            else:
                print("only number between 1 - 9")
        except ValueError:
            print("only valid")


def roll_dice():
    return random.randint(1,6)


def play_round():
    player_dice = roll_dice()
    computer_dice = roll_dice()
    winner = calculate_winner(player_dice, computer_dice)
    round_game = {
        "round":0,
        "player_dice": player_dice,
        "computer_dice": computer_dice,
        "winner": winner,
    }
    return round_game



def start_game():
    name = get_name()
    get_round = get_rounds()
    player_score = 0 
    computer_score = 0
    result_dict = []
    for i in range(get_round):
        round_play = play_round()
        round_play["round"] = i+1
        if round_play["winner"] == "player":
            player_score += 1
            round_play["winner"] = name
        elif round_play["winner"] == "computer":
            computer_score += 1
            round_play["winner"] = "computer"
        else:
            round_play["winner"] = "draw"
        result_dict.append(round_play)
    

    winner = calculate_winner(player_score, computer_score)
    if winner == "player":
        game["winner"] = name
    else:
        game["winner"] = winner


    game["player_name"] = name
    game["rounds"] = get_round
    game["player_score"] = player_score
    game["computer_score"] = computer_score
    game["results"] = result_dict

    display_game_results(game)
    save_game(game)
    return game



    



def calculate_winner(player_score, computer_score):
    if player_score > computer_score:
        return "player"
    elif player_score < computer_score:
        return "computer"
    else:
        return "draw"






def display_game_results(game):
    print(f"""
        ================================
                    NEW GAME
        ================================

        Player name: {game["player_name"]}
        Number of rounds: {game["rounds"]}
        """)

    for result in game["results"]:
        print(f"""

            ---------- ROUND {result["round"]} ----------

            {game["player_name"]}: 🎲 {result["player_dice"]}
            Computer: 🎲 {result["computer_dice"]}


            {result["winner"]} wins this round!

            """)




    print(f"""
        ================================
                GAME OVER
        ================================

        {game["player_name"]}: {game["player_score"]} points
        Computer: {game["computer_score"]} points

        WINNER: {game["winner"]}!

        """
        )







def display_game_history(history):
    for i in history:
        print(f"""
        ================================
                    GAME
        ================================

        Result!
        Player name:{i["player_name"]}
        Number of rounds: {i["rounds"]}
        Player score: {i["player_score"]}
        Computer: {i["computer_score"]}
        Winner: {i["winner"]}
        """
        )








def display_statistics(history):
    counter_history = 0
    counter_player_wins = 0
    counter_computer_wins = 0
    counter_draw = 0
    for i in history:
        counter_history += 1
        if i["winner"] == "computer":
            counter_computer_wins += 1
        elif i["winner"] == "draw":
            counter_draw += 1
        else:
            counter_player_wins += 1
    
    counter_win_percentage = (counter_player_wins / counter_history) * 100

    print(f"""
        ================================
                  STATISTICS
        ================================
        Rounds: {counter_history}
        Player wins: {counter_player_wins}
        Computer wins: {counter_computer_wins}
        Draw: {counter_draw}
        Win Percentage: {counter_win_percentage}
    """
    )
    
    return counter_history
