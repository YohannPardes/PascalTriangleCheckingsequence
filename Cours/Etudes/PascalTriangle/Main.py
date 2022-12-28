def PT(wanted_numbers, depth=1000):
    previous_row = [1]
    current_depth = 2
    while current_depth < depth:
        row = []
        for i in range(current_depth):
            res = 0

            if (0 > i - 1):
                res += 0

            else:
                res += previous_row[i - 1]

            if (i + 1 > len(previous_row)):
                res += 0
            else:
                res += previous_row[i]

            row.append(res)

        if check_end(row, wanted_numbers, current_depth):
            return

        current_depth += 1
        previous_row = row[:]

    print(f"No matching have been found at {depth} depth.")


def check_end(row, wanted_nb, depth):
    """
    The function check have the following sequence nb1X, nb2X... for each wanted numbers
    """
    for i in range(len(row) - 3):
        check_potential = [row[i + j] % wanted_nb[j] == 0 for j in range(len(wanted_nb))]
        if check_potential.count(1) == len(check_potential):
            division_res = [row[i + l] // nb for l, nb in enumerate(wanted_nb)]
            if division_res.count(division_res[0]) == len(division_res):
                print_info(depth, i, row, wanted_nb)
                return True

    return False


def print_info(depth, i, row, wanted_nb):
    print("ending depth -", depth - 1, "(when counting the rows from 0)")
    print(f"At the indexes {i}, {i + 1}, {i + 2}")
    print(f"Appearing the following numbers {row[i]}, {row[i + 1]}, {row[i + 2]}")
    print(f"The row is :")
    print(*[[f"{nb}*{row[i + l] / nb}"] for l, nb in enumerate(wanted_nb)], sep="")
    print(f"The wanted x is :{row[i] / wanted_nb[0]}")


if __name__ == "__main__":
    wanted_folowing_divisors = [3, 4, 5]
    depth_search = 2000
    PT(wanted_folowing_divisors, depth_search)
