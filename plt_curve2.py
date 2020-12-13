import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

import pandas as pd
import numpy as np
from scipy.optimize import minimize

# death rate is assumed to be constant
# it is the percentage of sick people dying
# sick people is a percentage of total people
#

#filename="WHO-COVID-19-global-data.csv"
filename="owid-covid-data.csv"
data = pd.read_csv(filename, sep=",")
weight = pd.read_csv("weekly_test_sweden.dat", sep=" ")

w = weight["tests"]

country="Sweden"
#country="United States of America"
nc="new_cases"
nd="new_deaths"
da="date"

c = data["location"]

days=7
days2=14
factor=15
shift=1
cases=[]
deaths=[]
date=[]
normalized_cases = []

for i,d in enumerate(c):
    if d==country:
        cases.append(data[nc][i])
        deaths.append(data[nd][i])
        date.append(data[da][i])

for i,d in enumerate(cases):
    dx = date[i]
    ds = (dx).split('-')
    week = float(datetime.date(int(ds[0]),int(ds[1]),int(ds[2])).isocalendar()[1])
    wi = w[week]
    factor = 200000.0/wi
    factor = min(15.0, factor)
    normalized_cases.append(d*factor)

free_test_date = [ "2020-06-04" ]
free_test_case = [ 7000.0 ]

fig, ax = plt.subplots(figsize=(15,6))

dco=np.convolve(cases, np.ones(days)/days, mode='same')
dco2=np.convolve(cases, np.ones(days2)/days2, mode='same')
dcn=np.convolve(normalized_cases, np.ones(days)/days, mode='same')
dcn2=np.convolve(normalized_cases, np.ones(days2)/days2, mode='same')

plt.plot(date,dco, color='blue')
plt.plot(date,dcn, color='red')

plt.bar(date,cases, width=1, alpha=0.5, color='blue', label="cases")
plt.bar(date,normalized_cases, width=0.5, alpha=0.5, color='red', label="Normalized for 200 000 tests")
plt.bar(free_test_date,free_test_case, width=1, alpha=0.8, color="green", label="Start of free testing")

xt = ax.get_xticks()

ax.set_xticks(np.arange(xt[0],xt[np.size(xt)-1], 30))
plt.ylim(0,7500)
plt.legend()
plt.grid()
plt.xlabel("Date")
plt.ylabel("number of positive tests")
plt.title("Number of positive corona tests in Sweden")
plt.savefig("cases.png")
plt.show()
    
