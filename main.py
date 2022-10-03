import psutil as ps
import pymysql
import os
import datetime
from time import sleep
import pandas as pd 

bdsql = pymysql.connect(user='aluno', password='sptech', host='localhost', database='dadosMaquina')
cursor = bdsql.cursor()

dadosTemp = pd.read_csv("dados/ophm_trusted_02221041ryan.csv")

for i in range(200):
    print(i)
    cpuPercent = ps.cpu_percent(interval=0.1)
    ramPercent = ps.virtual_memory().percent
    discoPercent = ps.disk_usage("/").percent
    cpuTemp = dadosTemp["cpuTemp"][i]
    
    comando = 'INSERT INTO dados(cpuPercent, ramPercent, discoPercent, cpuTemp) VALUES (%s, %s, %s, %s)'
    val = (cpuPercent, ramPercent, discoPercent, cpuTemp)

    cursor.execute(comando, val)
    bdsql.commit()

print("Inserção realizada com sucesso!")