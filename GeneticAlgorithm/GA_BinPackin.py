import time
from random import randrange
import random
import os
import sys

#Heuristica normal que calcula la cantidad de servidores usada dado un arreglo de maquinas virtuales
def first_fit(vms,server_capacity):
    servers=0;
    server_rem=[0]*len(vms)

    for i in range(len(vms)):
        count=0
        for j in range(servers):
            count=j
            if server_rem[j] >= vms[i][1]:
                server_rem[j] =  server_rem[j] - vms[i][1]
                break
            count=count+1
        if count==servers:
            server_rem[servers] = (server_capacity - vms[i][1])
            servers = servers + 1
    return servers+1



def generate_population(vms,population):
    population_array=[]
    for i in range(population):
        population_array.append(random.sample(vms,len(vms)))
    return population_array



def mating(parent1,parent2):
    child=[]
    genes1=randrange(1,int(len(parent1)))
    genes2=len(parent1)-genes1
    gene=0

    for i in range(genes1):
        child.append(parent1[i])

    for i in range(len(parent2)):
        existe=False
        for j in range(len(child)):
            if parent2[i][0]==child[j][0]:
                existe=True
        if existe==False:
            child.append(parent2[i])


    return child

def GeneticAlgorithm(vms,population,server_capacity):
    elapsed=0
    generations=0
    minimum_found_generation=0
    minimum_found=len(vms)+1
    time_pased=0
    minimum_array=[]
    t0=time.time()
    try:
        while True:
            children=[]
            new_generation=[]
            #os.system('cls' if os.name=='nt' else 'clear')
            new_generation=generate_population(vms,population)
            generations=generations+1
            for i in range(int(len(new_generation)/2)):
                parent1=randrange(population)
                parent2=randrange(population)
                children.append(mating(new_generation[parent1],new_generation[parent2]))
            for i in range(len(children)):
                temp=first_fit(children[i],server_capacity)
                if temp<minimum_found:
                    elapsed=time.time()-t0
                    minimum_found=temp
                    minimum_found_generation=generations
                    minimum_array=children[i]
            print("generacion actual:",generations,"| cantidad de servers minima:",minimum_found,"| generacion en que se encontro:",minimum_found_generation,"| Tiempo transcurrido:",elapsed,"segundos")
    except KeyboardInterrupt:
        print("\nse ha salido del programa")
        sys.exit()


    return

def main():
    totalMem=0
    vm_list=[]
    server_capacity=100
    population=10
    for i in range(1000):
        mem=randrange(1,server_capacity)
        vm_list.append((i,mem))
        totalMem=totalMem+mem
    print("memoria total de las maquinas virtuales:",totalMem)
    ff_attempt=first_fit(vm_list,server_capacity)
    print("intento con heuristica first fit, bins usados:",ff_attempt)
    GeneticAlgorithm(vm_list,population,server_capacity)



if __name__ == '__main__':
    main()
