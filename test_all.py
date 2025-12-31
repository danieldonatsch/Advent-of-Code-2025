import time

from run import get_advent_of_code_solution


# Solution for samples.
# Dict key is the day, first solution for star 1, second for star 2
sample_solutions = {
    1: (3, 6),
    2: (1227775554, 4174379265),
    3: (357, 3121910778619),
    4: (13, 43),
    5: (3, 14),
    6: (4277556, 3263823),
    7: (21, 40),
    8: (40, 25272),
    9: (50, ),
    10: (7, ),
    11: (5, 2)
}

# Solution for samples.
# Dict key is the day, first solution for star 1, second for star 2
puzzle_solutions = {
    1: (1089, 6530),
    2: (64215794229, 85513235135),
    3: (17278, 171528556468625),
    4: (1409, 8366),
    5: (640, 365804144481581),
    6: (5977759036837, 9630000828442),
    7: (1543, 3223365367809),
    8: (123930, 27338688),
    9: (4771532800, 1544362560),
    10: (447, ),
    11: (590, 319473830844560),
}


def run_all_tests(example=True) -> None:
    target_values = sample_solutions if example else puzzle_solutions

    if example:
        print("Results with small examples")
    else:
        print("Real Input Results:")
    print("Day Stars")
    for day, values in sorted(target_values.items()):
        solution = get_advent_of_code_solution(day=day, is_example=example)
        val = values[0]
        out = ''
        if val == solution._star_1():
            out += '*'
        else:
            out += 'x'
        if len(values) == 1:
            out += '-'
        else:
            val = values[1]
            if val == solution._star_2():
                out += '*'
            else:
                out += 'x'
        print(f"{day: 3d}", out)


if __name__ == '__main__':
    t0 = time.time()
    run_all_tests(example=False)

    print("\nRunning all Advent of Code 2025 puzzles took", round(time.time() - t0, 4), "seconds")