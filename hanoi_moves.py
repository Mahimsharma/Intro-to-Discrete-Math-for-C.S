def moves(discs):
    if discs == 1:
        return 1

    return (1 + 2*moves(discs - 1))

print(moves(6))
