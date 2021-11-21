#Roberta Pires - 02211057
#Soluções do Monitoramento de Sistema

import psutil

nObs = 0;
i = 0;

print("Escolha uma opção para monitorar: ")
opcao_selec = input("CPU\nHD\nMemória\n\n")
if opcao_selec == "CPU":
     nObs = int(input("Quantas observações você quer ver:\n"))
     for i in range(nObs):
        if i == nObs:
            break
        print("---------------",i+1,"° Monitoramento------------------")
        print("Tempo de uso: ", psutil.cpu_times(percpu = False),"\n")
        print("Monitoramento de CPU sem intervalo: ", psutil.cpu_percent(interval = None, percpu = False),"\n")
        print("Número de CPU lógica: ", psutil.cpu_count(logical = True),"\n")
        print("Frequência: ", psutil.cpu_freq(),"\n")
        print("---------------------------------\n\n")
elif opcao_selec == "HD":
    nObs = int(input("Quantas observações você quer ver:\n"))
    for i in range(nObs):
        if i == nObs:
            break
        print("---------------",i+1,"° Monitoramento------------------")
        print("Uso de disco: ", psutil.disk_usage(),"\n")
        print("Partições de disco: ", psutil.disk_partitions(all = False),"\n")
        print("------------------------------------\n\n")
elif opcao_selec == "Memória":
    nObs = int(input("Quantas observações você quer ver:\n"))
    for i in range(nObs):
        if i == nObs:
            break
        print("---------------",i+1,"° Monitoramento------------------")
        print("Memória Virtual: ", psutil.virtual_memory(),"\n")
        print("------------------------------------\n\n")

        
