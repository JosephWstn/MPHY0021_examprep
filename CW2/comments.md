Part 2a - perf_plot:
As more iterations are added, the time increases. Adding more layers it is clear that the time taken exponentially increases as more layers are added to the tree. This is expected as with each new layer, there are double the branches as each branch splits into two. Therefore an exponential increase in the time taken is expected.

Part 2b - perf_plot_np:
Up to around 15 layers, both methods are equally as quick and it is difficult to tell which is quicker. However beyond this, the numpy method become noticeably quicker. The numpy method still looks exponential but rises at a much slower rate than the original.