import requests

url = "https://disease.sh/v3/covid-19/all"
response = requests.get(url)
rawData = response.json()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

data = rawData.copy()
dataIndex = data.values() 
print(data)
print(data['cases'])
print(data['deaths'])
print(data['recovered'])
x = np.array(['cases','deaths','recovered'])
y = np.array([data['cases'],data['deaths'],data['recovered']])
print(y)

plt.bar(x,y)
plt.figure(1)
plt.show() 

plt.figure(2)
plt.pie(y)
plt.show()