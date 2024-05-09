"""
Histogram: The histogram displays the frequency of values within different bins
    or intervals. Each bar represents the count of observations falling within that interval.
    The height of each bar indicates how many data points are in that range.
visualize Distributions with Seaborn:
seaborn is a library that uses matplotlib underneath to plot graphs. It will be used
to visualize random distributions.
"""
import matplotlib.pyplot as plt
import seaborn as sns


sns.distplot([0, 1, 5, 0, 9, 5], kde = 0,   color='red')
plt.show()

"""
Plotting a distplot without the histogram.
sns.distplot([0, 1, 2, 3, 4, 5], hist = False)
"""