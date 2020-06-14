import time
def perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]



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



if __name__ == '__main__':
    VM_list=(4,8,1,4,2,1,9,9,1,1)
    server_capacity=10
    min_bins=999999999
    order=[]
    t0=time.time()
    for i in perms(VM_list):
        temp=VM_allocate(i,server_capacity)
        if min_bins>temp:
            min_bins=temp
            order=i
    elapsed=time.time()-t0
    print ("se necesita un minimo de ", min_bins,"servidores de capacidad",server_capacity,"en el orden",order)
    print ("Esta solucion optima se encontro en",elapsed,"segundos")
    exit()
