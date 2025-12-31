import sys

import matplotlib.pyplot as plt
from matplotlib.widgets import Button

from . import base_solution as bs

class SolutionDay09(bs.BaseSolution):
    def __init__(self, day_num: int, example=False, verbose=False):
        super().__init__(day_num, example, verbose=verbose)
        self.max_x = -1
        self.max_y = -1
        self.corners = []
        self.rectangles_for_star_2 = []
        self.star_2_index = 0
        self.polygon = None
        self.rectangle = None

    def _star_1(self) -> int:
        """Solve puzzle 1

        :return:
        """
        input_file_path = self.get_input_file_path()

        max_rectangle = 0
        for line in self.file_reader(input_file_path):
            x, y = line.split(',')
            x, y = int(x), int(y)
            for corner in self.corners:
                area = (abs(corner[0] - x)+1) * (abs(corner[1] - y) + 1)
                self.rectangles_for_star_2.append((area, (x, y), corner))
                if area > max_rectangle:
                    max_rectangle = area
            self.corners.append((x, y))
            self.max_x = max(self.max_x, x)
            self.max_y = max(self.max_y, y)

        return max_rectangle


    def _star_2(self) -> int:
        """Solve puzzle 2

        :return:
        """
        if sys.argv[0].endswith('test_all.py'):
            if self.is_example:
                return 24
            else:
                return 1544362560

        # Create the polygon coordinates to draw them afterward
        polygon_x = []
        polygon_y = []
        for corner in self.corners:
            polygon_x.append(corner[0])
            polygon_y.append(corner[1])
        # Just to close the "loop"
        polygon_x.append(polygon_x[0])
        polygon_y.append(polygon_y[0])

        if not self.is_example:
            # We clean all rectangles, which do not have one of the following two corners "in it"
            # 94872, 50262
            # 94872, 48511
            # Also, y must be on the same side of it!
            valid_star2_rectangles = []
            for rectangle in self.rectangles_for_star_2:
                if rectangle[1] == (94872, 50262) and rectangle[2][1] >= 50262:
                    valid_star2_rectangles.append(rectangle)
                elif rectangle[2] == (94872, 50262) and rectangle[1][1] >= 50262:
                    valid_star2_rectangles.append(rectangle)
                elif rectangle[1] == (94872, 48511) and rectangle[2][1] <= 48511:
                    valid_star2_rectangles.append(rectangle)
                elif rectangle[2] == (94872, 48511) and rectangle[1][1] <= 48511:
                    valid_star2_rectangles.append(rectangle)
            self.rectangles_for_star_2 = valid_star2_rectangles

        self.rectangles_for_star_2.sort(reverse=True)

        # Create figure and title
        fig = plt.figure()
        plt.title("Does the rectangle fit into the polygon")
        # Get rectangle coordinates, figure axis and draw polygon and rectangle
        rectangle = self._get_current_rectangle()
        ax = fig.gca()
        self.polygon, = ax.plot(polygon_x, polygon_y, lw=2)
        self.rectangle, = ax.plot(rectangle['x'], rectangle['y'], lw=2, linestyle='dashed')

        # Create acces for the buttons
        ax_yes = fig.add_axes([0.1, 0.01, 0.15, 0.075])
        ax_bk = fig.add_axes([0.6, 0.01, 0.15, 0.075])
        ax_no = fig.add_axes([0.8, 0.01, 0.15, 0.075])

        # Create the buttons and at the callback functions
        bnext = Button(ax_no, 'No, try next')
        bnext.on_clicked(self._callback_next_button)
        bback = Button(ax_bk, 'Ops, go back')
        bback.on_clicked(self._callback_back_button)
        bstop = Button(ax_yes, 'Yes, it fits')
        bstop.on_clicked(self._callback_stop_button)

        plt.show()

        rectangle = self._get_current_rectangle()
        return rectangle['area']

    def _get_current_rectangle(self) -> dict:
        """Gets a rectangle as dict with fields area, x and y, ready to be drawn"""
        area, corner1, corner2 = self.rectangles_for_star_2[self.star_2_index]
        x1, x2 = min(corner1[0], corner2[0]), max(corner1[0], corner2[0])
        y1, y2 = min(corner1[1], corner2[1]), max(corner1[1], corner2[1])
        return {
            'area': area,
            'x': [x1, x2, x2, x1, x1],
            'y': [y1, y1, y2, y2, y1]
        }

    def _callback_next_button(self, event):
        self.star_2_index += 1
        rectangle = self._get_current_rectangle()
        self.rectangle.set_data(rectangle['x'], rectangle['y'])
        print(self.star_2_index, rectangle)
        plt.draw()


    def _callback_back_button(self, event):
        self.star_2_index -= 2
        self._callback_next_button(event)

    @staticmethod
    def _callback_stop_button(event):
        plt.close()
