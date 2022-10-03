coleta1_02221041ryan <- read.csv("~/Documents/dados-maquina/dados/coleta1_02221041ryan.csv")
View(coleta1_02221041ryan)
ophm_trusted_02221041ryan <- read.csv("~/Documents/dados-maquina/dados/ophm_trusted_02221041ryan.csv", header=FALSE)
View(ophm_trusted_02221041ryan)

cpuPercent <- coleta1_02221041ryan$cpuPercent
cpuTemp <- ophm_trusted_02221041ryan$temperatura

plot(cpuPercent, type="l", xlab="Tempo", ylab="Medida", col="red", pch=20)
lines(cpuTemp, type="l", col="blue", pch=20)
