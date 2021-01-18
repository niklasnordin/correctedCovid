import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

import pandas as pd
import numpy as np
from scipy.optimize import minimize

country="Sweden"

filename="Excess Mortality Data – HMD (2021).csv"
df = pd.read_csv(filename, sep=",")

countries = df["Entity"]
data = df["Week"]

print(data)

        

    




