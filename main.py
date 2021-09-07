from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Games:
    title: str
    progress: str
    genre: str


def create() -> Games:
    title = input("Game title: ")
    progress = input(
        "Have you [beaten] the game, is it [backlogged], or are you currently [playing]? ")
    genre = input("What genre is the game? ")
    with open("games.txt", "a") as file:
            file.write(f"{title} - {progress} - {genre}\n")                                       
    return Games(title, progress, genre)

def load_games():
    game_info = []
    try:
        with open("games.txt", "r") as file:
                for game in file:
                    return game_info
    except FileNotFoundError:
        with open("games.txt", "w") as file:
            return game_info

def view_all(games: List):
    with open("games.txt", "r") as file:
        for game in file:
            print(game)


def view_progress(games: List):
    file = open("games.txt", "r")
    lines = file.readlines()
    file.close()
    print("Do you want to view by [backlogged], [beaten], or [playing]?")
    action = input("> ")
    if action == "backlogged":
        for line in lines:
            if "backlogged" in line:
                print(line)
    elif action == "beaten":
        for line in lines:
            if "beaten" in line:
                print(line)
    elif action == "playing":
        for line in lines:
            if "playing" in line:
                print(line)
    else:
        print("Action not available")


def detect_game(game_name: str) -> Optional[bool]:
    try:
         with open("games.txt", "r") as file:
             for line in file:
                 if game_name in line:
                     return True
             return False
    except FileNotFoundError:
        print("\nYou have no games in collection!")
    return None

def update(games: List[Games], game_name: str) -> None:
    file = open("games.txt", "r")
    lines = file.readlines()
    file.close()
    if detect_game(game_name) == True:
        progress = input(
                    "Have you [beaten] the game, is it [backlogged], or are you currently [playing]? "
                )
        genre = input("What genre is the game?  ")
        with open("games.txt", "w") as file:
            for line in lines:
                if not game_name in line.strip("\n"):
                            file.write(line)
            file.write(game_name + " - " + progress + " - " + genre + "\n")
    else:
        print("\nThat game is not in your collection!")


def find_name(games: List[Games], game_name: str) -> None:
    file = open("games.txt", "r")
    lines = file.readlines()
    file.close()
    if detect_game(game_name) == True:
        for line in lines:
            if game_name in line:
                print(line)
    else:
        print("\nThat game is not in your collection!")


def delete(games: List[Games], game_name: str) -> None:
    file = open("games.txt", "r")
    lines = file.readlines()
    file.close()
    if detect_game(game_name) == True:
        with open("games.txt", "w") as file:
            for line in lines:
                if not game_name in line.strip("\n"):
                    file.write(line)
    else:
        print("\nThat game is not in your collection!")


def main():
    games = load_games()
    print(
            "Welcome to Game Information! We can store the game you have entered and your information for it!"
        )
    while True:
        print(
            "Would you like to [create], view [all], view by [name], view by [progress], [update], [delete], or [quit]?"
        )
        action = input("> ")
        if action == "create":
            create()
        elif action == "name":
            find_name(games, input("Game Title: "))
        elif action == "all":
            view_all(games)
        elif action == "progress":
            view_progress(games)
        elif action == "update":
            update(games, input("Game Title: "))
        elif action == "delete":
            delete(games, input("Game Title: "))
        elif action == "quit":
                break

if __name__ == "__main__":
    main()
