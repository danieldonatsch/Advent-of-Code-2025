from . import base_solution as bs


class SolutionDay10(bs.BaseSolution):
    def __init__(self, day_num: int, example=False, verbose=False):
        super().__init__(day_num, example, verbose=verbose)
        self.n_lights = 0

    def compute_lights_target(self, input) -> int:
        self.n_lights = 0
        lt = ''
        for character in input[1:-1]:
            self.n_lights += 1
            if character == '#':
                lt = lt + '1'
            else:
                lt = lt + '0'
        return int(lt, 2)

    def button_as_num(self, button_str):
        # Remove brackets
        switches = ['0'] * self.n_lights
        for switch in button_str[1:-1].split(','):
            switches[int(switch)] = '1'

        return int(''.join(switches), 2)

    @staticmethod
    def get_number_of_clicks(lights_target, buttons) -> int:
        #print(lights_target, buttons)
        clicks = 0
        lights = {0}
        while True:
            #print(lights)
            clicks += 1
            #print(clicks)
            next_lights = set()
            for light in lights:
                for button in buttons:
                    #print(light, button, light ^ button)
                    new_light = light ^ button
                    if new_light == lights_target:
                        #print(clicks)
                        return clicks
                    next_lights.add(new_light)
            lights = next_lights


    def _star_1(self) -> int:
        """Solve puzzle 1

        :return:
        """
        input_file_path = self.get_input_file_path()

        tot_num_clicks = 0
        for line in self.file_reader(input_file_path):
            items = line.split(' ')
            lights_target = self.compute_lights_target(items[0])
            buttons = [self.button_as_num(b) for b in items[1:-1]]
            num_clicks = self.get_number_of_clicks(lights_target, buttons)
            tot_num_clicks += num_clicks

        return tot_num_clicks


    def _star_2(self) -> int:
        """Solve puzzle 2

        :return:
        """
        input_file_path = self.get_input_file_path()

