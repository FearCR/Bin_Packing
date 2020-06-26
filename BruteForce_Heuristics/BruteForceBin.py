import time
def perms(elements_tp):
    if len(elements_tp) <=1:
        yield elements_tp
    else:
        for perm in perms(elements_tp[1:]):
            for i in range(len(elements_tp)):
                yield perm[:i] + elements_tp[0:1] + perm[i:]

def first_fit(vms,server_capacity):
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
    print(vms)
    print(server_rem)
    return servers

def decreasing_first_fit(vms,server_capacity):
    servers=0;
    server_rem=[0]*len(vms)
    vms.sort(reverse=True)
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
    print(vms)
    print(server_rem)
    return servers

def VM_allocate(vms, server_capacity):#next fit
    servers=1
    rem=server_capacity
    for i in range(len(vms)):
        if rem>=vms[i]:
            rem=rem-vms[i]
        else:
            servers+=1
            rem=server_capacity-vms[i]
    return servers

def main():
    VM_tuple=(4,8,1,4,2,1,9,9,1)
    VM_list=list(VM_tuple)
    server_capacity=10
    min_bins=len(VM_list)
    order=[]
    t0=time.time()

    #BRUTE FORCE
    for i in perms(VM_tuple):
        temp=VM_allocate(i,server_capacity)
        if min_bins>temp:
            min_bins=temp
            order=i
    elapsed=time.time()-t0
    print ("Brute Force: se necesita un minimo de", min_bins,"servidores de capacidad",server_capacity,"en el orden",list(order))
    print ("Esta solucion optima se encontro en",elapsed,"segundos\n\n")

    t0=time.time()
    #FF ONLINE
    servers=first_fit(VM_list,server_capacity)
    elapsed=time.time()-t0
    print("First Fit: se encontro un minimo de",servers,"servidores de capacidad",server_capacity)
    print ("Esta solucion se encontro en",elapsed,"segundos\n\n")


    t0=time.time()
    #FF OFFLINE
    servers=decreasing_first_fit(VM_list,server_capacity)
    elapsed=time.time()-t0
    print("Decreasing First Fit: se encontro un minimo de",servers,"servidores de capacidad",server_capacity)
    print ("Esta solucion se encontro en",elapsed,"segundos\n\n")

    exit()

if __name__ == '__main__':
    main()
