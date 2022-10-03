create database dadosMaquina;
use dadosMaquina;

create table dados(
id int primary key auto_increment,
cpuTemp decimal(5,2),
cpuPercent decimal(5,2),
ramPercent decimal(5,2),
discoPercent decimal(5,2) 
);

select * from dados;