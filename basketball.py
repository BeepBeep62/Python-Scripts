listy = [
    "flappy bird",
    "tetris",
    "snake",
    "pong",
    "DOOM",
    "furit ningja",
    "ok"
]
count = 1
for l in listy:
    print(count, l)
    count = count+1
obj = enumerate(listy)
print(list(obj))