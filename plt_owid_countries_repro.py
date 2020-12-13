import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

import pandas as pd
import numpy as np
from scipy.optimize import minimize

filename="owid-covid-data.csv"
data = pd.read_csv(filename, sep=",")

days=5
days2=14
#country= [ "SWE", "USA", "ITA", "BEL", "ESP", "POL", "GBR" ]
#country= [ "SWE", "DNK", "NOR", "FIN" ]
country = [ "SWE", "USA", "ITA" ]
c = data["iso_code"]

nc="new_cases"
nd="new_deaths"
da="date"
pr="positive_rate"
nt='new_tests'
rr='reproduction_rate'

cases=[]
deaths=[]
date=[]
pos_rate=[]
psr = []
normalized_cases=[]
tests=[]
all_dates=[]
repro=[]

for cnt in country:
    pos_rate= []
    date = []
    repi = []
    tt = []
    for i,d in enumerate(c):
        if d==cnt:
            pos_rate.append(data[pr][i])
            repi.append(data[rr][i])
            date.append(data[da][i])
            tt.append(data[nt][i])
    tests.append(tt)
    psr.append(pos_rate)
    repro.append(repi)
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
    dcn=np.convolve(repro[i], np.ones(days)/days, mode='same')
    #plt.plot(all_dates[i],dcn, label=country[i])
    #plt.plot(all_dates[i], repro[i], label=country[i])
    plt.plot(all_dates[i], dcn, label=country[i])

xt = ax.get_xticks()
ax.set_xticks(np.arange(xt[0],xt[np.size(xt)-1], 30))
plt.legend()
plt.grid()
plt.xlabel("Date")
plt.ylabel("Reproduction Rate")
plt.title("Real Time Estimation of the R value")
plt.savefig("cases_owid_cntr.png")
plt.show()

