import time
import random

# player states
player = {
    "name": "",
    "health": 100,
    "gold": 50,
    "items": []
}

# Game location
locations = {
    "town": {
        "description": "A bustling town with shops and friendly people.",
        "options": ["shop", "fores", "rest"]
    },
    "forest": {
        "description": "A dark forest with strang sounds and hidden treasures.",
        "options": ["explore", "return to town", "camp"]
    },
    "shop": {
        "description": "A small shop with various items for sale.",
        "options": ["buy health potion (20 gold)", "buy sward (50)", "return to town"]
    },

},


# Items with effects
items = {
    "health potion": {"health": 30, "price": 20},
    "sword": {"damage": 10, "price": 50}
}

# Enemies that can be encountered
enemies = [
    {"name": "Goblin", "health": 30, "damage": 5, "gold": 15},
    {"name": "Wolf", "health": 20, "damage": 7, "gold": 10},
    {"name": "Bandit", "health": 40, "damage": 8, "gold": 25},
]


def slow_print(text):
    pass


def display_stats():
    pass


def town():
    pass


def shop():
    pass


def buy_item():
    pass


def forest():
    pass


def explore():
    pass


def enemy_encounter():
    pass


def treasure_encounter():
    pass


def rest():
    pass


def game_over():
    pass


def start_game():
    player["health"] = 100
    player["gold"] = 50
    player["items"] = []

    slow_print("\n" + "=" * 60)
    slow_print("FOREST ADVENTURE")
    slow_print("="*60)
    slow_print("Welcome to simple text adventure game!")

    player["name"] = input("\What is your name, adventure?")
    slow_print(
        f"\nWelcome, {player['name']}! Your adventure begins in a small town.")


start_game()
