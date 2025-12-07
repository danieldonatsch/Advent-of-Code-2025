from . import base_solution as bs


class SolutionDay07(bs.BaseSolution):
    def __init__(self, day_num: int, example=False, verbose=False):
        super().__init__(day_num, example, verbose=verbose)

    def _star_1(self) -> int:
        """Solve puzzle 1

        :return:
        """
        input_file_path = self.get_input_file_path()

        beams = None
        split_count = 0
        for line in self.file_reader(input_file_path):
            new_beams = set()
            for i, char in enumerate(line):
                if beams is None:
                    if char == 'S':
                        beams = {i}
                        break
                else:
                    if char == '^' and i in beams:
                        split_count += 1
                        new_beams.add(i-1)
                        new_beams.add(i+1)
                        beams.remove(i)
            beams = beams.union(new_beams)

        return split_count

    def _star_2(self) -> int:
        """Solve puzzle 2

        :return:
        """
        input_file_path = self.get_input_file_path()

        paths = dict()

        for line in self.file_reader(input_file_path):
            if not paths:
                # Deal with the first line
                paths[line.find('S')] = 1
                continue
            new_path = dict()
            # Check all current paths/beams.
            for pos, num in paths.items():
                if line[pos] == '^':
                    # If the beam is split, "shift" the path to left and right
                    # but make sure, keep potentially existing paths!
                    new_path[pos-1] = new_path.get(pos-1, 0) + num
                    new_path[pos+1] = new_path.get(pos+1, 0) + num
                else:
                    # No split, keep the current path
                    new_path[pos] = new_path.get(pos, 0) + num

            paths = new_path

        return sum(paths.values())