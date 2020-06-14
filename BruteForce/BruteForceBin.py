import time
def perms(elements_tp):
    if len(elements_tp) <=1:
        yield elements_tp
    else:
        for perm in perms(elements_tp[1:]):
            for i in range(len(elements_tp)):
                yield perm[:i] + elements_tp[0:1] + perm[i:]



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
    VM_tuple=(4,8,1,4,2,1,9,9,1)
    VM_list=list(VM_tuple)
    server_capacity=10
    min_bins=999999999
    order=[]
    t0=time.time()
    for i in perms(VM_tuple):
        temp=VM_allocate(i,server_capacity)
        if min_bins>temp:
            min_bins=temp
            order=i
    elapsed=time.time()-t0
    print ("se necesita un minimo de ", min_bins,"servidores de capacidad",server_capacity,"en el orden",list(order))
    print ("Esta solucion optima se encontro en",elapsed,"segundos")
    exit()
