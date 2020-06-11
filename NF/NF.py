import time
from random import randrange
def nextfit(vms,server_capacity, bins):
    vms.sort(reverse=True)
    servers=0
    rem=server_capacity
    for x in range(len(vms)):
        if rem>vms[x]:
            rem=rem-vms[x]
        else:
            servers+=1
            bins.append(server_capacity-rem)
            rem=server_capacity-vms[x]
    return servers
vms_ammount=1000
vms=[]
server_capacity=10
bins=[]

for x in range(vms_ammount):
    vms.append(randrange(1,server_capacity))


start_time=time.time()
server_ammount=nextfit(vms,server_capacity,bins)
elapsed_time=time.time()-start_time

print("VMS:",vms)
print("Bins:")
for x in range(len(bins)):
    print("Server",x+1,"Espacio Usado:", bins[x])

print("se se necesitan ",server_ammount," Servidores de capacidad ",server_capacity, "para las ", len(vms), "maquinas virtuales especificadas")
print("tiempo en que se encontro esta solucion optima=",elapsed_time)
