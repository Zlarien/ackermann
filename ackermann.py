"""Fonction d'Ackermann, version itérative avec limite d'étapes."""


def ackermann(m, n, limite=None, montrer=()):
    pile, etapes = [m], 0
    while pile:
        etapes += 1
        if etapes in montrer:
            print(f"étape {etapes:>10} | n = {n:<5} | pile = {pile[-5:]} (taille {len(pile)})")
        if limite and etapes > limite:
            return None, etapes  # trop long : on abandonne
        m = pile.pop()
        if m == 0:
            n += 1
        else:
            pile.append(m - 1)
            if n == 0:
                n = 1
            else:
                pile.append(m)
                n -= 1
    return n, etapes


if __name__ == "__main__":
    for m, n in [(1, 3), (2, 3), (3, 2), (4, 0)]:
        print(f"A({m},{n}) = {ackermann(m, n)[0]}")

    r, etapes = ackermann(4, 4, limite=50_000_000, montrer={1, 5, 10, 1_000, 1_000_000, 50_000_000})
    print("A(4,4) =", r if r is not None else f"abandonné après {etapes:,} étapes (trop long)")
