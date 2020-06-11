import time
from random import randrange

def firstfit(vms,server_capacity):
    servers=0;
    server_rem=[0]*len(vms)

    for i in range(len(vms)):
        count=0
        for j in range(servers):
            count=j
            if server_rem[j]>=vms[i]:
                server_rem[j]=server_rem[j]-vms[i]
                break
            count=count+1
        if count==servers:
            server_rem[servers]=(server_capacity-vms[i])
            servers=servers+1
    return servers

vms_ammount=100
vms=[]
server_capacity=10

for x in range(vms_ammount):
    vms.append(randrange(1,server_capacity))


start_time=time.time()
server_ammount=firstfit(vms,server_capacity)
elapsed_time=time.time()-start_time

print("se se necesitan ",server_ammount," Servidores de capacidad ",server_capacity, "para las ", len(vms), "maquinas virtuales especificadas")
print("tiempo en que se encontro esta solucion optima=",elapsed_time)
