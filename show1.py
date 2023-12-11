import random

with open("./hyakuninisshu.txt", encoding="utf-8") as f:
    wakas = [s.strip() for s in f.readlines()]

print(wakas[random.randrange(len(wakas))])