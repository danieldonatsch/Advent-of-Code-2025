from . import base_solution as bs


class SolutionDay01(bs.BaseSolution):
    def __init__(self, day_num: int, example=False, verbose=False):
        super().__init__(day_num, example, verbose=verbose)

    def _star_1(self) -> int:
        """Solve puzzle 1

        :return:
        """
        input_file_path = self.get_input_file_path()

        curr_pos = 50
        zero_count = 0
        with open(input_file_path, 'r') as of:
            while line := of.readline():
                line = line.strip()
                direction = line[0]
                steps = int(line[1:])
                if direction == 'L':
                    curr_pos -= steps
                else:
                    curr_pos += steps
                curr_pos = curr_pos % 100
                if curr_pos == 0:
                    zero_count += 1

        return zero_count

    def _star_2(self) -> int:
        """Solve puzzle 2

        :return:
        """
        input_file_path = self.get_input_file_path()

        curr_pos = 50
        zero_count = 0
        with open(input_file_path, 'r') as of:
            while line := of.readline():
                line = line.strip()
                direction = line[0]
                steps = int(line[1:])
                # If we do more than 100 steps, we pass for sure once zero!
                zero_count += int(steps/100)
                # Keep just the rest...
                steps = steps % 100

                if direction == 'L':
                    new_pos = curr_pos - steps
                    # Check, if we crossed zero. We haven't crossed it, if we've been at 0 just before
                    if new_pos <= 0 and curr_pos != 0:
                        zero_count += 1
                else:
                    new_pos = curr_pos + steps
                    # Check, if we crossed zero. We haven't crossed it, if we've been at 0 just before
                    if new_pos > 99 and curr_pos != 0:
                        zero_count += 1
                # Make the new position the current position and make sure to stay in the range
                curr_pos = new_pos % 100

        return zero_count
