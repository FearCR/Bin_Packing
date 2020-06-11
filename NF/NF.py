def nextfit(vms,server_capacity, bins):
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

vms=[2,5,4,7,1,3,8]
server_capacity=10
bins=[]
print("se se necesitan ",nextfit(vms,server_capacity,bins)," Servidores de capacidad ",server_capacity, "para las ", len(vms), "maquinas virtuales especificadas")
print("VMS:",vms)
print("Bins:")
for x in range(len(bins)):
    print("Server",x+1,"Espacio Usado:", bins[x])
