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
country="SWE"
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
normalized_cases=[]
tests=[]

for i,d in enumerate(c):
    if d==country:
        cases.append(data[nc][i])
        deaths.append(data[nd][i])
        date.append(data[da][i])
        pos_rate.append(data[pr][i])
        tests.append(data[nt][i])

def_test=1000000.0/7.0
for i,d in enumerate(pos_rate):
    normalized_cases.append(def_test*d)


free_test_date = [ "2020-06-04" ]
free_test_case = [ 4000.0 ]

fig, ax = plt.subplots(figsize=(15,6))

dco=np.convolve(cases, np.ones(days)/days, mode='same')
dco2=np.convolve(cases, np.ones(days2)/days2, mode='same')
dcn=np.convolve(normalized_cases, np.ones(days)/days, mode='same')
dcn2=np.convolve(normalized_cases, np.ones(days2)/days2, mode='same')

plt.plot(date,dco, color='blue')
plt.plot(date,dcn, color='red')

plt.bar(date,cases, width=1, alpha=0.5, color='blue', label="cases")
plt.bar(date,normalized_cases, width=0.5, alpha=0.5, color='red', label="Normalized for 1 000 000 tests")
#plt.bar(free_test_date,free_test_case, width=1, alpha=0.5, color="green", label="Start of free testing")

xt = ax.get_xticks()
ax.set_xticks(np.arange(xt[0],xt[np.size(xt)-1], 30))
plt.legend()
plt.grid()
plt.xlabel("Date")
plt.ylabel("number of positive tests")
plt.title("Number of positive corona tests in Belgium")
plt.savefig("cases_owid_swe.png")
plt.show()

#print(tests)
