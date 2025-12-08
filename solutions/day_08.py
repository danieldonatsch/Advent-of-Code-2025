from . import base_solution as bs


class SolutionDay08(bs.BaseSolution):
    def __init__(self, day_num: int, example=False, verbose=False):
        super().__init__(day_num, example, verbose=verbose)
        self.n_conns = 10 if example else 1000
        self.nodes = []
        self.connections = []
        self.circuits = []

    def _add_connection_to_circuits(self, con_num):

        _, n1, n2 = self.connections[con_num]
        c1, c2 = -1, -1
        for j, circuit in enumerate(self.circuits):
            if n1 in circuit:
                c1 = j
                circuit.add(n1)
            if n2 in circuit:
                c2 = j
                circuit.add(n2)
        # After checking all existing circuits
        if c1 == c2:
            # Both are already in same circuit. Nothing to do
            return
        else:
            if c1 == -1:
                # Node 1 is in no circuit, but c2 is. So add node 1 to the circuit of node 2
                self.circuits[c2].add(n1)
            elif c2 == -1:
                # Node 2 is in no circuit, but c2 is. So, add node 2 to the circuit of node 1
                self.circuits[c1].add(n2)
            else:
                self.circuits[c1] = self.circuits[c1].union(self.circuits[c2])
                del self.circuits[c2]

    def _star_1(self) -> int:
        """Solve puzzle 1

        :return:
        """
        input_file_path = self.get_input_file_path()

        for i, line in enumerate(self.file_reader(input_file_path)):
            self.circuits.append({i})
            x, y, z = line.split(',')
            x, y, z = int(x), int(y), int(z)
            self.nodes.append((x, y, z))
            for j in range(i):
                d = (self.nodes[j][0] - x) * (self.nodes[j][0] - x) + \
                    (self.nodes[j][1] - y) * (self.nodes[j][1] - y) + \
                    (self.nodes[j][2] - z) * (self.nodes[j][2] - z)
                self.connections.append((d, i, j))

        self.connections.sort()
        #for d, i, j in self.connections[:self.n_conns]:
        #    print(d, i, j, self.nodes[i], self.nodes[j])

        for i in range(self.n_conns):
            self._add_connection_to_circuits(i)

        circ_lens = []
        for circuit in self.circuits:
            circ_lens.append(len(circuit))

        circ_lens.sort(reverse=True)

        return circ_lens[0] * circ_lens[1] * circ_lens[2]


    def _star_2(self) -> int:
        """Solve puzzle 2

        :return:
        """
        # Keep adding connections...
        for con_num in range(self.n_conns, len(self.connections)):
            self._add_connection_to_circuits(con_num)
            # Until all nodes belong to one circuit...
            if len(self.circuits) == 1:
                # Then multiply the x coordinates of them.
                d, n1, n2 = self.connections[con_num]
                return self.nodes[n1][0] * self.nodes[n2][0]

        return -1