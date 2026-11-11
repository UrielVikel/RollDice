import json 
from pathlib import Path



path = Path(__file__).parent / "historygame.json"



game = {
    "player_name": "",
    "rounds": 0,
    "player_score": 0,
    "computer_score": 0,
    "winner": "",
    "results": []
}



# def read_file(path):
#     try:
#         with open (path, "r") as f:
#             read_file = f.read()
#             return json.load(f)
#     except NotImplementedError:
#         return []


# def write_file(path):
#     try:
#         with open(path, "w") as f:
#             return json.dump(f)
#     except Exception as e:
#         print(e)


# def load_game_history():
#     with open(path, "r", encoding="utf-8") as f:
#         games = json.load(f)
#     return games

# def save_game(game):
#     games = load_game_history()
#     games.append(game)
#     with open(path, "w", encoding="utf-8") as f:
#         json.dump(games, path, indent=2, ensure_ascii=False)
#     print("Game saved successfully!")




def load_game_history():
    with open(path, "r", encoding="utf-8") as file:
        games = json.load(file)                    
    return games




def save_game(game):
    games = load_game_history()
    games.append(game)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(games, file, indent=2, ensure_ascii=False)
    print("Game saved successfully!")