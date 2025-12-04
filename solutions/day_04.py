from . import base_solution as bs


class SolutionDay04(bs.BaseSolution):
    def __init__(self, day_num: int, example=False, verbose=False):
        super().__init__(day_num, example, verbose=verbose)

    def _star_1(self) -> int:
        """Solve puzzle 1

        :return:
        """
        input_file_path = self.get_input_file_path()

        grid = []
        for line in self.file_reader(input_file_path):
            grid.append(list(line))

        movable_paper_roles = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != '@':
                    continue

                # Check all neighbors
                paper_role_count = 0
                for ii, jj in [(i-1, j), (i+1, j),
                               (i, j-1), (i, j+1),
                               (i-1, j-1), (i-1, j+1),
                               (i+1, j-1), (i+1, j+1)]:
                    if 0 <= ii < len(grid) and 0 <= jj < len(grid[i]):
                        paper_role_count += int(grid[ii][jj] == '@')

                    if paper_role_count > 3:
                        break

                movable_paper_roles += int(paper_role_count < 4)

        return movable_paper_roles

    def _star_2(self) -> int:
        """Solve puzzle 2

        :return:
        """
        input_file_path = self.get_input_file_path()

        grid = []
        debug_grid = []
        for line in self.file_reader(input_file_path):
            grid.append(list(line))
            debug_grid.append(list(line))

        movable_paper_roles = 0
        keep_going = True

        while keep_going:
            keep_going = False

            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] != '@':
                        continue

                    # Check all neighbors
                    paper_role_count = 0
                    for ii, jj in [(i-1, j), (i+1, j),
                                   (i, j-1), (i, j+1),
                                   (i-1, j-1), (i-1, j+1),
                                   (i+1, j-1), (i+1, j+1)]:
                        if 0 <= ii < len(grid) and 0 <= jj < len(grid[i]):
                            paper_role_count += int(grid[ii][jj] == '@')

                        if paper_role_count > 3:
                            break

                    if paper_role_count < 4:
                        movable_paper_roles += 1
                        grid[i][j] = 'X'
                        keep_going = True

        return movable_paper_roles