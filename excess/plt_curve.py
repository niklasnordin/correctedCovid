import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
import math

import pandas as pd
import numpy as np
from scipy.optimize import minimize

country="Sweden"
#country="United States"
#country="Italy"
#country="Spain"
#country="Portugal"
#country="Belgium"
#country="Netherlands"
#country="Norway"
#country="United Kingdom"
#country="Denmark"
#country="Iceland"
country="Germany"
#country="France"

reported = {}
reported["Belgium"] = 19441
reported["United States"] = 354391
reported["Sweden"] = 9771
reported["Italy"] = 74159
reported["Spain"] = 50837
reported["Norway"] = 436
reported["United Kingdom"] = 73512
reported["Denmark"] = 1298
reported["Iceland"] = 29
reported["Germany"] = 34194
reported["France"] = 64780

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
w15 = []
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
        if math.isnan(a15):
            a15 = a19
        xmin = a20 - min(a15, a16, a17, a18, a19)
        xmax = a20 - max(a15, a16, a17, a18, a19)
#        print("{} : xmin = {} {} {} {} {} {}".format(i,xmin,a15,a16,a17,a18,a19))
        if not math.isnan(xa):
            sum_av += xa
        if not math.isnan(xmin):
            sum_min += xmin
        if not math.isnan(xmax):
            sum_max += xmax
            
        y1519.append(a1519)
        if not math.isnan(a15):
            y15.append(a15)
            w15.append(weeks[i])
            
        y16.append(a16)
        y17.append(a17)
        y18.append(a18)
        y19.append(a19)
        y20.append(a20)        
        w.append(weeks[i])
        
fig, ax = plt.subplots(figsize=(15,6))

plt.plot(w15, y15, color='grey', linewidth=0.5, label="2015")
plt.plot(w, y16, color='grey', linewidth=0.5, label="2016")
plt.plot(w, y17, color='grey', linewidth=0.5, label="2017")
plt.plot(w, y18, color='green', linewidth=0.5, label="2018")
plt.plot(w, y19, color='blue', linewidth=0.5, label="2019")
plt.plot(w, y20, color='k', label="2020")

plt.plot(w, y1519, color="red", label="2015-2019")

xt = ax.get_xticks()
ax.set_xticks(np.arange(1, 53))

plt.legend()
plt.grid()
plt.xlabel("Week")
plt.ylabel("Mortality")
plt.title("{} : min={} : av={} : max={} : reported={}".format(country, int(sum_min), int(sum_av), int(sum_max), reported[country]))

print("Excess death min     : {:d}".format(int(sum_min)))
print("Excess death max     : {:d}".format(int(sum_max)))
print("Excess death average : {:d}".format(int(sum_av)))

plt.savefig("{}_fig.png".format(country))

plt.show()

