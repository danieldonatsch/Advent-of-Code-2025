from . import base_solution as bs


class SolutionDay03(bs.BaseSolution):
    def __init__(self, day_num: int, example=False, verbose=False):
        super().__init__(day_num, example, verbose=verbose)

    def _star_1(self) -> int:
        """Solve puzzle 1

        :return:
        """
        input_file_path = self.get_input_file_path()

        sum_of_line_max = 0
        for line in self.file_reader(input_file_path):
            first_digit, second_digit = -1, -1
            for digit in line[:-1]:
                d = int(digit)
                if d > first_digit:
                    first_digit = d
                    second_digit = -1
                elif d > second_digit:
                    second_digit = d
            # use the last digit of the line
            if int(line[-1]) > second_digit:
                second_digit = int(line[-1])

            sum_of_line_max += 10 * first_digit + second_digit

        return sum_of_line_max

    def _star_2(self) -> int:
        """Solve puzzle 2

        :return:
        """
        input_file_path = self.get_input_file_path()

        n = 12  # n: the number of digits we use
        sum_of_line_max = 0
        for line in self.file_reader(input_file_path):
            l = len(line)   # l the line length
            used_digits = [-1] * n
            for i, digit in enumerate(line):    # i the number of digit in the line
                d = int(digit)  # d: the digit as integer
                # Check if the new digit is larger than...
                # Loop starts at that position where still enough digits are left to cover the rest of the "used bits"
                # This is the number of used digits (n) minus the number of digits left in the line (l - i(
                for j in range(max(0, n-(l-i)), n):
                    if d > used_digits[j]:
                        used_digits[j] = d
                        # Set all alter digits to -1
                        for k in range(j+1, n):
                            used_digits[k] = -1
                        # Leaf the loop
                        break
            # Finally, we found the digits we want to use. Convert them into a number and sum it to the total.
            tot_val = 0
            for used_digit in used_digits:
                tot_val *= 10
                tot_val += used_digit
            sum_of_line_max += tot_val

        return sum_of_line_max