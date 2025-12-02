from . import base_solution as bs


class SolutionDay02(bs.BaseSolution):
    def __init__(self, day_num: int, example=False, verbose=False):
        super().__init__(day_num, example, verbose=verbose)

    def _star_1(self) -> int:
        """Solve puzzle 1

        :return:
        """
        input_file_path = self.get_input_file_path()

        with open(input_file_path, 'r') as of:
            line = of.readline()
            ranges = line.strip().split(',')
        if not ranges:
            print("Failed to read input")
            return -1

        inv_ids_sum = 0
        for rng in ranges:
            range_first, range_last = rng.split('-')
            l = len(range_first)
            half_digits = range_first[:int(l/2)]
            if l % 2 == 1:
                if l == len(range_last):
                    # Odd num of digits: Impossible to find something like xyzxyz
                    continue
                else:
                    half_digits = ''.join(['1'] + ['0']*len(half_digits))

            range_first = int(range_first)
            range_last = int(range_last)
            full_digits = int(half_digits + half_digits)
            while full_digits <= range_last:
                if full_digits >= range_first:
                    inv_ids_sum += full_digits
                half_digits = str(int(half_digits) + 1)
                full_digits = int(half_digits + half_digits)

        return inv_ids_sum

    def _star_2(self) -> int:
        """Solve puzzle 2

        :return:
        """
        input_file_path = self.get_input_file_path()

        with open(input_file_path, 'r') as of:
            line = of.readline()
            ranges = line.strip().split(',')

        inv_ids_sum = 0
        for rng in ranges:
            range_first, range_last = rng.split('-')

            range_min = int(range_first)
            range_max = int(range_last)
            rep = len(range_last)

            seen = set()
            pattern = '0'
            while True:
                # Increment the pattern by 1
                pattern = str(int(pattern) + 1)
                # Compute the full digits
                full_digits = int(''.join([pattern] * rep))
                if full_digits < range_min:
                    continue
                if full_digits > range_max:
                    rep -= 1
                    if rep < 2:
                        break
                    else:
                        pattern = str(int(pattern) - 1)
                        continue
                # It is in the range, check if we haven't counted it
                # If we have e.g. 222222 we can build it with 6x 2, 3x 22 and 2x 222
                # Similar with 10101010: 4x 10 and 2x 1010
                if full_digits not in seen:
                    inv_ids_sum += full_digits
                    seen.add(full_digits)
                    #print(" inv id found:", full_digits)

        return inv_ids_sum



