from logic_game import *
from storge import *



def main():
    escape = False
    try:
        while not escape:
            print("""
            ================================
                        ROLL DICE
            ================================

            1. Start New Game
            2. View Game History
            3. View Statistics
            4. Exit

            Choose an option:

            """
            )

            choose = input("Enter your choice: ")
            if choose == "4":
                escape = True
            elif choose == "1":
                game = start_game()
            elif choose == "2":
                history = load_game_history()
                display_game_history(history)
            elif choose == "3":
                history = load_game_history()
                display_statistics(history)
                

    except ValueError as e:
        print(e)




main()