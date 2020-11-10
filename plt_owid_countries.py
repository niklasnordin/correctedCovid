import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

import pandas as pd
import numpy as np
from scipy.optimize import minimize

filename="owid-covid-data.csv"
data = pd.read_csv(filename, sep=",")

days=7
days2=14
country= [ "SWE", "USA", "ITA", "BEL", "ESP", "POL", "GBR" ]
c = data["iso_code"]

nc="new_cases"
nd="new_deaths"
da="date"
pr="positive_rate"
nt='new_tests'

cases=[]
deaths=[]
date=[]
pos_rate=[]
psr = []
normalized_cases=[]
tests=[]
all_dates=[]
for cnt in country:
    pos_rate= []
    date = []
    for i,d in enumerate(c):
        if d==cnt:
            pos_rate.append(data[pr][i])
            date.append(data[da][i])
    psr.append(pos_rate)
    all_dates.append(date)    

ncall = []
def_test=1000000.0/7.0
for p in psr:
    normalized_cases = []
    for i,d in enumerate(p):
        normalized_cases.append(def_test*d)
    ncall.append(normalized_cases)

fig, ax = plt.subplots(figsize=(15,6))


for i,p in enumerate(ncall):
    print(i)
    dcn=np.convolve(p, np.ones(days)/days, mode='same')
    plt.plot(all_dates[i],dcn, label=country[i])

#plt.bar(date,cases, width=1, alpha=0.5, color='blue', label="cases")
#plt.bar(date,normalized_cases, width=0.5, alpha=0.5, color='red', label="Normalized for 1 000 000 tests")
#plt.bar(free_test_date,free_test_case, width=1, alpha=0.5, color="green", label="Start of free testing")

xt = ax.get_xticks()
ax.set_xticks(np.arange(xt[0],xt[np.size(xt)-1], 30))
plt.legend()
plt.grid()
plt.xlabel("Date")
plt.ylabel("number of positive tests")
plt.title("Number of positive corona tests scaled to 1 000 000 tests")
plt.savefig("cases_owid_cntr.png")
plt.show()

#print(tests)
