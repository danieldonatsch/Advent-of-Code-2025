from . import base_solution as bs


class SolutionDay05(bs.BaseSolution):
    def __init__(self, day_num: int, example=False, verbose=False):
        super().__init__(day_num, example, verbose=verbose)

        self.intervals = []

    def _star_1(self) -> int:
        """Solve puzzle 1

        :return:
        """
        input_file_path = self.get_input_file_path()

        def add_interval(intverval_str) -> None:
            interval = intverval_str.split('-')
            self.intervals.append((int(interval[0]), int(interval[1])))

        def check(num) -> int:
            for (s, e) in self.intervals:
                if s <= num <= e:
                    # Found in interval
                    return 1
            # Not in interval
            return 0


        check_id = False
        ids_in_intervals = 0
        for line in self.file_reader(input_file_path):
            if line == "":
                check_id = True
                continue

            if check_id:
                ids_in_intervals += check(int(line))
            else:
                add_interval(line)

        return ids_in_intervals


    def _star_2(self) -> int:
        """Solve puzzle 2

        :return:
        """

        self.intervals.sort()

        merged_intervals = []
        new_s, new_e = -1, -1
        for (s, e) in self.intervals:
            if new_s == -1:
                new_s, new_e = s, e
                continue
            if s > new_e:
                # current "open" interval is finished
                merged_intervals.append((new_s, new_e))
                new_s, new_e = s, e
            else:
                # Overlap?
                new_e = max(new_e, e)

        # Add the last "open" interval:
        merged_intervals.append((new_s, new_e))

        # Count numbers in intervals
        tot_num_in_int = 0
        for (s, e) in merged_intervals:
            tot_num_in_int += (e-s+1)

        return tot_num_in_int