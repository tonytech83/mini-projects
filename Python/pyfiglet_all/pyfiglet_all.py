import pyfiglet
from collections import deque

with open("fonts.txt", "r") as file:
    fonts = deque(file.read().splitlines())

while fonts:
    font = fonts.popleft()
    print("Testing font " + font)
    f = pyfiglet.Figlet(font=font, width=80)
    print(f.renderText('Tic-Tac-Toe'))
