from math import sin, cos
from matplotlib import pyplot as plt
from argparse import ArgumentParser


def tree_of_life(spread, scale_factor, height, layers, plot):
    """
    Prints the tree of life plot

    Parameters
    ----------
    spread: float
        The amount that the angle will change by each layer
    scale_factor: float
        The amount that the height will change by each layer
    height: float
        The height of the first line
    layers: int
        The number of layers desired in the tree
    plot: bool
        If true, plots and saves the tree plot

    """

    # current number of layers
    number_of_layers = 1
    # starting point of the first line
    starting_point = [0, 0]
    # ending point of the first line
    first_line = [0, height]
    start = [{"x": first_line[0], "y": height, "angle": 0}]

    if plot:
        plt.plot(starting_point, first_line)

    while number_of_layers < layers:
        end = []

        for j in start:
            # define current x, y, and angle
            current_x = j["x"]
            current_y = j["y"]
            current_angle = j["angle"]

            # calculate new left x, y, angle
            new_la = current_angle - spread
            new_lx = current_x + height*sin(new_la)
            new_ly = current_y+height*cos(new_la)

            # calculate new right x, y, angle
            new_ra = current_angle+spread
            new_rx = current_x + height*sin(new_ra)
            new_ry = current_y + height*cos(new_ra)

            # create the new dictionaries
            new_left = {"x": new_lx, "y": new_ly, "angle": new_la}
            new_right = {"x": new_rx, "y": new_ry, "angle": new_ra}

            # append the new dictionaries to the new points
            end.append(new_left)
            end.append(new_right)

            # plot the left and right brance
            if plot:
                plt.plot([current_x, new_lx], [current_y, new_ly])
                plt.plot([current_x, new_rx], [current_y, new_ry])
        start = end
        height *= scale_factor
        number_of_layers += 1
    if plot:
        plt.savefig('tree.png')


# argparse arguments
if __name__ == "__main__":
    parser = ArgumentParser(description="Generate Tree")
    parser.add_argument("spread")
    parser.add_argument("scale_factor")
    parser.add_argument("height")
    parser.add_argument("layers")
    parser.add_argument("--plot", action='store_true')
    arguments = parser.parse_args()
    tree_of_life(float(arguments.spread), float(arguments.scale_factor),
                 float(arguments.height), int(arguments.layers),
                 bool(arguments.plot))
