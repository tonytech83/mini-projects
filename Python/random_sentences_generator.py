import random


def get_random(lst: list[str]):
    return random.choice(lst)


lst: list[list[str]] = [
    ["Anton", "Petar", "Dian", "Teodor", "Junian", "Kiril"],
    ["Sofia", "Stara Zagora", "Plovdiv", "Galabovo", "Varna"],
    ["coding on", "eats", "holds", "plays with", "brings"],
    ["laptop", "stones", "bikes", "cake"],
    ["slowly", "sadly", "rapidly", "warmly"],
    ["near the sea", "at home", "at work", "in the park"],
]

input("Hello! This will be your first random sentence.")

usr_input: str = ""
while usr_input != "q":
    result = [get_random(x) for x in lst]

    print(
        f"{result[0]} from {result[1]} {result[2]} {result[3]} {result[4]} {result[5]}",
    )
    usr_input = input("Hit [Enter] to generate a new one or [q] to quit!")
