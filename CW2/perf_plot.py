from tree import tree_of_life
from tree_np import tree_of_life_numpy
import time
from matplotlib import pyplot as plt


def time_perf(layers, numpy):
    """
    Finds array of times taken for tree of life from 0 to number of layers with
    numpy or original method

    Parameters
    ----------
    layers: int
        The number of layers to go up to for the tree
    numpy: bool
        If True, will use the numpy method
    Returns
    -------
    times: list
        List of all the times taken to plot the tree for each layer
    """
    times = []
    for i in range(layers):

        if numpy:
            start_time = time.time()
            tree_of_life_numpy(spread=0.1, scale_factor=0.6,
                               height=1, layers=i, plot=False)
            times.append(time.time() - start_time)
        else:
            start_time = time.time()
            tree_of_life(spread=0.1, scale_factor=0.6,
                         height=1, layers=i, plot=False)
            times.append(time.time() - start_time)
    return times


times = time_perf(layers=21, numpy=False)
times_np = time_perf(layers=21, numpy=True)


# plot time analysis for just original
plt.plot(1)
plt.plot(times, "+")
plt.ylabel("Total runtime / s")
plt.xlabel("Iterations")
plt.title("Time to produce the tree for different number of iterations")
plt.grid(b=True)
plt.savefig('perf_plot.png')

# plot time original for comparison of original and numpy
plt.plot(2)
plt.plot(times, "b+", label="Original")
plt.plot(times_np, "r+", label="Numpy")
plt.legend(loc=2)
plt.title("Comparison of time to produce the tree for different \n"
          "number of iterations for original and numpy method")
plt.ylabel("Total runtime / s")
plt.xlabel("Iterations")
plt.grid(b=True)
plt.savefig("perf_plot_np.png")
