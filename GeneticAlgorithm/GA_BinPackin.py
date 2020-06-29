import time
from random import randrange
import random
import os
import sys
import matplotlib.pyplot as plt

#Heuristica Online normal que calcula la cantidad de servidores usada dado un arreglo de maquinas virtuales
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

def decreasing_first_fit(vms,server_capacity):
    servers=0;
    server_rem=[0]*len(vms)
    vms.sort(reverse=True)
    for i in range(len(vms)):
        count=0
        for j in range(servers):
            count=j
            if server_rem[j] >= vms[i]:
                server_rem[j] =  server_rem[j] - vms[i]
                break
            count=count+1
        if count==servers:
            server_rem[servers] = (server_capacity - vms[i])
            servers = servers + 1
    return servers
#genera un arreglo de arreglos de maquinas virtuales ordenados al azar
def generate_population(vms,population):
    population_array=[]
    for i in range(population):
        population_array.append(random.sample(vms,len(vms)))
    return population_array


#genera una cantidad determinada de hijos con parejas de arreglos(combinando sus elementos al azar sin repetirlos)
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
                break
        if existe==False:
            child.append(parent2[i])


    return child

#algoritmo genetico que busca la cantidad minima de servidores de tamano fijo para almacenar un conunto de maquinas virtuales
# con tamanos distintos
def GeneticAlgorithm(vms,population,server_capacity):
    x=[]
    y=[]
    elapsed=0
    generations=0
    minimum_found_generation=0
    minimum_found=len(vms)+1
    time_pased=0
    minimum_array=[]
    t0=time.time()
    stable_generations=0
    mutation_percentage=5
    try:
        while stable_generations<200:
            children=[]
            new_generation=[]
            #os.system('cls' if os.name=='nt' else 'clear')
            new_generation=generate_population(vms,population)
            generations=generations+1
            stable_generations=stable_generations+1
            for i in range(int(len(new_generation)/2)):
                parent1=randrange(population)
                parent2=randrange(population)
                children.append(mating(new_generation[parent1],new_generation[parent2]))
            for i in range(len(children)):
                #mutation
                mutation=randrange(1,100)
                if mutation<=mutation_percentage:
                    pos1=randrange(len(children[i]))
                    pos2=randrange(len(children[i]))
                    children[i][pos1],children[i][pos2]=children[i][pos2],children[i][pos1]
                temp=first_fit(children[i],server_capacity)
                if temp<minimum_found:
                    stable_generations=0
                    elapsed=time.time()-t0
                    minimum_found=temp
                    minimum_found_generation=generations
                    minimum_array=children[i]
            print("generacion actual:\033[94m",generations,"\033[0m| cantidad de servers minima:\033[92m",minimum_found,"\033[m| Encontrado en Generacion:\033[92m",minimum_found_generation,"\033[0m| Tardo en encontrarlo:\033[92m",elapsed,"segundos\033[0m")
            y.append(minimum_found)
            x.append(generations)
    except KeyboardInterrupt:
        print("\nse ha salido del programa")
        print("tiempo total de ejecucion:",time.time()-t0)
        print("Mejor solucion enconrada:")
        print("Generacion:",generations,"| Solucion:",minimum_found,"| Encontrado en Generacion:",minimum_found_generation,"| Tardo en encontrarlo:",elapsed,"segundos")
        plt.plot(x,y)
        plt.xlabel('Generacion')
        plt.ylabel('Solucion encontrada')
        plt.title('Genetic Algorithm')
        plt.show()
        sys.exit()
    #en caso de que no se haga un interrupt y se haga una condicion de parada:
    print("\nNo ha habido mejoria en",stable_generations,"generaciones")
    print("se ha salido del programa")
    print("tiempo total de ejecucion:",time.time()-t0)
    print("Mejor solucion enconrada:")
    print("Generacion:",generations,"| Solucion:",minimum_found,"| Encontrado en Generacion:",minimum_found_generation,"| Tardo en encontrarlo:",elapsed,"segundos")
    plt.plot(x,y)
    plt.xlabel('Generacion')
    plt.ylabel('Solucion encontrada')
    plt.title('Genetic Algorithm')
    plt.show()
    sys.exit()
    return

def main():
    """
    testList1=[(0,98),(1,65),(2,34),(3,83),(4,74),(5,56),(6,34),(7,12),(8,3),(9,86),(10,36),(11,83),(12,23),(13,54),(14,96),(15,58),(16,77),(17,88),(18,40),(19,23),(20,43),(21,65),(22,86),(23,32),(24,22),(25,28),(26,99),(27,73),(28,65),(29,77),(30,43),(31,35),(32,37),(33,66),(34,88),(35,2),(36,54),(37,24),(38,19),(39,25),(40,55),(41,75),(42,54),(43,24),(44,73),(45,79),(46,59),(47,90),(48,10),(49,56)]
    testList2=[(0,98),(1,65),(2,34),(3,83),(4,74),(5,56),(6,34),(7,12),(8,3),(9,86),(10,36),(11,83),(12,23),(13,54),(14,96),(15,58),(16,77),(17,88),(18,40),(19,23),(20,43),(21,65),(22,86),(23,32),(24,22),(25,28),(26,99),(27,73),(28,65),(29,77),(30,43),(31,35),(32,37),(33,66),(34,88),(35,2),(36,54),(37,24),(38,19),(39,25),(40,55),(41,75),(42,54),(43,24),(44,73),(45,79),(46,59),(47,90),(48,10),(49,56)]
    testList3=[98,65,34,83,74,56,34,12,3,86,36,83,23,54,96,58,77,88,40,23,43,65,86,32,22,28,99,73,65,77,43,35,37,66,88,2,54,24,19,25,55,75,54,24,73,79,59,90,10,56]
    ff_attempt=first_fit(testList1,server_capacity)
    dff_attempt=decreasing_first_fit(testList3,server_capacity)
    """
    vm_list=[]
    totalMem=0
    server_capacity=100
    population=10
    for i in range(500):
        mem=randrange(1,server_capacity)
        vm_list.append((i,mem))
        totalMem=totalMem+mem
    print("memoria total de las maquinas virtuales:",totalMem)
    ff_attempt=first_fit(vm_list,server_capacity)
    print("resultado con heuristica first fit, servers usados:",ff_attempt)
#    print("resultado con heuristica decreasing first fit, servers usados:",dff_attempt)
    GeneticAlgorithm(vm_list,population,server_capacity)



if __name__ == '__main__':
    main()
