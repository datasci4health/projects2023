""" Data Processing and Filtering """

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('..')
df = pd.read_csv('data\raw\hans_2001.csv', header=0)
