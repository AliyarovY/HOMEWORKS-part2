def calc_salt(mass):
    try:
        return int(mass) / 100
    except ValueError as gk:
        print(gk)
        return 0.0


