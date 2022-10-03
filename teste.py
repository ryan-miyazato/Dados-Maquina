import pandas as pd 

brutoTemp = pd.read_csv("dados/ophm_trusted_02221041ryan.csv")
brutoApi = pd.read_csv("dados/coleta1_02221041ryan.csv")

cpuTemp = brutoTemp['cpuTemp'][1]

print(cpuTemp)