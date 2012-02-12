#!/usr/bin/env python 
import numpy

# plot the cdf of plot_data
def plot_cdf(subplot, plot_data, **kwargs):
    xlist = plot_data[:]
    xlist = list(set(xlist))
    xlist.sort()
    ylist = []
    so_far = 0.0
    total = len(plot_data)
    for i in xrange(len(xlist)):
        count = plot_data.count(xlist[i])
        so_far = so_far + (100 * count) / float(total)
        ylist.append(so_far)
        if so_far > 99.99:
            break
    return subplot.plot(xlist[:i + 1], [j / 100.0 for j in ylist], **kwargs)

def plot_list(subplot, plot_data, marker = None, markevery = None):
    xlist = xrange(len(plot_data))
    return subplot.plot(xlist, plot_data, marker, markevery)

def plot_bar(subplot, data, bottom = None, **kwargs):
    ind = numpy.arange(len(data))
    width = 0.35
    return subplot.bar(ind, data, width, bottom, **kwargs) 
