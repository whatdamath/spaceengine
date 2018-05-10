
import matplotlib.pyplot as plt
import numpy as np

with open("d:/weather.txt" ,'r') as data:
    read_data=data.readlines()
    
year=[]
maxtemp=[]
mintemp=[]
avtemp=[]

for i in read_data:
    year.append(float(i[0:4]))
    maxtemp.append(float(i[5:9]))
    mintemp.append(float(i[10:14]))
    avtemp.append((float(i[5:9])+float(i[10:14]))/2.0)

plt.title("Temperature since 1905")
plt.xlabel("Years")
plt.ylabel("Degrees in F")
plt.plot(year, avtemp)
plt.xticks(np.arange(1905, max(year), 10.0))
plt.plot(year, np.poly1d(np.polyfit(year, avtemp, 1))(year))
plt.show()

