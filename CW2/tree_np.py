from argparse import ArgumentParser
from math import sin, cos
from matplotlib import pyplot as plt
import numpy as np


def tree_of_life_numpy(spread, scale_factor, height, layers, plot):
    """
    Prints the tree of life plot using numpy data

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
    d = np.array([[0, height, 0]])
    starting_point = [0, 0]
    first_line = [0, height]
    if plot:
        # plot first vertical line
        plt.plot(starting_point, first_line)
    number_of_layers = 1

    # loop for number of branch interations
    while number_of_layers < layers:

        # access Xs, Ys, angles
        Xs = d[:, 0]
        Ys = d[:, 1]
        angles = d[:, 2]

        # new angles
        new_angles_l = angles - spread
        new_angles_r = angles + spread

        # define the new left x, y
        new_lx = Xs + height * np.sin(new_angles_l)
        new_ly = Ys + height * np.cos(new_angles_l)

        # define the new right x, y
        new_rx = Xs + height * np.sin(new_angles_r)
        new_ry = Ys + height * np.cos(new_angles_r)

        # create arrays of [x,y,angle] for each new point by
        # stacking the arrays of [x], [y], [angle]
        new_left = np.dstack((new_lx, new_ly, new_angles_l))
        new_right = np.dstack((new_rx, new_ry, new_angles_r))

        if plot:
            plt.plot([Xs, new_lx], [Ys, new_ly])  # plot left branch
            plt.plot([Xs, new_rx], [Ys, new_ry])  # plot right branch
        # change the length, making it 0.6 * length of last branch
        height *= scale_factor

        number_of_layers += 1
        d = np.append(new_left[0], new_right[0], axis=0)
    if plot:
        plt.savefig('tree_np.png')


if __name__ == "__main__":
    parser = ArgumentParser(description="Generate Tree")
    parser.add_argument("spread")
    parser.add_argument("scale_factor")
    parser.add_argument("height")
    parser.add_argument("layers")
    parser.add_argument("--plot", action="store_true")
    arguments = parser.parse_args()
    tree_of_life_numpy(float(arguments.spread), float(arguments.scale_factor),
                       float(arguments.height), int(arguments.layers),
                       bool(arguments.plot))
