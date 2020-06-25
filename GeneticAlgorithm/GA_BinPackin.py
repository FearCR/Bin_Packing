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
    return servers



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

    for i in range(genes2):
        index=randrange(1,int(len(parent1)))
        



    return child

def GeneticAlgorithm(vms,population,server_capacity):
    generations=0
    minimum_found_generation=0
    minimum_found=len(vms+1)
    time_pased=0

    try:
        x=0
        while x<1000:
            #os.system('cls' if os.name=='nt' else 'clear')
            new_generation=generate_population(vms,population)
            print(new_generation)
            x=x+1
    except KeyboardInterrupt:
        print("se ha salido del programa")
        sys.exit()


    return

def main():
    vm_list=[('0',1),('1',1),('2',1),('3',1),('4',1)]
    population_array=generate_population(vm_list,2)
    #GeneticAlgorithm(vm_list,4,10)
    child=mating(population_array[0],population_array[1])
    print(child)


if __name__ == '__main__':
    main()
