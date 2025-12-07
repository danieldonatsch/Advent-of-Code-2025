from . import base_solution as bs


class SolutionDay06(bs.BaseSolution):
    def __init__(self, day_num: int, example=False, verbose=False):
        super().__init__(day_num, example, verbose=verbose)

    def _star_1(self) -> int:
        """Solve puzzle 1

        :return:
        """
        input_file_path = self.get_input_file_path()

        # Build the "grid" of values
        value_grid = []
        for line in self.file_reader(input_file_path):
            value_grid.append(
                [item for item in line.split(' ') if item != '']
            )

        # Process it column by column
        total_sum = 0
        n = len(value_grid[0])
        for col in range(n):
            # Figure out the operation
            sum_or_mult = 's' if value_grid[-1][col] == '+' else 'm'
            col_tot = None
            # Take one value after the other from the column...
            for row in range(len(value_grid)-1):
                val = int(value_grid[row][col])
                if row == 0:
                    col_tot = val
                else:
                    if sum_or_mult == 's':
                        col_tot += val
                    else:
                        col_tot *= val
            # Add the column value to the total sum
            total_sum += col_tot

        return total_sum


    def _star_2(self) -> int:
        """Solve puzzle 2

        :return:
        """
        def process_column(s, e):
            sum_or_mult = 's' if lines[-1][s] == '+' else 'm'
            col_tot = None

            for j in range(s, e):
                num_str = ''
                for line in lines[:-1]:
                    num_str = num_str + line[j]

                num = int(num_str)
                if col_tot is None:
                    col_tot = num
                else:
                    if sum_or_mult == 's':
                        col_tot += num
                    else:
                        col_tot *= num

            return col_tot

        input_file_path = self.get_input_file_path()

        with open(input_file_path, 'r') as of:
            lines = of.readlines()

        total_sum = 0
        s = 0
        for i in range(1, len(lines[-1])):
            # find range
            if lines[-1][i] != ' ':
                total_sum += process_column(s, i-1)
                s = i

        n = 0
        for line in lines:
            n = max(n, len(lines))

        total_sum += process_column(s, len(lines[0])-1)

        return total_sum