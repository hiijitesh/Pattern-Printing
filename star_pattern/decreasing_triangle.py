from sre_constants import RANGE


n = 7

for row in range(n):
    for col in range(row, n):
        print("* ", end="")
    print()
