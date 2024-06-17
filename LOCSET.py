import numpy as np
import pandas as pd
from math import sqrt
import matplotlib.pyplot as plt
import os
import torch

data_num = int(10e8)
time = 10
dt = time / data_num
tao = 3 / 10e3
len = int(tao / dt)
t = np.linspace(0, time, data_num)
w_ref = 2*np.pi*1
noise0 = 2*np.pi*np.sin(w_ref*t)

plt.plot(noise0)