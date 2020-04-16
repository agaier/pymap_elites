# only required to run python3 examples/cvt_rastrigin.py
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import math

import map_elites.cvt as cvt_map_elites
import map_elites.common as cm_map_elites


def rastrigin(xx):
    x = xx * 10 - 5
    f = 10 * x.shape[0] + (x * x - 10 * np.cos(2 * math.pi * x)).sum()
    return -f, np.array([xx[0], xx[1]])


# we do 10M evaluations, which takes a while in Python (but it is very fast in the C++ version...)
px = cm_map_elites.default_params.copy()
px["dump_period"] = 100000
px["dump_period"] = 100000
px["batch_size"] = 200
px["min"] = 0
px["max"] = 1
px["iso_sigma"] = 1./300.
px["line_sigma"] =  10./300.
px["parallel"] = True

archive = cvt_map_elites.compute(2, 10, rastrigin, n_niches=10000, max_evals=10e6, log_file=open('cover_max_median.dat', 'w'), params=px)
