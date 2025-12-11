from collections import defaultdict
from functools import lru_cache

from . import base_solution as bs


class SolutionDay11(bs.BaseSolution):
    def __init__(self, day_num: int, example=False, verbose=False):
        super().__init__(day_num, example, verbose=verbose)
        self.graph = defaultdict(list)

    def build_graph(self, star=1) -> None:
        # Get input file path
        input_file_path = self.get_input_file_path(star=star)
        # Reset the graph
        self.graph = defaultdict(list)
        # Build Graph
        for line in self.file_reader(input_file_path):
            servers = line.split(' ')
            server0 = servers[0][:-1]    # Remove the column
            self.graph[server0].extend(servers[1:])


    def _star_1(self) -> int:
        """Solve puzzle 1

        :return:
        """
        # Do a depth first search with caching
        @lru_cache
        def dfs(server) -> int:
            if server == 'out':
                return 1
            n_con = 0
            for next_server in self.graph[server]:
                n_con += dfs(next_server)
            return n_con

        self.build_graph(1)

        # Do a depth first search with caching
        return dfs('you')


    def _star_2(self) -> int:
        """Solve puzzle 2

        :return:
        """
        @lru_cache
        def dfs(server, dac_visited, fft_visited) -> int:
            if server == 'out':
                return int(dac_visited and fft_visited)

            if server == 'dac':
                dac_visited = True
            if server == 'fft':
                fft_visited = True

            n_con = 0
            for next_server in self.graph[server]:
                n_con += dfs(next_server, dac_visited, fft_visited)
            return n_con

        self.build_graph(2)

        return dfs('svr', False, False)