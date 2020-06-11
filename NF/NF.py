def nextfit(vms,server_capacity):
    servers=0
    rem=server_capacity
    for x in range(len(vms)):
        if rem>vms[x]:
            rem=rem-vms[x]
        else:
            servers+=1
            rem=server_capacity-vms[x]
    return servers

vms=[2,5,4,7,1,3,8]
server_capacity=10

print("se se necesitan ",nextfit(vms,server_capacity)," Servidores de capacidad ",server_capacity, "para las ", len(vms), "maquinas virtuales especificadas")
