import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
import math

import pandas as pd
import numpy as np
from scipy.optimize import minimize

country="Sweden"
country="United States"

av1519 = "average_deaths_2015_2019_all_ages"
d15 = "deaths_2015_all_ages"
d16 = "deaths_2016_all_ages"
d17 = "deaths_2017_all_ages"
d18 = "deaths_2018_all_ages"
d19 = "deaths_2019_all_ages"
d20 = "deaths_2020_all_ages"


filename="Excess Mortality Data – HMD (2021).csv"
df = pd.read_csv(filename, sep=",")

countries = df["Entity"]
weeks = df["Week"]

y1519 = []
y20 = []
y19 = []
y18 = []
y17 = []
y16 = []
y15 = []

w = []
sum_min = 0.0
sum_max = 0.0
sum_av = 0.0

for i,c in enumerate(countries):
    if c == country:
        a1519 = df[av1519][i]
        a15 = df[d15][i]
        a16 = df[d16][i]
        a17 = df[d17][i]
        a18 = df[d18][i]
        a19 = df[d19][i]
        a20 = df[d20][i]        
        xa = a20 - a1519
        xmin = a20 - min(a15, a16, a17, a18, a19)
        xmax = a20 - max(a15, a16, a17, a18, a19)
        
        if not math.isnan(xa):
            sum_av += xa
        if not math.isnan(xmin):
            sum_min += xmin
        if not math.isnan(xmax):
            sum_max += xmax
            
        y1519.append(a1519)
        y15.append(a15)
        y16.append(a16)
        y17.append(a17)
        y18.append(a18)
        y19.append(a19)
        y20.append(a20)        
        w.append(weeks[i])
        
fig, ax = plt.subplots(figsize=(15,6))

plt.plot(w, y15, color='grey', linewidth=0.5, label="2015")
plt.plot(w, y16, color='grey', linewidth=0.5, label="2016")
plt.plot(w, y17, color='grey', linewidth=0.5, label="2017")
plt.plot(w, y18, color='grey', linewidth=0.5, label="2018")
plt.plot(w, y19, color='grey', linewidth=0.5, label="2019")
plt.plot(w, y20, color='k', label="2020")

plt.plot(w, y1519, color="red", label="2015-2019")

plt.legend()
plt.grid()
plt.xlabel("Week")
plt.ylabel("Excess Mortality")
plt.title("{} : min={} : av={} : max={}".format(country, int(sum_min), int(sum_av), int(sum_max)))

print("Excess death min     : {:d}".format(int(sum_min)))
print("Excess death max     : {:d}".format(int(sum_max)))
print("Excess death average : {:d}".format(int(sum_av)))

plt.savefig("figure.png")

plt.show()

